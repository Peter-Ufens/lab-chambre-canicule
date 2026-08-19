#!/bin/bash
# Exporte les moyennes SQLite pour coller dans le prompt IA (jour J).
# Usage : bash export-mesures-pour-ia.sh > mesures.txt
set -euo pipefail
DB="${1:-$HOME/lab-canicule/canicule.sqlite}"
if [ ! -f "$DB" ]; then
  echo "Base introuvable : $DB" >&2
  exit 1
fi
echo "=== MOYENNES PAR HEURE (Paris) ==="
sqlite3 -header -column "$DB" "
SELECT sensor_mac, hour_local, n_samples,
       ROUND(temp_avg, 2) AS temp_c,
       ROUND(temp_min, 2) AS t_min,
       ROUND(temp_max, 2) AS t_max,
       ROUND(hum_avg, 1) AS hum_pct
FROM hour ORDER BY hour_local, sensor_mac;
"
echo
echo "=== MOYENNES PAR TRANCHE (jour) ==="
sqlite3 -header -column "$DB" "
SELECT sensor_mac, day_local, slice_id, n_samples,
       ROUND(temp_avg, 2) AS temp_c
FROM slice ORDER BY day_local, slice_id, sensor_mac;
"
