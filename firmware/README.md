# Firmware

`esp-a-bme-serial/` : test USB (I2C BME280, moniteur 115200).

`esp-wifi-bme/` : Wi-Fi + BME + POST 1 min vers le Pi. Identité = **MAC**. `secrets.h` (Wi-Fi) n’est pas dans git. Hôte collecteur = IPv4 du **Pi** (`192.168.1.25`), pas l’IP de l’ESP.
