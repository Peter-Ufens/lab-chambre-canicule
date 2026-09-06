# Plan v2 — Semaine canicule (trous ESP + heure NTP)

**Date :** 2026-08-18 13h13 (horodatage message Peter)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ACTIF  
**But :** confirmer qu’on n’avance **pas à l’aveugle**, et figer deux trous : ESP down, horloge / changement d’heure.

> **Anti-hallucination :** observé = plans 17/08 déjà écrits · dictée 18/08 (ESP débranché / coupure, NTP fuseau, DST déjà vu en prod). Déduit = l’ESP n’a pas une horloge fiable, le Pi horodate. Inconnu = durée réelle de la pause avant ESP-A aujourd’hui.

**Supplante :** v1 semaine (`planning/2026-08-17_17h45_plan-v1_semaine-canicule-deadline-jeudi.md`) pour le calendrier du jour. Les v1 **données** et **Gamma** restent valides.

## On n’est pas à l’aveugle

| Fichier | Rôle |
|---|---|
| `…17h22…donnees-canicule-retention.md` | 1 min, 48 h brut, moyennes, 3 tranches |
| `…17h34…gamma-canicule.md` | récit Gamma FT |
| v1 semaine 17h45 | deadline **jeu. 20/08** · mar. ESP / mer. collecteur / jeu. vitrine |
| **Ce v2** | ESP manquant + NTP / DST + mardi décalé |

## Mardi 18 (ajusté)

Matin : urgences Vladymir + IKEA (lit). Reprise ~13h. **Pause**, puis ESP-A **quand l’énergie est là**.

Même geste qu’en v1 : un par un, Gotronic, pas les deux alims. Un ESP qui lit le BME suffit pour mercredi.

Deadline jeudi **inchangée** : 1 sonde + Pi + README + Gamma reste un envoi honnête.

## Ce que cette version apporte

- Index des plans déjà là (on ne repart pas de zéro).
- ESP manquant : heartbeat, `n_samples`, pas d’invention de °C.
- Heure : UTC en base, Paris à l’affichage, NTP sur le Pi, ESP pas horloge.
- Mardi recalé (urgences + IKEA) sans bouger jeudi.

## ESP down (prise, coupure, Wi-Fi)

Un ESP éteint ≠ une température de 0 °C. On **n’invente pas**.

| Règle | Détail |
|---|---|
| Horodatage | Le Pi pose `received_at` en **UTC** (NTP). L’ESP n’est pas la source de vérité de l’heure. |
| Heartbeat | Pas de POST depuis **3 min** → sonde `down` (événement dans les logs). Retour → `up`. |
| Moyennes | Uniquement les points **reçus**. Stocker `n_samples` (ex. 12/60 si une demi-heure morte). |
| Deux sondes | E1 down n’empêche pas E2. On ne fusionne pas les deux pour « remplir le trou ». |
| Pi down | À la reprise : NTP d’abord, puis on reprend. Pas de rattrapage magique des minutes perdues. |
| Gamma / IA | Le prompt dira : si `n_samples` trop bas, **ne pas** conclure une clim sur cette heure. |

Cause indifférenciée côté collecteur (prise tirée, disjoncteur, Wi-Fi) : on voit un **trou**, pas le pourquoi. Optionnel plus tard : LED / page « E1 last seen ».

## Heure monde (NTP + changement d’heure)

Leçon admin : pannes au **changement d’heure** si on stocke du « local naïf » sans fuseau.

| Règle | Détail |
|---|---|
| Fuseau | `Europe/Paris` (déjà Imager). CET/CEST = le fuseau, pas un script à 2 h du matin. |
| Sync | `systemd-timesyncd` (ou chrony) · `timedatectl` UTC + NTP **yes**. |
| Stockage | **UTC** en base. Affichage Paris pour les tranches 00–08 / 08–16 / 16–24. |
| ESP | Pas d’horloge à croire. Payload = id + temp + hum. Le Pi tamponne. |
| Boot Pi | Attendre NTP (ou au moins le marquer `clock_unsynced`) avant d’écrire des moyennes d’heure. |

Vérif mercredi, 2 commandes : `timedatectl` · `date -u`.

**Iris MCP (`time-v1`) :** avis 18/08. WorldTimeAPI, fuseau `Europe/Paris`. Utile **une fois** depuis Cursor pour comparer avec le Pi. **Pas** la synchro 24/7 : le collecteur doit tourner sans Cursor, sans HTTP externe. Source de vérité = NTP du Pi (`systemd-timesyncd`).

## Inchangé (v1)

Jeudi 20/08 : vitrine IGEL, pas 14 jours de data. WoL / LLM hors semaine.

## Limites

- Mardi entamé tard : ESP-B peut glisser à mercredi.  
- Heartbeat 3 min : à calibrer au flash (timeout Wi-Fi).  
- Onduleur Eaton toujours KO : une coupure Pi = trou assumé.

## Ouverture v3

Si jeudi est trop juste après cette matinée : envoyer **quand même** 1 sonde + méthode Gamma, et le dire à IGEL (lab en cours, pas étude finie).
