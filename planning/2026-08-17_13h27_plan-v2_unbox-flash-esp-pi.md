# Plan v2 — Unbox complet, puis assemble, puis flash (ESP + Pi)

**Date :** 2026-08-17 13h27 (horodatage dictée Peter)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ACTIF  
**MAJ 18/08 :** crans **C2 + C3 ESP** faits (A et B, blink + BME USB). Collecteur Pi = encore ouvert.  
**But :** vider les cartons et **prouver que tout est là**, ensuite assembler, ensuite flasher / configurer, sur **2–3 jours**, pour le lab **et** la ligne FT « Se former en autonomie ».

> **Anti-hallucination :** observé = dictée Peter 17/08 (sortir progressivement + vérifier pièces + assembler + flasher, 2–3 j, FT). Observé aussi = switch / Ethernet long **volontairement hors commande** cet appart. Déduit = le « câble réseau » sera souvent **absent**, ce n’est pas un oubli LDLC. Inconnu = pièces réellement dans les mains (on coche aujourd’hui).

**Supplante :** v1 (`2026-08-17_13h21_plan-v1_unbox-esp-raspberry.md`) trop prudente (flash reporté). Ici on **travaille dès aujourd’hui**, flash **après** inventaire, pas avant.

## Contexte / déclencheur

Peter : ne pas seulement « ouvrir sans flasher ». D’abord **toutes les pièces sur la table**, y compris ce qu’on croit manquant (réseau). Ensuite assemblage. Ensuite configuration. Si ça prend 2–3 jours, tant mieux : le suivi FT voit déjà de l’activité.

## Décisions acquises

| Point | Décision |
|---|---|
| Ordre | **1. Inventaire vide-carton** → **2. Assemblage** → **3. Flash / OS / config** |
| Durée | **2–3 jours** OK · pas tout le même après-midi |
| FT | Lab = **Se former en autonomie** · noter chaque jour ce qui a été fait (3 lignes suffisent) |
| Flash ESP | **Autorisé après** liste cochée (GO inventaire). Pas de flash « pour voir » sur une carte non identifiée. |
| OS Pi | Raspberry Pi Imager **après** case + alim 27 W identifiée. Boot SSD = étape suivante, pas jour 1. |
| Ethernet long / switch | **Non commandé** · à cocher **ABSENT (prévu)** · WoL filaire = plus tard / autre logement |
| Câbles | StarTech = **SSD Pi** · USB Gotronic = **ESP** · ne pas mélanger |

## Ce que « fonctionnel » veut dire (3 crans)

| Cran | OK quand | Jour cible |
|---|---|---|
| **C1 Inventaire** | Chaque ligne de la liste a un objet physique (ou « absent prévu ») | **Aujourd’hui** |
| **C2 Assemblé** | Pi dans sa case · 1 ESP + 1 BME clips à froid · alims reconnues | Jour 1 soir ou **jour 2** |
| **C3 Allumé / flashé** | Pi boot (microSD d’abord) · au moins **1 ESP** qui se connecte en USB et accepte un flash test | **Jour 2–3** |

Le collecteur 24/7 + 2 sondes murales + WoL = **après** C3. Pas une exigence de ce week-end.

---

## Jour 1 (aujourd’hui) — tout sortir, rien forcer

### 1. Un seul carton à la fois

**D’abord LDLC (Pi).** Tout hors de la boîte, **sur le bureau**, sacs ouverts.  
**Ensuite Gotronic (ESP).** Même chose.  
On ne commence **pas** la case tant que les deux listes ne sont pas cochées.

### Relevé Peter 17/08 ~13h30 (carton Pi, sous les yeux)

| # | Pièce | État |
|---|---|---|
| P3 | Alim 27 W USB-C officielle | **Présente** |
| P5 | Câble USB-C ↔ USB-A (StarTech) | **Présent** |
| P4 | SSD externe 500 Go (XS2000) | **Présent** |
| P2 | Case Raspberry Pi 5 | **Présente** |
| P6 | MicroSD 64 Go | **Présente** |
| P1 | **Carte** Pi 5 8 Go (le PCB, pas la boîte) | **Présente** (Peter 17/08 ~13h32) |


| # | Pièce | Présent ? |
|---|---|---|
| P1 | Carte Pi 5 8 Go | |
| P2 | Case officiel Blanc/Rouge + ventilo | |
| P3 | Alim USB-C **27 W** officielle | |
| P4 | Kingston XS2000 500 Go | |
| P5 | StarTech USB-A → C 1 m | |
| P6 | SanDisk Extreme 64 Go + adaptateur SD | |
| P7 | Câble HDMI (tiroir maison, **pas** dans LDLC) | |
| P8 | Câble Ethernet **long** / switch | **Absent prévu** (décision 10/08) |
| P9 | Court RJ45 chambre (inventaire : **&lt; 1 m** déjà là) | noter si tu le retrouves |

P7 : sans HDMI on peut quand même flasher la microSD depuis le **PC**. Un écran + clavier Pi = confort jour 2, pas bloquant jour 1.

### Relevé Peter 17/08 ~13h36 (carton ESP, dictée Win+H)

