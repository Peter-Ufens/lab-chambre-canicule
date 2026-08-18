# lab-chambre-canicule

Relevés chaleur **chambre** (ESP32 + BME280 → Raspberry) pour **dimensionner une clim**.  
France Travail : ligne « Se former en autonomie ».

**Hub Cursor :** [`hub-materiel`](https://github.com/Peter-Ufens/hub-materiel) (`<workspace>\hub-materiel`). Pas un 2ᵉ workspace Cursor.

Machine : **`<hostname-pi>`** (Pi 5 8 Go). Config + captures : [`docs/pi-setup.md`](docs/pi-setup.md).  
Tutos YouTube (emboîtable, **pas de soudure**) : [`docs/tutos.md`](docs/tutos.md).  
Sketch USB (temp / hum) : [`firmware/esp-a-bme-serial/`](firmware/esp-a-bme-serial/).

## Statut 18/08/2026

| Brique | État |
|---|---|
| Pi OS / SSH / bureau Connect | **OK** (17/08) |
| ESP-A | blink + BME USB **OK** · MAC `YY:YY:YY:YY:YY:YY` |
| ESP-B | blink + BME USB **OK** · MAC `XX:XX:XX:XX:XX:XX` |
| Collecteur HTTP + SQLite | pas encore (mercredi) |
| Mini LLM sur le Pi | **non** · option après canicule **et** WoL |

Repo frère : [`lab-wol`](https://github.com/Peter-Ufens/lab-wol) (même Pi, autre sujet).

Pas de Wi-Fi / mots de passe ici.
