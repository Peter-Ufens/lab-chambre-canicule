#!/bin/bash
set -euo pipefail
mkdir -p "$HOME/lab-canicule" "$HOME/.config/systemd/user"
cd "$HOME/lab-canicule"
chmod +x wifi-watchdog.sh
cp -f wifi-watchdog.service wifi-watchdog.timer "$HOME/.config/systemd/user/"
systemctl --user daemon-reload
systemctl --user enable --now wifi-watchdog.timer
systemctl --user --no-pager --lines=8 status wifi-watchdog.timer
