#!/usr/bin/env python3
"""Collecteur canicule — Lab-Tiny-Peter.

L'ESP pousse POST /ingest (identite = MAC). Les IP DHCP des ESP ne sont pas une cle.
Horodatage = NTP du Pi (UTC en base, Europe/Paris pour les tranches).
"""
from __future__ import annotations

import json
import sqlite3
import threading
import time
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")
UTC = timezone.utc
DOWN_AFTER_S = 180
RAW_KEEP = timedelta(hours=48)
FLUSH_EVERY_S = 300
ROLLUP_EVERY_S = 60
HOST = "0.0.0.0"
PORT = 8080
DB_PATH = Path(__file__).resolve().parent / "canicule.sqlite"

_lock = threading.Lock()
_queue: list[tuple] = []
_last_seen: dict[str, datetime] = {}
_status: dict[str, str] = {}
_clock_ok = True


def utcnow() -> datetime:
    return datetime.now(UTC)


def iso_z(dt: datetime) -> str:
    return dt.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_z(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=NORMAL")
    return con


def init_db(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS raw (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            received_at TEXT NOT NULL,
            sensor_mac TEXT NOT NULL,
            temp_c REAL,
            hum_pct REAL,
            press_hpa REAL,
            rssi INTEGER
        );
        CREATE INDEX IF NOT EXISTS idx_raw_mac_time ON raw(sensor_mac, received_at);
        CREATE TABLE IF NOT EXISTS hour (
            sensor_mac TEXT NOT NULL,
            hour_local TEXT NOT NULL,
            temp_avg REAL, temp_min REAL, temp_max REAL,
            hum_avg REAL, n_samples INTEGER NOT NULL,
            PRIMARY KEY (sensor_mac, hour_local)
        );
        CREATE TABLE IF NOT EXISTS slice (
            sensor_mac TEXT NOT NULL,
            day_local TEXT NOT NULL,
            slice_id TEXT NOT NULL,
            temp_avg REAL, temp_min REAL, temp_max REAL,
            hum_avg REAL, n_samples INTEGER NOT NULL,
            PRIMARY KEY (sensor_mac, day_local, slice_id)
        );
        CREATE TABLE IF NOT EXISTS day (
            sensor_mac TEXT NOT NULL,
            day_local TEXT NOT NULL,
            temp_avg REAL, temp_min REAL, temp_max REAL,
            hum_avg REAL, n_samples INTEGER NOT NULL,
            PRIMARY KEY (sensor_mac, day_local)
        );
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            at TEXT NOT NULL,
            sensor_mac TEXT NOT NULL,
            kind TEXT NOT NULL
        );
        """
    )
    con.commit()


def check_clock() -> None:
    global _clock_ok
    ntp = Path("/run/systemd/timesync/synchronized")
    _clock_ok = ntp.exists() if ntp.parent.exists() else True


def flush(con: sqlite3.Connection) -> None:
    with _lock:
        batch = list(_queue)
        _queue.clear()
    if not batch:
        return
    con.executemany(
        "INSERT INTO raw(received_at, sensor_mac, temp_c, hum_pct, press_hpa, rssi) VALUES (?,?,?,?,?,?)",
        batch,
    )
    cutoff = iso_z(utcnow() - RAW_KEEP)
    con.execute("DELETE FROM raw WHERE received_at < ?", (cutoff,))
    con.commit()


def slice_id_for(local: datetime) -> str:
    h = local.hour
    if h < 8:
        return "nuit"
    if h < 16:
        return "jour"
    return "soir"


def rollup_hours(con: sqlite3.Connection) -> None:
    now_p = datetime.now(PARIS)
    prev = (now_p.replace(minute=0, second=0, microsecond=0) - timedelta(hours=1))
    start = prev.astimezone(UTC)
    end = (prev + timedelta(hours=1)).astimezone(UTC)
    hour_local = prev.strftime("%Y-%m-%dT%H:00")
    rows = con.execute(
        """
        SELECT sensor_mac, AVG(temp_c), MIN(temp_c), MAX(temp_c), AVG(hum_pct), COUNT(*)
        FROM raw WHERE received_at >= ? AND received_at < ?
        GROUP BY sensor_mac
        """,
        (iso_z(start), iso_z(end)),
    ).fetchall()
    for mac, tavg, tmin, tmax, havg, n in rows:
        con.execute(
            """
            INSERT INTO hour(sensor_mac, hour_local, temp_avg, temp_min, temp_max, hum_avg, n_samples)
            VALUES (?,?,?,?,?,?,?)
            ON CONFLICT(sensor_mac, hour_local) DO UPDATE SET
              temp_avg=excluded.temp_avg, temp_min=excluded.temp_min, temp_max=excluded.temp_max,
              hum_avg=excluded.hum_avg, n_samples=excluded.n_samples
            """,
            (mac, hour_local, tavg, tmin, tmax, havg, n),
        )
    con.commit()


def rollup_slices_days(con: sqlite3.Connection) -> None:
    now_p = datetime.now(PARIS)
    today = now_p.date().isoformat()
    rows = con.execute(
        "SELECT sensor_mac, received_at, temp_c, hum_pct FROM raw"
    ).fetchall()
    buckets: dict[tuple, list] = {}
    days: dict[tuple, list] = {}
    for mac, rec, temp, hum in rows:
        local = parse_z(rec).astimezone(PARIS)
        if local.date().isoformat() != today and (now_p.date() - local.date()).days > 2:
            continue
        key_s = (mac, local.date().isoformat(), slice_id_for(local))
        key_d = (mac, local.date().isoformat())
        buckets.setdefault(key_s, []).append((temp, hum))
        days.setdefault(key_d, []).append((temp, hum))

    def stats(pts: list) -> tuple:
        temps = [p[0] for p in pts if p[0] is not None]
        hums = [p[1] for p in pts if p[1] is not None]
        if not temps:
            return None
        return (
            sum(temps) / len(temps),
            min(temps),
            max(temps),
            (sum(hums) / len(hums)) if hums else None,
            len(temps),
        )

    for (mac, day, sid), pts in buckets.items():
        st = stats(pts)
        if not st:
            continue
        con.execute(
            """
            INSERT INTO slice(sensor_mac, day_local, slice_id, temp_avg, temp_min, temp_max, hum_avg, n_samples)
            VALUES (?,?,?,?,?,?,?,?)
            ON CONFLICT(sensor_mac, day_local, slice_id) DO UPDATE SET
              temp_avg=excluded.temp_avg, temp_min=excluded.temp_min, temp_max=excluded.temp_max,
              hum_avg=excluded.hum_avg, n_samples=excluded.n_samples
            """,
            (mac, day, sid, *st),
        )
    for (mac, day), pts in days.items():
        st = stats(pts)
        if not st:
            continue
        con.execute(
            """
            INSERT INTO day(sensor_mac, day_local, temp_avg, temp_min, temp_max, hum_avg, n_samples)
            VALUES (?,?,?,?,?,?,?)
            ON CONFLICT(sensor_mac, day_local) DO UPDATE SET
              temp_avg=excluded.temp_avg, temp_min=excluded.temp_min, temp_max=excluded.temp_max,
              hum_avg=excluded.hum_avg, n_samples=excluded.n_samples
            """,
            (mac, day, *st),
        )
    con.commit()


def heartbeats(con: sqlite3.Connection) -> None:
    now = utcnow()
    with _lock:
        items = list(_last_seen.items())
    for mac, seen in items:
        age = (now - seen).total_seconds()
        want = "down" if age > DOWN_AFTER_S else "up"
        prev = _status.get(mac)
        if prev != want:
            _status[mac] = want
            con.execute(
                "INSERT INTO events(at, sensor_mac, kind) VALUES (?,?,?)",
                (iso_z(now), mac, want),
            )
            con.commit()


def worker(con: sqlite3.Connection) -> None:
    last_flush = 0.0
    last_rollup = 0.0
    while True:
        time.sleep(1)
        now = time.monotonic()
        if now - last_flush >= FLUSH_EVERY_S:
            flush(con)
            last_flush = now
        if now - last_rollup >= ROLLUP_EVERY_S:
            flush(con)
            last_flush = now
            heartbeats(con)
            rollup_hours(con)
            rollup_slices_days(con)
            check_clock()
            last_rollup = now


class Handler(BaseHTTPRequestHandler):
    con: sqlite3.Connection

    def log_message(self, fmt: str, *args) -> None:
        print("[%s] " % iso_z(utcnow()) + fmt % args)

    def _json(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path in ("/", "/health"):
            now = utcnow()
            sensors = []
            with _lock:
                seen = dict(_last_seen)
            for mac, dt in seen.items():
                age = int((now - dt).total_seconds())
                sensors.append(
                    {
                        "mac": mac,
                        "last_seen": iso_z(dt),
                        "age_s": age,
                        "status": "down" if age > DOWN_AFTER_S else "up",
                    }
                )
            self._json(
                200,
                {
                    "ok": True,
                    "clock_ok": _clock_ok,
                    "now_utc": iso_z(now),
                    "sensors": sensors,
                },
            )
            return
        if self.path == "/latest":
            rows = self.con.execute(
                """
                SELECT sensor_mac, received_at, temp_c, hum_pct, press_hpa, rssi
                FROM raw WHERE id IN (SELECT MAX(id) FROM raw GROUP BY sensor_mac)
                """
            ).fetchall()
            self._json(
                200,
                {
                    "points": [
                        {
                            "mac": r[0],
                            "received_at": r[1],
                            "temp_c": r[2],
                            "hum_pct": r[3],
                            "press_hpa": r[4],
                            "rssi": r[5],
                        }
                        for r in rows
                    ]
                },
            )
            return
        self._json(404, {"ok": False})

    def do_POST(self) -> None:
        if self.path != "/ingest":
            self._json(404, {"ok": False})
            return
        n = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(n)
        try:
            data = json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            self._json(400, {"ok": False, "err": "json"})
            return
        mac = str(data.get("mac") or "").upper().replace("-", ":")
        if len(mac) < 11:
            self._json(400, {"ok": False, "err": "mac"})
            return
        now = utcnow()
        rec = (
            iso_z(now),
            mac,
            data.get("temp_c"),
            data.get("hum_pct"),
            data.get("press_hpa"),
            data.get("rssi"),
        )
        with _lock:
            _queue.append(rec)
            prev = _last_seen.get(mac)
            _last_seen[mac] = now
            if prev is None:
                _status[mac] = "up"
        if _status.get(mac) == "down":
            _status[mac] = "up"
            self.con.execute(
                "INSERT INTO events(at, sensor_mac, kind) VALUES (?,?,?)",
                (iso_z(now), mac, "up"),
            )
            self.con.commit()
        flush(self.con)
        self._json(200, {"ok": True, "received_at": rec[0], "clock_ok": _clock_ok})


def main() -> None:
    check_clock()
    con = connect()
    init_db(con)
    Handler.con = con
    threading.Thread(target=worker, args=(con,), daemon=True).start()
    httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    print("collector http://0.0.0.0:%s  db=%s  clock_ok=%s" % (PORT, DB_PATH, _clock_ok))
    httpd.serve_forever()


if __name__ == "__main__":
    main()
