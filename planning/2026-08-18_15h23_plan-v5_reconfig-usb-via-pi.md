# Plan v5 — Reconfig USB via le Pi (complément portail)

**Date :** 2026-08-18 15h23 (idée Peter, session Cursor)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ACTIF (décision) · **pas encore codé**  
**But :** valider l’idée « ESP en USB sur le Pi, scripts qui reprennent le Wi-Fi du Pi ».

> **Anti-hallucination :** observé = alims Gotronic 5 V prévues pour E1/E2 · Pi actuel = **Wi-Fi**, Ethernet long **absent** cet appart. Déduit = USB Pi = mode **atelier**, pas 24/7 au mur. Inconnu = prochain logement (prise RJ45 ou non).

**Complète** le v4 (portail si l’ESP est déjà au mur, hors câble).

## Ce qui est juste

Deux scripts, c’est le bon découpage :

1. **Exporter** depuis le Pi : SSID / mot de passe **Wi-Fi 2,4 GHz** (et l’IPv4 du Pi) → fichier secrets (hors git).  
2. **Appliquer** : le firmware lit ces variables, puis **esptool** envoie le sketch **via le USB Gotronic branché sur le Pi**.

Dès que le Pi est sur le **nouveau** réseau et que l’ESP est **en USB dessus**, un `./flash-esp.sh` peut être quasi automatique. Pas besoin du PC NZXT.

## Nuances (sinon ça casse)

| Idée | Vrai si | Faux si |
|---|---|---|
| USB Gotronic Pi ↔ ESP | câble **data** (les nôtres le sont) | câble charge-only |
| Secrets = config du Pi | le Pi est **lui-même en Wi-Fi** (ou Wi-Fi + Ethernet) | le Pi est **Ethernet seul** : sa conf n’a **pas** le SSID/mot de passe dont l’ESP a besoin |
| Automatique après nouvelle box | les ESP sont **branchés USB au Pi** à ce moment-là | les ESP restent à E1/E2 sur **prise 5 V** : le script n’a pas de fil, il ne peut rien flasher |
| Ethernet sur le Pi | prochain logement / switch | **cet appart** : pas de câble long (décision 10/08) |

L’ESP reste un client **Wi-Fi 2,4 GHz**. Le Pi en Ethernet, ça le rend joignable pour SSH. Ça ne nourrit pas magiquement le SSID des sondes.

## Deux modes (on garde les deux)

| Mode | Quand | Quoi |
|---|---|---|
| **Atelier USB** (ton idée) | ESP sur le bureau / sur le Pi | scripts secrets + flash |
| **Mur / portail** (v4) | ESP déjà à l’entrée, sans USB | téléphone + BOOT |

24/7 : **alims 5 V Gotronic** aux emplacements. USB Pi = reconfig / flash, pas le courant de tous les jours (budget USB du Pi + longueur jusqu’à l’entrée).

## Décision (18/08)

- Idée **bonne**, à coder **après jeudi**.  
- Aujourd’hui : POST + collecteur, secrets encore tapés une fois sur le PC.  
- Plus tard : `scripts/export-wifi-from-pi.sh` + `scripts/flash-usb.sh`.  
- Si Pi Ethernet-only : le script 1 demandera le SSID 2,4 **à la main** (ou un 2ᵉ Wi-Fi sur le Pi).

## Limites

- Mot de passe Wi-Fi du Pi : lisible seulement s’il est stocké (NetworkManager). Sinon on le recolle une fois.  
- 2 ESP : un USB à la fois, ou 2 ports Pi, toujours **pas** USB + prise 5 V ensemble.
