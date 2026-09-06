# Brief Sharon · ESP32 ×2 (W2bis) vs écosystème Peter

**De :** Karen (Cursor · hub-materiel)  
**Pour :** Sharon (Claude Desktop)  
**Date :** 2026-08-07  
**Demande Peter :** analyser si le matériel listé convient aux **besoins des projets** ; sinon **proposer des équipements adaptés**.  
**Contexte achat :** solution **C** (Gotronic DIY + LDLC secteur) · liens prêts · **pas encore GO commande** · triangle multiprise **déjà chez Peter**.

---

## 0. Mission Sharon (lecture seule + avis)

1. Lire ce brief + fiches Parc liées.  
2. Croiser avec les projets actifs / pause de l’écosystème (INDEX + notes vault).  
3. Dire clairement : **OK / OK avec réserves / pas adapté** pour chaque usage.  
4. Si pas adapté : **alternative concrète** (réf. type + pourquoi), sans ouvrir un nouveau monolithe.  
5. Réponse collable dans Parc : `planning/avis-sharon-esp32-ecosysteme-2026-08-07.md` (Peter / Karen colleront).

**Hors brief :** commander à la place de Peter · toucher ProgramData · rouvrir clim Canicule · dimensionner Raspberry (file U séparée).

---

## 1. Matériel proposé (panier C)

### 1.1 Cœur DIY · Gotronic

| Qté | Équipement | Lien / code | Rôle technique |
|---:|---|---|---|
| 2 | NodeMCU **ESP32** USB-C (Wi-Fi + BT · DevKit) | https://www.gotronic.fr/art-module-nodemcu-esp32-usb-c-47499.htm · **39126** · ~14,30 € · stock ~49 | MCU lab LAN |
| 2 | Module **BME280** I2C (temp + humidité + pression) | https://www.gotronic.fr/art-module-bme280-sku27347-37634.htm · **38419** · stock ~58 | Capteur env. |
| 1 | Pack 20 câbles Dupont F/F (+ M/M) | https://www.gotronic.fr/art-pack-de-20-cables-de-connexion-f-f-bbj19-26569.htm · **12331** | Câblage I2C |
| 2 | Câble USB-A→C (ou C→C) | Gotronic / LDLC / stock maison | Alim 5 V + flash firmware |

Alt. stock : ESP32 micro-USB **35989** · BME premium PIM472 **38928**.

### 1.2 Secteur · LDLC (Peter achète Pi ici plus tard)

| Qté | Équipement | Lien type | Note |
|---:|---|---|---|
| 2 | Chargeur secteur USB ≥1 A/port | Ex. https://www.ldlc.com/fiche/PB00410889.html (Akashi 4×USB 5A) ou USB-C 20–36 W | **1 par emplacement** |
| 0 | Multiprise triangle | — | **Déjà possédée** (entrée) |

### 1.3 Ce que ce n’est PAS

- Pas un Raspberry Pi (file **U** · tunnel CF / WoL distant / always-on).  
- Pas Shelly / station météo fermée.  
- Pas ESP32-CAM (Vision = C920 / Lyla-Vision).  
- Papier CF 06/08 : ESP32 = **lab local** · Pi = always-on distant.

---

## 2. Positions physiques (chambre Guillemites)

```
[ Entrée chambre ]                    [ Coin bureau / NZXT ]
 Prise murale                          Prise / multiprise bureau
    └─ Multiprise TRIANGLE (déjà là)        └─ Chargeur USB mural (à acheter)
         ├─ Répéteur Wi-Fi (.18)                  └─ ESP32 #2 (E2) + BME280 #2
         └─ Chargeur USB mural (à acheter)
              └─ ESP32 #1 (E1) + BME280 #1
```

| ID | Emplacement | Alim | Capteur | Rôle phase 1 | Rôle après Raspberry (file U) |
|---|---|---|---|---|---|
| **E1** | **Entrée chambre** (près répéteur Wi-Fi) | Secteur → chargeur USB 5 V sur triangle | BME280 #1 | **Thermique durable** (temp/humidité) | **Reste** capteur chambre |
| **E2** | **Coin PC** (bureau NZXT · `<poste>` `.12`) | Secteur → chargeur USB 5 V sur multiprise bureau | BME280 #2 | Thermique **temporaire** | **Recyclable** : WoL lab (W1) et/ou autre micro-projet |

