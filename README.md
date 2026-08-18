# lab-chambre-canicule

Relevés chaleur **chambre** (ESP32 + BME280 → Raspberry) pour **dimensionner une clim**.  
France Travail : ligne « Se former en autonomie ».

**Hub Cursor :** [`Parc-Maison`](https://github.com/Peter-Ufens/Parc-Maison) (`D:\IA-CURSOR\Parc-Maison`). Pas un 2ᵉ workspace Cursor.

Machine : **`Lab-Tiny-Peter`** (Pi 5 8 Go). Config : [`docs/pi-setup.md`](docs/pi-setup.md).  
Tutos : [`docs/tutos.md`](docs/tutos.md).  
Firmware POST : [`firmware/esp-wifi-bme/`](firmware/esp-wifi-bme/).  
Collecteur : [`collector/`](collector/).

## Statut 18/08/2026 ~16h22

| Brique | État |
|---|---|
| Pi OS / SSH / bureau Connect | **OK** · watchdog Wi-Fi timer |
| Collecteur HTTP + SQLite | **OK** · port **8080** · id = **MAC** |
| ESP-A (E1 entrée) | **up** · ~27,9 °C · RSSI -13 |
| ESP-B (E2 coin PC) | **up** · ~29,4 °C · RSSI -52 |
| Nuit mesures | **en cours** |
| Vitrine Gamma / repo public | visée **mer. 19** |
| Mini LLM sur le Pi | **non** · après canicule **et** WoL |

Repo frère : [`lab-wol`](https://github.com/Peter-Ufens/lab-wol).

Pas de Wi-Fi / mots de passe ici (`secrets.h` hors git).
