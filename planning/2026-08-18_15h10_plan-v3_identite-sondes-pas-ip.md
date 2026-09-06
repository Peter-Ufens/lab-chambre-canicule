# Plan v3 — Identité des sondes (pas l’IP ESP)

**Date :** 2026-08-18 15h10 (question Peter, session Cursor)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** ACTIF  
**But :** figer que le collecteur **ne dépend pas** des IP `.26` / `.27`.

> **Anti-hallucination :** observé = ESP-A `.27` et ESP-B `.26` ce jour (DHCP box). Déduit = ces baux peuvent partir à une TV, un tel, un reboot. Inconnu = si box a des réservations DHCP (on n’en fait pas pour les ESP).

**Supplante :** v2 pour le calendrier semaine reste ACTIF. Ce v3 complète l’identité.

## Décision

| Qui | Comment on le trouve | Si l’IP bouge |
|---|---|---|
| ESP-A / ESP-B | **MAC** dans le JSON (`78:1C:3C:…`) | on s’en fiche |
| Collecteur (Pi) | hostname **`<hostname-pi>.home`** · repli `<IP-du-Pi>` | recompiler le repli, ou réserver le Pi sur la box plus tard |
| Moyennes | `n_samples` par MAC, pas par IP | idem |

L’ESP est **client HTTP** : il appelle le Pi. Le Pi n’a pas à « connaître » `.26`.

Si `.26` est pris par autre chose : l’ESP reçoit une **autre** IP, continue de POST.  
Si le Pi perd `.25` : là oui ça casse, jusqu’au nouveau repli. D’où le hostname en premier.

## Limites

- mDNS / DNS box : si `<hostname-pi>.home` échoue depuis l’ESP, on tombe sur le repli IP du **Pi**.  
- Réservation DHCP box pour le Pi : pas faite aujourd’hui.
