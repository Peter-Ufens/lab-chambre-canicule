# Liste matériel (BOM) — lab canicule

Tout public. Pas de mot de passe Wi-Fi, pas d’adresse.

## Mesure

| Qté | Article | Rôle |
|---|---|---|
| 2 | ESP32 Dev Module (USB-C, CP2102) | Sondes Wi-Fi |
| 2 | BME280 (breakout Qwiic / I2C) | Température, humidité, pression |
| 2 | Cordons Qwiic ou Dupont | Entre ESP et BME |
| 2 | Alimentation 5 V murale (USB) | Sondes en continu (pas le PC) |

## Collecteur

| Qté | Article | Rôle |
|---|---|---|
| 1 | Raspberry Pi 5 8 Go | Collecte + stub clim |
| 1 | Alimentation USB-C 27 W officielle Pi | Alimentation stable |
| 1 | SSD USB (ex. Kingston XS2000) ou microSD | OS + SQLite |
| 1 | Case Pi 5 (ventilation) | Refroidissement |

## Optionnel (jour J)

| Qté | Article | Rôle |
|---|---|---|
| 1 | Climatiseur connecté (mobile ou split) | À dimensionner après mesures |
| 1 | Pont IR / API selon marque | Branché plus tard dans `clim-controller` |

Logiciel : Arduino IDE + core Espressif, firmware `firmware/esp-wifi-bme/`, collecteur `collector/`.
