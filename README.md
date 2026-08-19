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



## Statut 19/08/2026



| Brique | État |

|---|---|

| Pi OS / SSH / Connect | **OK** · watchdog Wi-Fi timer |

| Collecteur HTTP + SQLite | **OK** · port **8080** · id = **MAC** |

| ESP-A (E1 entrée) + ESP-B (E2 coin PC) | **up** · nuit 17h→05h `n≈60`/h |

| Deck **Gamma** | **publié** (lien ci-dessus) |

| Repo **public** + lien IGEL | **OK** repo public · prompt jour J · AI-Lab-Journal MAJ |

| **clim-controller** (stub) | **code repo** · `enabled=false` · driver stub · timer Pi à installer |

| Mini LLM sur le Pi | **non** · après canicule **et** WoL |



Repo frère : [`lab-wol`](https://github.com/Peter-Ufens/lab-wol).



Pas de Wi-Fi / mots de passe ici (`secrets.h`, `clim_config.json` hors git).

