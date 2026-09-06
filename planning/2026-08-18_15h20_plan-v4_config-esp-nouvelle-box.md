# Plan v4 — Config ESP durable (nouvelle box)

**Date :** 2026-08-18 15h20 (question Peter, session Cursor)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ACTIF (décision) · **pas encore codé**  
**But :** dire si le collecteur peut reconfigurer les ESP, et quoi faire pour que ce soit durable.

> **Anti-hallucination :** observé = firmware actuel = SSID + mot de passe + IP du Pi **dans le flash** (`secrets.h`). Déduit = hors Wi-Fi, le Pi n’a aucun canal vers l’ESP. Inconnu = date d’un futur changement de box / déménagement.

**Complète** le v3 (identité MAC, pas IP ESP). Ne remplace pas le collecteur déjà allumé.

## Réponse courte

**Non.** Le collecteur **ne peut pas** reconfigurer un ESP si la box a changé. L’ESP est hors réseau : le Pi n’a rien à qui parler.

Ce qui **marche sans USB** plus tard : l’ESP ouvre lui-même un petit Wi-Fi « config » (téléphone, 2 minutes). Portail captif. Identifiants en NVS, pas dans le sketch.

## Cas

| Changement | Collecteur peut pousser ? | Geste durable |
|---|---|---|
| IP DHCP de l’ESP | inutile (id = MAC) | rien |
| IP du **Pi**, même box | non (ESP tape encore `.25`) | mDNS ou bouton config |
| SSID / mot de passe box | **non** | portail config (ou USB + `secrets.h`) |
| Déménagement / nouvelle box | **non** | portail config |

USB + `secrets.h` = plan B (aujourd’hui). Correct pour jeudi.

## Décision (18/08)

1. **Aujourd’hui** : POST vers le Pi.  
2. **Après jeudi** : portail + nom du Pi. BOOT long = nouvelle box.  
3. Complément USB/Pi : voir **v5**.

## Limites

- Portail = 1–2 flashes de plus, une fois.  
- SSID de config visible près de l’ESP : local, normal.
