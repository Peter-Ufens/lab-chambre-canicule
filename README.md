# lab-chambre-canicule

Relevés chaleur **chambre** (ESP32 + BME280 → Raspberry) pour **dimensionner une clim**.  
France Travail : ligne « Se former en autonomie ».

**Hub Cursor :** [`hub-materiel`](https://github.com/Peter-Ufens/hub-materiel) (`<workspace>\hub-materiel`). Pas un 2ᵉ workspace Cursor.

Machine : **`<hostname-pi>`** (Pi 5 8 Go). Config : [`docs/pi-setup.md`](docs/pi-setup.md).  
Tutos : [`docs/tutos.md`](docs/tutos.md).  
Firmware POST : [`firmware/esp-wifi-bme/`](firmware/esp-wifi-bme/).  
Collecteur : [`collector/`](collector/).

## Statut 18/08/2026 ~15h37

| Brique | État |
|---|---|
| Pi OS / SSH / bureau Connect | **OK** |
| Collecteur HTTP + SQLite | **OK** · port **8080** · id = **MAC** |
| ESP-A | POST **OK** · MAC `YY:YY:YY:YY:YY:YY` |
| ESP-B | POST **OK** · MAC `XX:XX:XX:XX:XX:XX` |
| Placement E1/E2 | pas encore (mercredi) |
| Mini LLM sur le Pi | **non** · après canicule **et** WoL |

Repo frère : [`lab-wol`](https://github.com/Peter-Ufens/lab-wol).

Pas de Wi-Fi / mots de passe ici (`secrets.h` hors git).
