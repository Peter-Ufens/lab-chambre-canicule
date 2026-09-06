# Plan v1 — Unbox ESP32 + Raspberry (assemblage sans crainte)

**Date :** 2026-08-17 13h21 (horodatage message Peter « me revoici »)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ARCHIVÉ — supplanté par v2 (`planning/2026-08-17_13h27_plan-v2_unbox-flash-esp-pi.md`)  
**But :** sortir les cartons, identifier chaque pièce, monter le Pi dans sa case, poser les ESP sans les flasher.

> **Anti-hallucination :** observé = lots reçus (inventaire 17/08), Wave:3 déjà OK. Déduit = ordre Pi d’abord (plus de pièces mécaniques). Inconnu = Facecam encore à confirmer (hors ce plan).

## Contexte / déclencheur

Pause linge terminée. Audio (SD+ / Wave:3 / DT 700) OK. Peter demande **quoi déballer en premier** et un plan pour assembler **sans crainte**.

Lots **1** (ESP thermique) et **2** (Pi) restent **dans hub-materiel**. Pas de 2ᵉ projet Cursor.

## Décisions acquises

| Point | Décision |
|---|---|
| Ordre | **Raspberry d’abord**, ESP ensuite |
| Flash ESP | **Interdit** tant que Peter n’a pas dit **GO** |
| OS Pi | **Pas aujourd’hui** sauf GO explicite (imagerie / boot SSD) |
| Alim Pi | **Uniquement** le bloc officiel **27 W** (pas un chargeur téléphone) |
| Ethernet long / switch | **Non** cet appart |
| Câble StarTech A→C 1 m | **Réservé au SSD XS2000 ↔ Pi** (pas aux ESP) |
| Câbles USB-A→C Gotronic | **Réservés aux 2 ESP32** |

## Réponse courte : on déballe quoi en premier ?

**Le Raspberry (lot LDLC).** Case + ventilo + carte + alim. C’est le montage le plus « cassable » si on force.  
Les ESP : on les **étale et on les nomme** après, sans 5 V tant qu’on n’a pas fini le Pi.

---

## Table GO / STOP (à garder sous les yeux)

**GO (aujourd’hui)**  
- Ouvrir cartons, poser sur le bureau, cocher la liste  
- Enfiler le Pi dans la **case officielle** + ventilo  
- Brancher l’alim 27 W **à vide** (sans allumer longtemps) pour voir si la LED s’allume, **ou** attendre le GO OS  
- Clipper **à froid** un cordon Qwiic sur un BME280 (sans USB, sans secteur)

**STOP (pas aujourd’hui, sauf GO Peter)**  
- Flasher un ESP32  
- Brancher **USB PC + chargeur 5 V** en même temps sur un ESP  
- Forcer des Dupont sur les broches  
- Formater / installer l’OS sur le Kingston XS2000  
- Utiliser un hub USB, un chargeur PD random, ou l’alim Pi pour un ESP  
- Tirer un Ethernet jusqu’à la box

---

## Partie A — Raspberry (premier carton)

### A0. Espace

Bureau dégagé. Pas de tapis qui peluche dans les GPIO. Pi **hors sac antistatique** seulement au moment du montage.

### A1. Inventaire (cocher à voix haute)

| # | Pièce | Attendu |
|---|---|---|
| 1 | Carte Pi 5 **8 Go** | PCB vert, ports USB, HDMI, USB-C alim |
| 2 | Case **Blanc/Rouge** + ventilo intégré | Officielle Pi 5 |
| 3 | Alim **USB-C 27 W** officielle | Gros bloc, pas 5 W téléphone |
| 4 | Kingston **XS2000 500 Go** | SSD USB-C compact |
| 5 | StarTech **USB-A → C 1 m** | Pour le SSD, plus tard |
| 6 | SanDisk Extreme **64 Go** + adapt. SD | Secours / 1er flash OS, **pas** le 24/7 |

Si une pièce manque : on **arrête** et on note. On ne « complète pas » avec un autre câble.

### A2. Montage case (lent)

