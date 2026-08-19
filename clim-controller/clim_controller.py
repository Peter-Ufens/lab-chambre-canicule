#!/usr/bin/env python3
"""Pilotage clim connectée (stub jour J) — Lab-Tiny-Peter.

Lit les sondes via le collecteur, compare aux seuils, envoie consigne / ON / OFF
via un driver interchangeable (stub par défaut, IR ou Wi-Fi plus tard).

Config : clim_config.json (copier depuis clim_config.example.json).
Par défaut enabled=false : aucun ordre réel tant que la clim n'est pas branchée.
"""
from __future__ import annotations

import json
import logging
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")
CONFIG_PATH = Path(__file__).resolve().parent / "clim_config.json"
LOG = logging.getLogger("clim-controller")


@dataclass
class SensorPoint:
    mac: str
    temp_c: float | None
    hum_pct: float | None


class ClimDriver:
    def power(self, on: bool) -> None:
        raise NotImplementedError

    def set_setpoint(self, temp_c: float) -> None:
        raise NotImplementedError

    def night_mode(self, active: bool) -> None:
        raise NotImplementedError


class StubDriver(ClimDriver):
    """Journalise les ordres. Brancher IR / API constructeur plus tard."""

    def __init__(self) -> None:
        self._on = False
        self._setpoint: float | None = None
        self._night = False

    def power(self, on: bool) -> None:
        if self._on != on:
            LOG.info("STUB clim POWER %s", "ON" if on else "OFF")
            self._on = on

    def set_setpoint(self, temp_c: float) -> None:
        if self._setpoint != temp_c:
            LOG.info("STUB clim SETPOINT %.1f C", temp_c)
            self._setpoint = temp_c

    def night_mode(self, active: bool) -> None:
        if self._night != active:
            LOG.info("STUB clim NIGHT_MODE %s", "ON" if active else "OFF")
            self._night = active


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Config manquante : {CONFIG_PATH}. "
            "Copier clim_config.example.json vers clim_config.json"
        )
    with CONFIG_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def fetch_points(url: str) -> list[SensorPoint]:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=8) as resp:
        data = json.loads(resp.read().decode())
    out: list[SensorPoint] = []
    for p in data.get("points", []):
        out.append(
            SensorPoint(
                mac=p.get("mac", ""),
                temp_c=p.get("temp_c"),
                hum_pct=p.get("hum_pct"),
            )
        )
    return out


def pick_hot_temp(points: list[SensorPoint], cfg: dict) -> float | None:
    hot_mac = cfg.get("hot_sensor_mac")
    if hot_mac:
        for p in points:
            if p.mac == hot_mac and p.temp_c is not None:
                return p.temp_c
    temps = [p.temp_c for p in points if p.temp_c is not None]
    return max(temps) if temps else None


def gap_c(points: list[SensorPoint], cfg: dict) -> float | None:
    hot_mac = cfg.get("hot_sensor_mac")
    cold_mac = cfg.get("cold_sensor_mac")
    hot = cold = None
    for p in points:
        if p.mac == hot_mac:
            hot = p.temp_c
        if p.mac == cold_mac:
            cold = p.temp_c
    if hot is None or cold is None:
        temps = [p.temp_c for p in points if p.temp_c is not None]
        if len(temps) < 2:
            return None
        return max(temps) - min(temps)
    return hot - cold


def is_night(now: datetime, cfg: dict) -> bool:
    start = int(cfg.get("night_start_hour", 22))
    end = int(cfg.get("night_end_hour", 7))
    h = now.hour
    if start < end:
        return start <= h < end
    return h >= start or h < end


def make_driver(name: str, options: dict) -> ClimDriver:
    if name == "stub":
        return StubDriver()
    raise ValueError(f"Driver inconnu : {name!r} (stub seulement pour l'instant)")


def run_once(cfg: dict, driver: ClimDriver, state: dict) -> None:
    if not cfg.get("enabled", False):
        LOG.debug("clim-controller desactive (enabled=false)")
        return

    points = fetch_points(cfg["collector_url"])
    hot = pick_hot_temp(points, cfg)
    if hot is None:
        LOG.warning("aucune temperature disponible")
        return

    now = datetime.now(PARIS)
    night = is_night(now, cfg)
    setpoint = float(
        cfg.get("setpoint_night_c", 25.0) if night else cfg.get("setpoint_day_c", 24.0)
    )
    start = float(cfg.get("start_threshold_c", 27.0))
    stop = float(cfg.get("stop_threshold_c", 25.5))
    max_gap = float(cfg.get("max_gap_c", 3.0))

    g = gap_c(points, cfg)
    if g is not None and g > max_gap:
        LOG.warning("ecart temp %.1f C > max %.1f C (E1 vs E2)", g, max_gap)

    driver.night_mode(night)
    driver.set_setpoint(setpoint)

    powered = state.get("powered", False)
    if not powered and hot >= start:
        driver.power(True)
        state["powered"] = True
        LOG.info("demarrage clim (T=%.1f >= %.1f)", hot, start)
    elif powered and hot <= stop:
        driver.power(False)
        state["powered"] = False
        LOG.info("arret clim (T=%.1f <= %.1f)", hot, stop)
    else:
        LOG.info(
            "maintien T=%.1f consigne=%.1f nuit=%s powered=%s",
            hot,
            setpoint,
            night,
            state.get("powered", False),
        )


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        stream=sys.stdout,
    )
    cfg = load_config()
    driver = make_driver(cfg.get("driver", "stub"), cfg.get("driver_options", {}))
    state: dict = {"powered": False}
    try:
        run_once(cfg, driver, state)
    except urllib.error.URLError as exc:
        LOG.error("collecteur injoignable : %s", exc)
        return 1
    except FileNotFoundError as exc:
        LOG.error("%s", exc)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