Réseau cible : Wi-Fi maison `<reseau-local>/24` · même LAN que NZXT, Redmi, répéteur, etc. (`hub-materiel/context/reseau-lan.md`).

---

## 3. Usages croisés écosystème (à valider)

| Projet / fil | Besoin potentiel ESP32 | E1 / E2 ? | Adequation DevKit ESP32 + BME280 (avis Karen) | Question pour Sharon |
|---|---|---|---|---|
| **hub-materiel** W2bis | Inventaire · 2 points mesure | E1+E2 | **OK** cœur du panier | Confirmer BME280 vs AHT20 / SHT |
| **Canicule** (pause · reprise ~02/2027) | Données temp/humidité chambre (pas achat clim) | surtout **E1** | **OK** pour logger · pas pour piloter clim | Suffit-il pour décisions thermiques plus tard ? |
| **Nora-n8n** | Webhook / MQTT léger depuis capteurs | E1 (et E2 phase 1) | **OK** (HTTP/MQTT client) | Préférer MQTT, HTTP, ou attendre Pi ? |
| **Parc W1 WoL lab** | Magic packet LAN vers NZXT | plutôt **E2** après Pi | **OK** (Wi-Fi UDP) | ESP32 classique suffit vs module Ethernet ? |
| **Cloudflare / RDP distant** | Tunnel + Access + WoL distant | **Pi**, pas ESP32 | ESP32 **non** comme always-on distant (aligné papier 06/08) | Confirmer : aucun ESP32 derrière CF ? |
| **Lyla-App / Memory / Orchestrator** | Pas de MCU requis | — | N/A | — |
| **Lyla-Vision / Avatar** | Caméra / UE | — | ESP32-CAM **hors** panier | Ne pas dériver vers CAM |
| **Lyla (signal bureau) W3** | LED / bouton feedback | possible **E2** plus tard | **OK** GPIO | Besoin bouton/LED dès l’achat ? |
| **Carl-Agent / Sport / Suivi-Pro** | — | — | N/A | — |

Karen : le **DevKit ESP32 générique** (pas S3 obligatoire) couvre thermique + WoL lab + webhook + GPIO. L’**ESP32-S3** n’est utile que si Sharon voit un besoin AI/caméra edge (hors scope actuel).

---

## 4. Fiches Parc à lire (chemins)

| Fichier | Contenu |
|---|---|
| `<workspace>\hub-materiel\planning\panier-commande-esp32-solution-c-2026-08-07.md` | Liens commande C |
| `<workspace>\hub-materiel\planning\recherche-esp32-capteurs-chambre-2026-08-07.md` | Recherche + BOM + LDLC |
| `<workspace>\hub-materiel\context\pistes-esp32.md` | W1 / W2 / W2bis / W3 |
| `<workspace>\hub-materiel\planning\prochaines-etapes.md` | File W |
| Vault | `04-Idees/IDEE-Wake-on-LAN-ESP32.md` · `ESP32-vs-Raspberry-Pi-Comparatif.md` |
| A-traiter | `2026-08-06-cloudflare-rdp-wol-access-papier.md` · ESP32 = lab local |

---

## 5. Format de réponse souhaité (Sharon)

```markdown
# Avis Sharon · ESP32 W2bis · 2026-08-07

## Verdict global
OK / OK avec réserves / Revoir panier

## Par usage (tableau)
| Usage | Verdict | Commentaire | Alt. si besoin |

## Matériel
- ESP32 USB-C NodeMCU : ...
- BME280 : ...
- Alim LDLC : ...
- Manque éventuel (LED, bouton, boîtier, Ethernet, S3…) : ...

## Positions E1 / E2
Confirmer ou ajuster rôles.

## Risques
(ex. faux BME280=BMP280, chaleur coin PC fausse la mesure, Wi-Fi 2,4 GHz only…)

## Recommandation avant GO Peter
1. ...
2. ...
```

---

## 6. Rappel budget (sans triangle)

Gotronic ~**45–55 €** + LDLC chargeurs ~**20–40 €** → total ~**65–95 €** + ports.
