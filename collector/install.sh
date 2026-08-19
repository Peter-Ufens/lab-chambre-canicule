#!/bin/bash
set -euo pipefail
mkdir -p "$HOME/lab-canicule" "$HOME/.config/systemd/user"
cd "$HOME/lab-canicule"
chmod +x "$HOME/lab-canicule/collector.py" || true
cp -f "$HOME/lab-canicule/canicule-collector.service" "$HOME/.config/systemd/user/"
loginctl enable-linger "$USER" || true
systemctl --user daemon-reload
systemctl --user enable --now canicule-collector.service
sleep 1
systemctl --user --no-pager --lines=20 status canicule-collector.service
curl -sS http://127.0.0.1:8080/health || true
