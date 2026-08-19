#!/bin/bash
set -euo pipefail
mkdir -p "$HOME/lab-canicule" "$HOME/.config/systemd/user"
cd "$HOME/lab-canicule"
if [ ! -f clim_config.json ]; then
  cp -f clim_config.example.json clim_config.json
  echo "clim_config.json cree (enabled=false par defaut)"
fi
chmod +x "$HOME/lab-canicule/clim_controller.py" || true
cp -f "$HOME/lab-canicule/clim-controller.service" "$HOME/.config/systemd/user/"
cp -f "$HOME/lab-canicule/clim-controller.timer" "$HOME/.config/systemd/user/"
loginctl enable-linger "$USER" || true
systemctl --user daemon-reload
systemctl --user enable --now clim-controller.timer
sleep 1
systemctl --user --no-pager --lines=10 status clim-controller.timer
echo "Test manuel : python3 ~/lab-canicule/clim_controller.py"
