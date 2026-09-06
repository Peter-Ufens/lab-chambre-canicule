# Cadre froid · Lot 1 ESP thermique (sans code)

**Date :** 2026-08-16 · suggestion Sharon · posé Karen  
**MAJ :** 2026-08-18 16h12 · E1 ESP-A entrée · E2 ESP-B coin PC · scotchés · nuit mesures  
**GO code :** après ce cadre + plan Gamma (prochain prompt) · assemblage ESP un par un

## Figé (17/08)

| Élément | Décision |
|---|---|
| Sonde E1 | Entrée / point froid (scotch le jour J) |
| Sonde E2 | Coin PC / point chaud |
| Format relevé | timestamp ISO · temp °C · humidité BME280 · id sonde |
| Fréquence brute | **1 minute** |
| Brut | **48 h glissantes** |
| Synthèse | moyennes **heure** + **jour** + **3 tranches** (00–08 / 08–16 / 16–24) dès la 1re heure |
| Dépôt Pi | SQLite 4 couches (`raw` / `hour` / `slice` / `day`) |
| Transfert PC | tiré, plus tard |
| Repo | `lab-chambre-canicule` |

Détail : `planning/2026-08-17_17h22_plan-v1_donnees-canicule-retention.md`.  
Lots : `planning/LOTS-ESP-PI-WOL-2026-08-15.md`.
