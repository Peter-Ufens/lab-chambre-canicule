# Plan v1 — Données canicule (fréquence, rétention, tranches)

**Date :** 2026-08-17 17h22 (horodatage message Peter, dictée Windows)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ACTIF  
**But :** figer *comment* on mesure et on résume, avant d’assembler les ESP.

> **Anti-hallucination :** observé = dictée Peter 17/08 ~17h22 (2 ESP un par un, mesures, 1 ou 5 min, brut 2 j, puis synthèse heure / jour / 3 tranches, Gamma plus tard). Déduit = volume disque négligeable, usure microSD = vrai risque si on écrit à chaque minute. Inconnu = plan Gamma (Peter l’envoie au prochain prompt).

**Ne remplace pas** le plan unbox v2. Complète le cadre froid : `planning/CADRE-FROID-ESP-LOT1-2026-08-16.md`.  
**Trous ESP / NTP :** `planning/2026-08-18_13h13_plan-v2_semaine-canicule-robustesse.md` (ce v1 données reste ACTIF).

## Contexte / déclencheur

Peter a l’énergie, s’ennuie, veut **vider la tête** avant l’assemblage. Idée : 2 ESP configurés et montés **l’un après l’autre**, puis premières mesures, avec une stratégie anti-surcharge **dès le jour 1**. Présentation Gamma : plan déjà en tête, **prochain prompt**.

Le Pi (`<hostname-pi>`) est déjà OS / SSH / Connect. Il reste le **collecteur** logiciel, pas un 2ᵉ Imager.

## Décisions acquises

| Point | Décision |
|---|---|
| Ordre | ESP-A (assembler + flasher + test) → ESP-B (pareil) → collecteur Pi → **mesures** |
| Sondes | E1 entrée / point froid · E2 coin PC / point chaud (cadre 16/08) |
| Période brute | **1 minute** (pas 5) |
| Brut | **48 h glissantes** (revenir en arrière, minute par minute) |
| Synthèse | **dès la 1re heure**, pas attendre le 3ᵉ jour pour commencer |
| Heure | moyenne des ~60 points de cette heure, **par sonde** |
| Jour | 3 tranches (ci-dessous) + moyenne journalière |
| Semaines | les mêmes tranches, empilées (matin / journée / soir) |
| Purge | au-delà de 48 h, le **brut** peut partir ; les moyennes **restent** |
| Gamma | `planning/2026-08-17_17h34_plan-v1_gamma-canicule.md` · **cohérent** · slides plus tard |
| Repo | `lab-chambre-canicule` · hub Cursor = Parc |

## Fréquence : 1 minute

Peter : 1 min ou 5 min, à trancher.

**1 min.** La pièce bouge lentement, mais tu veux 48 h « au millimètre » et 60 points → 1 moyenne d’heure. 5 min = 12 points/heure, moins confortable pour le récit Gamma.

Volume : 2 sondes × 1440 points/jour × 2 j ≈ **6 000 lignes**. SQLite s’en fiche. Le vrai sujet = **ne pas marteler la microSD** : le Pi **reçoit** chaque minute, **écrit** par lots (ex. toutes les 5–15 min) ou, mieux, boot Kingston plus tard.

## Tranches de journée (3)

Dictée : 00h–08h, 09h–15h, 16h–00h. Il manquait 08h–09h et 15h–16h.

**Tranches retenues (8 h, sans trou) :**

| Id | Heures (local, Europe/Paris) | Intention |
|---|---|---|
| `nuit` | 00:00 → 08:00 | soleil pas encore / pièce froide |
| `jour` | 08:00 → 16:00 | occupation + soleil (couvre ton 09h–15h) |
| `soir` | 16:00 → 24:00 | PC / soirée |

Si tu tiens absolument à 09h–15h, on recale. Sinon on garde ça.

Chaque tranche, **par sonde** : moyenne temp, min, max, (humidité si BME). C’est la « colonne déjà pré-résumée » dès le premier soir.

## Couches stockées (Pi)

| Couche | Grain | Durée de vie |
|---|---|---|
| `raw` | 1 min · timestamp ISO · °C · %HR · id sonde | **48 h** puis drop |
| `hour` | moyenne (min/max) par heure civile | **garder** (semaines / Gamma) |
| `slice` | moyenne par `nuit` / `jour` / `soir` et par date | **garder** |
| `day` | moyenne 24 h | **garder** |

Le 3ᵉ jour n’est pas un gros ménage unique : c’est la fenêtre de 48 h qui glisse, tous les jours.

Transfert vers le PC : **tiré** quand la tour est allumée (déjà dans le plan Pi). Pas bloquant pour démarrer.

## Ordre de chantier (quand on assemble)

1. **ESP-A** : BME + cordon (Rouge 3V3, Noir GND, Bleu GPIO21, Jaune GPIO22) · câble **Gotronic** · flash test.  
2. **ESP-B** : même geste. Spare BME reste en sachet.  
3. Collecteur sur `<hostname-pi>` (HTTP + SQLite, 4 couches).  
4. Premières mesures. Gamma **après** un peu de vrai brut (au moins quelques heures, idéalement 48 h).

Pas les deux ESP en même temps. Pas de Kingston aujourd’hui. Pas de LLM.

## Limites identifiées

- Tranches 8 h : petit écart vs 09h–15h dicté.  
- 1 min + microSD : flush par lots, sinon usure.  
- Positions E1/E2 : scotch le jour J.  
- Gamma : scénario calé (`planning/2026-08-17_17h34_plan-v1_gamma-canicule.md`), slides pas encore faites.

## Ouverture

GO assemblage ESP (un par un) quand Peter le dit. Slides Gamma = session dédiée.
