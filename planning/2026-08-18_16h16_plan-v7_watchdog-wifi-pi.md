# Plan v7 — Watchdog Wi-Fi Pi (répéteur vs box)

**Date :** 2026-08-18 16h16 (incident Peter, session Cursor)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ACTIF  
**But :** le Pi se recale tout seul si le répéteur d’entrée a sauté, sans attendre un débranchement 27 W.

> **Anti-hallucination :** observé = prise triple entrée · répéteur en amont · Pi injoignable · power-cycle 27 W → Connect OK. Peter : répéteur parfois à recycler (débrancher/rebrancher) · coupures immeuble · resynchro box/répéteur après le courant · déjà un répéteur neuf, distance chambre–box = la contrainte · **pas** de nouveau matos. Déduit = watchdog Pi = retry client, ça ne répare pas un répéteur figé. Inconnu = délai exact de resynchro après EDF.

## Cause

Pas un bug ESP. La prise **entrée** alimente le **répéteur**. Brancher la triple / l’ESP a coupé ou bougé cette alim. Le Pi (fond d’appart) ne voyait plus le Wi-Fi.

## Deux couches

| Couche | Quoi |
|---|---|
| **Prise** | Répéteur = **ne pas débrancher**. ESP-A sur une autre fiche de la triple, sans jamais ôter le répéteur. |
| **Script** | Toutes les 60 s : ping passerelle. Si mort : `nmcli` reconnect `wlan0` (même SSID `REMPLACE_SSID_2_4GHZ` : box **ou** répéteur). **Pas** de reboot. |

Le script ne « choisit » pas box vs répéteur : c’est le même SSID. Le chip se réassocie à celui qui répond.

Les ESP ont déjà un retry Wi-Fi dans le firmware (POST). Le trou de ce soir = le **Pi**.

## Limites

- Si box **et** répéteur sont éteints : rien à joindre.  
- Reconnect ~3–5 s : quelques POST ESP ratés, puis ça reprend (id MAC).  
- Répéteur **figé** : Peter continue le débrancher/rebrancher du répéteur. Le script ne le réveille pas. Il évite surtout de devoir **débrancher le Pi**.  
- Après coupure immeuble : le Pi reboote avec le 27 W, le timer reprend à 90 s, le répéteur peut mettre 1–2 min à se recaler sur la box.
