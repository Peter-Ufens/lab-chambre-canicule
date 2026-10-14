# lab-chambre-canicule

Relevés chaleur **chambre** (ESP32 + BME280 → Raspberry) pour **dimensionner une clim**.  
France Travail : ligne « Se former en autonomie ».

**GitHub :**
- **Privé (ops) :** https://github.com/Peter-Ufens/lab-chambre-canicule-private · remote `origin`
- **Public (vitrine) :** https://github.com/Peter-Ufens/lab-chambre-canicule · remote `public`  
Détail : [`REPOS.md`](REPOS.md). **≠** [`lab-wol`](https://github.com/Peter-Ufens/lab-wol).

**Statut INDEX :** **`cloture`** · voir [`CLOTURE.md`](CLOTURE.md) · collecte **continue** · reprise ops après fibre ~**16/09** + GO Peter.

**Présentation Gamma (04c) :**  
https://gamma.app/docs/Canicule-pas-de-clim-comment-ne-pas-se-tromper-dappareil-0y21j1gd58cd990  
Plans / prompts : [`presentations-gamma/`](presentations-gamma/).

**Workspace Cursor :** ce repo. Matériel Pi / inventaire : [`hub-materiel`]((hub matériel privé)) ([local](../hub-materiel/LIRE-EN-PREMIER.md)).  
Frère WoL (+ mini-LLM prévu) : [`lab-wol`](https://github.com/Peter-Ufens/lab-wol) ([local](../lab-wol/README.md)).  
Plans ops : [`planning/`](planning/).

Machine : **`<hostname-pi>`** (Pi 5 8 Go). Config : [`docs/pi-setup.md`](docs/pi-setup.md).  
Tutos : [`docs/tutos.md`](docs/tutos.md).  
Firmware POST : [`firmware/esp-wifi-bme/`](firmware/esp-wifi-bme/).  
Collecteur : [`collector/`](collector/).  
Pilotage clim (stub jour J) : [`clim-controller/`](clim-controller/).  
**Prompt IA jour J** : [`docs/prompt-dimensionnement-clim.md`](docs/prompt-dimensionnement-clim.md) · BOM : [`docs/bom-materiel.md`](docs/bom-materiel.md)

---

## Clôture vitrine · 19/08/2026

**Statut projet dev / FT : clôturé.**  
Le lab **continue de tourner** en exploitation (collecte jusqu’au jour J clim).

| Livrable | État |
|---|---|
| Pi + collecteur + 2 sondes | **OK** · exploitation |
| Deck Gamma + repo **public** | **OK** · `presentations-gamma/` |
| Prompt jour J + BOM + stub clim | **OK** |
| Index AI-Lab-Journal (04c) | **OK** |
| Envoi lien IGEL | **Peter** (Suivi-Pro) |

**Hors périmètre clôture 19/08** (volontaire) : 14 jours de mesures formelles · achat clim · driver IR réel.

### Suite gelée jusqu’à fibre stable (~16/09) · voir CLOTURE.md

1. Check LAN + relevés **19/08 → jour résolution fibre** (sans retoucher Wi-Fi Pi avant).
2. Kingston XS2000 sur le Pi.
3. Mini-LLM → **[`lab-wol`](../lab-wol/README.md)** (pas ici).
4. Export / dimensionnement clim au GO · achat → projet [`Canicule`](../Canicule/LIRE-EN-PREMIER.md) ~02/2027.

Pas de Wi-Fi / mots de passe ici (`secrets.h`, `clim_config.json` hors git).
