# Pilotage clim (stub)

Prêt pour le **jour J** (achat clim connectée). Aujourd'hui : driver **stub** (journalise ON/OFF, consigne, mode nuit). `enabled=false` par défaut.

## Installer sur le Pi

```bash
cd ~/lab-canicule
# copier depuis le repo : clim_controller.py, clim_config.example.json, install.sh, *.service, *.timer
cp clim_config.example.json clim_config.json   # si pas deja fait
bash install.sh
```

## Config (`clim_config.json`)

| Cle | Role |
|---|---|
| `enabled` | `false` tant que pas de clim branchée |
| `start_threshold_c` | au-dessus : démarrage |
| `stop_threshold_c` | en dessous : arrêt (hystérésis) |
| `setpoint_day_c` / `setpoint_night_c` | consigne jour / nuit |
| `night_start_hour` / `night_end_hour` | plage mode nuit (heure Paris) |
| `hot_sensor_mac` / `cold_sensor_mac` | E2 / E1 pour écart max |
| `driver` | `stub` pour l'instant |

## Jour J

1. Brancher la clim (IR, Wi-Fi marque, etc.).
2. Ajouter un driver dans `clim_controller.py` (ou module `drivers/`).
3. Mettre `enabled: true` dans `clim_config.json`.
4. `systemctl --user restart clim-controller.timer`

Logs : `journalctl --user -u clim-controller.service -n 30`
