# lab-chambre-canicule

Relevés chaleur **chambre** (ESP32 + BME280 → Raspberry) pour **dimensionner une clim**.  
France Travail : ligne « Se former en autonomie ».

**Hub Cursor :** [`hub-materiel`](https://github.com/Peter-Ufens/hub-materiel) (`<workspace>\hub-materiel`). Pas un 2ᵉ workspace Cursor.

Machine : **`<hostname-pi>`** (Pi 5 8 Go). Config + captures : [`docs/pi-setup.md`](docs/pi-setup.md).

## Statut 17/08/2026

| Brique | État |
|---|---|
| Pi OS / SSH / bureau Connect | **OK** |
| Collecteur HTTP + SQLite | pas encore |
| ESP32 + BME280 | matériel là · **pas flashé** |
| Mini LLM sur le Pi | **non** · option après canicule **et** WoL |

Repo frère : [`lab-wol`](https://github.com/Peter-Ufens/lab-wol) (même Pi, autre sujet).

Pas de Wi-Fi / mots de passe ici.