| # | Pièce | État |
|---|---|---|
| E9–E10 | 2× câble USB-A → C (Gotronic, USB 2.0) | **Présents** |
| E11–E12 | 2× adaptateurs secteur USB-A 5 V | **Présents** |
| E1–E2 | 2× NodeMCU ESP32 USB-C (2 sacs plastique) | **Présents** |
| E3–E5 | 3× BME280 Qwiic | **Présents** (Peter 17/08 ~13h37) |
| E6–E8 | 3× cordon Qwiic → 4 femelles | **Présents** (Peter 17/08 ~13h37) |

**Cran C1 inventaire : Pi + ESP complets** (Ethernet long = absent prévu).


| # | Pièce | Présent ? |
|---|---|---|
| E1 | ESP32 USB-C n°1 | |
| E2 | ESP32 USB-C n°2 | |
| E3 | BME280 Qwiic n°1 | |
| E4 | BME280 Qwiic n°2 | |
| E5 | BME280 Qwiic spare | |
| E6–E8 | 3× cordon Qwiic → 4 femelles | |
| E9–E10 | 2× USB-A → C Gotronic | |
| E11–E12 | 2× alim mur 5 V / 1,2 A USB-A | |

Post-it dès maintenant : **ESP-A / ESP-B** · **BME-1 / BME-2 / spare**.

### 4. Fin jour 1 (minimum FT)

- Photo du **tapis de pièces** (on rangera dans `pieces/images/` si tu veux).  
- 3 lignes journal : *inventaire Pi OK / inventaire ESP OK / manques : …*  
- Si tout est là : on enchaîne **case Pi** le même jour **seulement si tu as encore de l’énergie**. Sinon stop propre, jour 2 = assemblage.

**STOP jour 1 :** pas de flash, pas de formatage SSD, pas USB PC + secteur en même temps.

---

## Jour 2 — assembler petit à petit

### Pi

1. Case : GPIO vers le haut, ports dans les trous, ventilo sur connecteur **FAN**.  
2. MicroSD 64 Go : **GO Peter 17/08 ~14h10**. Recette : `planning/liens-tutos-youtube-esp-pi-2026-08-17.md`. OS = Raspberry Pi OS 64-bit. SSD Kingston = **pas encore** le disque d’install.  
3. Alim = **27 W uniquement**. Premier boot : LED + HDMI si dispo, sinon headless plus tard.

### ESP (mécanique)

1. Clip Qwiic sur **un** BME.  
2. 4 femelles **sans forcer** : Rouge **3V3** · Noir **GND** · Bleu **GPIO21** · Jaune **GPIO22** (à recouper avec l’étiquette du cordon).  
3. Câble Gotronic + alim 5 V **identifiés**, pas branchés tant qu’on n’a pas le PC prêt pour le flash.

**STOP jour 2 :** 2e ESP et 2e BME peuvent rester en sachet. Spare BME = appairage 24 h **après** firmware.

---

## Jour 3 — flasher / configurer (le « on vérifie que ça vit »)

Ordre volontaire : **Pi d’abord** (cerveau), **un ESP ensuite** (capteur).

| Étape | Fait quand |
|---|---|
| 3a | Pi boot, mot de passe, Wi-Fi chambre (5 GHz OK pour le Pi) |
| 3b | SSH ou clavier : `hostname`, mise à jour apt **courte** |
| 3c | PC : driver / outil flash ESP (on choisit **ensemble** : Arduino IDE ou `esptool`, pas les deux) |
| 3d | **ESP-A seulement** : flash firmware **test** (blink ou sketch I2C scan). Si OK, on parle BME. |
| 3e | Wi-Fi ESP = bande **2,4 GHz** (box). Le 5 GHz du PC ne sert pas à l’ESP. |
| 3f | Journal FT : *Pi allumé · ESP-A flashé · relevé test oui/non* |

Firmware « vrai » (POST vers le Pi toutes les 5 min) = **fin jour 3 ou jour 4**, pas le premier sketch.

---

## France Travail (pour ne pas perdre le fil)

Déjà prévu : **1 ligne** « Se former en autonomie » (lots 15/08).  
Chaque séance Parc : **date + 3 puces** dans `planning/prochaines-etapes.md` (historique) et, si tu veux, la même chose dans le suivi FT.

Exemples :
- 17/08 : inventaire Pi + ESP, pièces sorties, 0 flash.  
- 18/08 : case Pi + Imager microSD.  
- 19/08 : boot Pi + flash ESP-A.

Repo public `maison-pi-lab` : **refusé**. **2 repos** : `lab-chambre-canicule` (**validé**) · `lab-wol` (pas `-nzxt`). Case Pi : clips OK · dissipateur CPU collé ensuite (vidéo `I1-7vJMhkio`).

---

## Limites identifiées (v3 probable)

- Sans HDMI sous la main, le premier boot Pi est plus abstrait (LED seulement).  
- Ethernet long **absent prévu** : WoL NZXT reste bloqué tant qu’il n’y a pas de chemin box. Le **collecteur Wi-Fi** n’en dépend pas.  
- Outil de flash ESP pas encore choisi (Arduino vs esptool).  
- SSID 2,4 GHz box : à vérifier le jour du flash ESP, pas aujourd’hui.  
- Durée 2–3 j : si Carl / FT bouffe un jour, on glisse, on n’accélère pas le GPIO.

## Ouverture v3

Quand C1 est coché (listes P et E) : v3 = **recette Imager + premier sketch ESP** avec chemins PC exacts (lecteur microSD, COM USB).
