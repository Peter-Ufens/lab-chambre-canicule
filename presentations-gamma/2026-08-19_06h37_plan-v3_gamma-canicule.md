# Plan v3 — Présentation Gamma canicule

**Date :** 2026-08-19 06h37 (horodatage message Peter)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** SUPPLANTÉ par v4 `planning/2026-08-19_06h48_plan-v4_gamma-canicule.md` (9b = slide 10, tout décale)  
**Supplante :** v2 `planning/2026-08-19_06h32_plan-v2_gamma-canicule.md`  
**But :** scénario Gamma **à coller** (grand public + FT). Pas les chiffres lab dans les slides.

> **Anti-hallucination :** observé = dictée 19/08 ~06h37 (nouvelle slide avant hors saison : clim connectée ↔ background admin sys, sonde datacenter, deux images temp idéale DC / maison) + v2 06h32 + v1 17/08. Déduit = callback des slides 5–6, pas un doublon (5–6 = alerte / sonde bougée ; 19 = confort maintenu, chez soi comme les serveurs). Inconnu = visuels stock (salle serveurs + salon, thermomètre « idéal » sans chiffre lab).

Chiffres E1/E2 : **hors Gamma**. Repo visé : `lab-chambre-canicule` (encore privé, ouvrir sans secrets).

## Verdict Karen

La 19 **referme** le récit : on a ouvert avec le datacenter (crédibilité), on finit le bonus clim en disant que le chez-soi a **la même exigence** que les serveurs : une température idéale, avec une sonde qui veille. Ce n’est pas « je copie mon job », c’est « le confort humain mérite le même soin que la machine ».

Pas de nom d’employeur. Pas de °C du lab sur les images (pictogrammes / salles calmes, pas nos 25,9 °C).

## Fil du deck (pages)

**9b** reste 9b. **14 et 15** restent le plafond.

### Cœur (1–13) · inchangé

1. Titre · 2. Ça nous concerne · 3. Le piège · 4. Citadine, pas Ferrari  
5. D’où je parle · 6. Anecdote sonde · 7. Lexique express  
8. Le projet · 9. 2 capteurs · 9b. Ça s’emboîte  
10. 2 semaines · 11. L’IA · 12. Prompt GitHub · 13. Résultat  

### 14–15 · Hauteur humaine (inchangé)

14. Pourquoi ne pas mettre un capteur au plafond ? · Spider-Man · *Parce que je ne suis pas spider-man voyons !!!*  
15. Réponse sérieuse · pas un géant · solution adaptée pour chacun · basketteur + taille moyenne  

### 16–18 · Bonus clim connectée (inchangé)

16. Trop chaud → le Raspberry démarre tout seul. `#maison connectée bricolée`  
17. Consigne + mode nuit (s’il existe)  
18. Capteurs veillent · code prêt sur le Pi pour le jour J · MAJ GitHub  

### 19 · Boucle datacenter / maison (NOUVEAU)

**Avant** hors saison.

**Idée :** avoir une clim connectée et fonctionnelle **ramène** au background admin système. Dans le datacenter, la sonde température était là. Ici, le chez-soi est en température idéale **comme** les serveurs informatiques.

**Visuel :** deux images côte à côte.  
- température idéale **en datacenter** (salle serveurs, calme, pas une alarme rouge)  
- température idéale **à la maison** (pièce de vie, même idée de « ça va »)

**Lien avec 5–6 :** là on expliquait l’alerte (souvent la sonde a bougé). Ici on montre le **but** : un confort tenu, pas un incident. On ne répète pas l’anecdote mot pour mot.

### Clôture (décalée)

20. **Hors saison** · à Noël, cadeau à toi-même pour l’été suivant.  
21. **Lexique 1** · clim et énergie.  
22. **Lexique 2** · lab, mesures, maison connectée. **Minimum 2 pages.** Si ça déborde, 22b.  
23. **Me joindre** · coordonnées · autres labs sans noyer.

## Lexique (2 pages minimum)

**Page 21 (clim / logement)**  
BTU/h · kW froid (1 kW ≈ 3412 BTU/h) · frigories (une ligne) · DPE A–G · split / mobile · consigne · mode nuit · clim connectée · seuil « trop chaud ».

**Page 22 (lab / récit)**  
Datacenter · sonde · ESP · Raspberry Pi · relevé · moyenne · brut 48 h · emboîtable · GitHub · écart de température · #maison connectée bricolée.

Pas « BPU ». Pas « LLM » comme titre.

## Visuels (14–15 et 19)

| Slide | Images | Note |
|---|---|---|
| 14 | Spider-Man au plafond | Caricature / grimpeur. Pas un extrait Marvel. |
| 15 | Basketteur + taille moyenne | Capteur à hauteur d’humain. |
| 19 | Datacenter « idéal » + maison « idéale » | Même lecture (confort tenu). Pas nos chiffres. Pas de logo employeur. |

## Code Pi · gardes-fous · lab

Inchangés vs v2 : stub jour J, pas de marque, pas de SKU, pas de chiffres lab, pas de nom d’employeur.

Slide 19 = **récit**, pas une spec technique de plus.

## Ouverture

Prompts Gamma (3 lots, max 10) : `planning/2026-08-19_06h44_prompts-gamma-canicule-3-lots.md`.  
Stub clim Pi : après le deck, pas empilé sur l’envoi IGEL.
