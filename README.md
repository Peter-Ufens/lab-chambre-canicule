# lab-chambre-canicule

Relevés chaleur **chambre** (ESP32 + BME280 → Raspberry) pour **dimensionner une clim**.  
France Travail : ligne « Se former en autonomie ».

**Présentation Gamma (FT) :**  
https://gamma.app/docs/Canicule-pas-de-clim-comment-ne-pas-se-tromper-dappareil-0y21j1gd58cd990

**Hub Cursor :** [`Parc-Maison`](https://github.com/Peter-Ufens/Parc-Maison) (`D:\IA-CURSOR\Parc-Maison`). Pas un 2ᵉ workspace Cursor.

Machine : **`Lab-Tiny-Peter`** (Pi 5 8 Go). Config : [`docs/pi-setup.md`](docs/pi-setup.md).  
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
| Deck Gamma + repo **public** | **OK** |
| Prompt jour J + BOM + stub clim | **OK** |
| Index AI-Lab-Journal (04c) | **OK** |
| Envoi lien IGEL | **Peter** (Suivi-Pro) |

**Hors périmètre clôture** (volontaire) : 14 jours de mesures · achat clim · driver IR réel · Kingston (sauf saturation Pi, voir ci-dessous).

### Exploitation continue

- Les ESP envoient toujours (1/min → SQLite sur le Pi).
- **Jour J clim** : `scripts/export-mesures-pour-ia.sh` → prompt dans `docs/prompt-dimensionnement-clim.md`.
- **Kingston XS2000** : **pas maintenant**. Migration si le Pi **sature** (disque, lenteur microSD, collecte) **ou** avant mini LLM (voir Parc-Maison `planning/idee-mini-llm-pi-apres-labs-2026-08-17.md`).

### Brique technique (19/08)

| Brique | État |
|---|---|
| Pi OS / SSH / Connect | **OK** · watchdog Wi-Fi timer |
| Collecteur HTTP + SQLite | **OK** · port **8080** · id = **MAC** |
| ESP-A (E1 entrée) + ESP-B (E2 coin PC) | **up** · exploitation |
| **clim-controller** (stub) | **installé Pi** · `enabled=false` · driver stub |

**Suite Parc-Maison :** lot 2 [`lab-wol`](https://github.com/Peter-Ufens/lab-wol) puis mini LLM Pi. Plan : `Parc-Maison/planning/2026-08-19_plan-v1_wol-llm.md`.

Pas de Wi-Fi / mots de passe ici (`secrets.h`, `clim_config.json` hors git).
