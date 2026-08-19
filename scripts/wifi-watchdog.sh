#!/bin/bash
# Relance le Wi-Fi du Pi si la passerelle ne repond plus.
# Ne reboote pas (Connect + collecteur restent possibles apres un simple reconnect).
set -u
PATH=/usr/sbin:/usr/bin:/sbin:/bin

ping_ok() {
  ping -c 1 -W 2 "$1" >/dev/null 2>&1
}

GW="$(ip -4 route show default 2>/dev/null | awk '{print $3; exit}')"
if [ -n "${GW:-}" ] && ping_ok "$GW"; then
  exit 0
fi
if ping_ok 192.168.1.1; then
  exit 0
fi

logger -t wifi-watchdog "passerelle muette, reconnect wlan0 (box ou repetiteur)"
nmcli -g NAME,DEVICE connection show --active | while IFS=: read -r name dev; do
  if [ "$dev" = "wlan0" ]; then
    nmcli connection modify "$name" connection.autoconnect yes connection.autoconnect-retries -1 || true
  fi
done
nmcli device disconnect wlan0 >/dev/null 2>&1 || true
sleep 2
if ! nmcli device connect wlan0 >/dev/null 2>&1; then
  nmcli networking off || true
  sleep 1
  nmcli networking on || true
fi
logger -t wifi-watchdog "reconnect tente"
exit 0