1. Ouvrir la case selon la notice (clips, pas tournevis forcé).  
2. Poser le Pi **à plat**, GPIO vers le haut, ports alignés avec les trous.  
3. Ne **pas** appuyer sur les puces. Ne **pas** tordre les broches GPIO.  
4. Ventilo : nappe vers le connecteur **FAN** du Pi (petit connecteur dédié), pas un GPIO au hasard.  
5. Refermer la case. Vérifier USB / HDMI / USB-C alim accessibles.  
6. **Ne pas** enfoncer la microSD « pour voir » si on n’installe pas l’OS.

### A3. SSD (pose seulement)

- XS2000 **fermé**, on ne le formate pas.  
- StarTech : un bout USB-C dans le SSD, l’autre **USB-A bleu (USB 3)** du Pi **plus tard**, au boot.  
- Aujourd’hui : câble **à côté** de la case, étiquette mentale « Pi SSD ».

### A4. Premier allumage (optionnel, 10 s)

Seulement si Peter veut voir une LED : alim 27 W → USB-C **alim** du Pi (pas un port USB).  
Sans microSD / sans SSD : le Pi peut rester sur écran d’attente. **Couper** après 10 s. Ce n’est pas une install.

---

## Partie B — ESP32 (deuxième carton, après le Pi)

### B1. Inventaire Gotronic (112,40 €)

| Qté | Pièce | Rôle |
|---:|---|---|
| 2 | NodeMCU ESP32 **USB-C** | Cartes (E1 / E2 plus tard) |
| 3 | BME280 Pimoroni **Qwiic** | 2 sondes + 1 spare |
| 3 | Cordon Qwiic → **4 femelles** | 0 soudure |
| 2 | USB-A → USB-C **Gotronic** | Alim des ESP (pas le StarTech) |
| 2 | Adaptateur mur **5 V / 1,2 A** USB-A | Secteur, **pas** PD-only |

### B2. Identifier sans alimenter

- Marquer au feutre (ou post-it) : **ESP-A**, **ESP-B**, **BME-1 / 2 / spare**.  
- Les 3 BME : Sharon = 24 h côte à côte **après** firmware. Pas aujourd’hui.

### B3. Dry-fit (sans courant)

Brochage **si** tu clips (rappel Gotronic, à revérifier sur le carton) :

| Fil | ESP32 |
|---|---|
| Rouge | **3V3** (jamais 5 V) |
| Noir | **GND** |
| Bleu | **GPIO21** SDA |
| Jaune | **GPIO22** SCL |

Si ça résiste : **on force pas**. On laisse pour le GO flash.

### B4. Alim plus tard (après GO firmware)

Ordre alors : chargeur 5 V → câble Gotronic A→C → ESP **seul**.  
Jamais USB du PC **et** chargeur mur en même temps.

Emplacements **plus tard** (pas coller au mur aujourd’hui) :

| ID | Lieu |
|---|---|
| E1 | Entrée · triangle + répéteur · BME 1,1–1,5 m |
| E2 | Coin PC · ~50 cm de la tour |

---

## Ordre de séance proposé (maintenant)

1. Carton **Pi** : liste A1.  
2. Case A2. Photo si tu veux (on rangera dans `pieces/images/`).  
3. SSD + StarTech **à côté**, pas branchés.  
4. Carton **ESP** : liste B1.  
5. Dry-fit **un** BME si tu es à l’aise, sinon stop.  
6. On s’arrête. Flash / OS = **autre round + GO**.

## Limites identifiées (pourquoi une v2 viendra)

- Pas de photos des pièces ouvertes : l’inventaire peut encore rater un accessoire case.  
- Notice case Pi 5 : orientation ventilo à confirmer **sur le plastique**, pas de mémoire.  
- Brochage Dupont : recopié du panier 07/08, à recouper avec l’étiquette du cordon **dans la main**.  
- Allumage Pi 10 s : optionnel, peut angoisser sans écran HDMI.  
- WoL / Ethernet chambre : hors scope, le Pi restera Wi-Fi pour le collecteur.

## Ouverture v2

Après unbox : photos + cases cochées → v2 = **premier flash OS Pi** (microSD secours) **ou** GO ESP, au choix de Peter, pas les deux le même souffle.
