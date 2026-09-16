# Firmware

`esp-a-bme-serial/` : test USB (I2C BME280, moniteur 115200).

`esp-wifi-bme/` : Wi-Fi + BME + POST 1 min vers le Pi. Identité = **MAC**. `secrets.h` (Wi-Fi + IP collecteur) n’est pas dans git (voir `secrets.h.example` avec placeholders). Hôte collecteur = IPv4 du **Pi** (`COLLECTOR_HOST` dans `secrets.h`), pas l’IP de l’ESP. Remotes : [`REPOS.md`](../REPOS.md).
