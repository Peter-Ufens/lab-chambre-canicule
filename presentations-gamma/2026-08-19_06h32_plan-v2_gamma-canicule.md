# Plan v2 — Présentation Gamma canicule

**Date :** 2026-08-19 06h32 (horodatage message Peter)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** SUPPLANTÉ par v3 `planning/2026-08-19_06h37_plan-v3_gamma-canicule.md`  
**Supplante :** v1 `planning/2026-08-17_17h34_plan-v1_gamma-canicule.md` (le fil 1–13 reste, on ajoute plafond + clim connectée + lexique 2 pages mini).  
**But :** scénario Gamma **à coller** (grand public + FT). Pas les chiffres lab dans les slides.

> **Anti-hallucination :** observé = dictée 19/08 ~06h32 (plafond / Spider-Man, réponse taille humaine, clim connectée 2–3 slides, code Pi + GitHub, lexique 2 pages mini) + v1 17/08. Déduit = placement clim **après** 14–15 (même idée : adapté à chacun, puis automatisé). Inconnu = marque / protocole de la future clim (IR, Wi-Fi constructeur, etc.) · visuels Gamma (stock vs caricature).

Chiffres E1/E2 : **hors Gamma** (Peter 19/08). Repo visé : `lab-chambre-canicule` (encore privé, ouvrir sans secrets).

## Verdict Karen

Le gag plafond est le bon cousin de l’anecdote **sonde** (datacenter) : on mesure **où l’humain vit**, pas où c’est spectaculaire. La version sérieuse (pas un géant, solution pour chacun) évite de passer pour un sketch sans fond.

La clim connectée est un **bonus**, pas le cœur : le cœur reste dimensionner **avant** d’acheter. On ne vend pas une maison Domoticz. Mention `#maison connectée bricolée` une fois, sur la première slide bonus.

Code Pi : **intention**, pas encore écrit. Le jour J = achat clim. D’ici là : stub sur le Pi (consigne, seuil, mode nuit si dispo). Réglages live = commit GitHub. Le pont exact (télécommande IR, API Wi-Fi, etc.) se choisit **avec** l’appareil, on ne l’invente pas dans Gamma.

## Fil du deck (pages)

Ordre proposé. Titres de travail. **9b** reste 9b pour que **14 et 15** soient bien le plafond, comme demandé.

### Cœur (inchangé)

1. **Titre** · Canicule, pas de clim, comment ne pas se tromper d’appareil.  
2. **Ça nous concerne** · malchanceux sans clim · actualité (chaleur), pas un hobby geek.  
3. **Le piège** · 25 m² vs 42 m² après déménagement · le web sans vendeur Leroy Merlin.  
4. **Citadine, pas Ferrari** · 1 image caricaturale · mon besoin ≠ moteur de sport.  
5. **D’où je parle** · admin sys, datacenter : les serveurs doivent rester au frais.  
6. **Anecdote sonde** · alerte température = souvent la **sonde a bougé**, pas la salle en feu. Même leçon à la maison.  
7. **Lexique express** · datacenter (une phrase). Le gros lexique = fin.  
8. **Le projet en une phrase** · mesurer la pièce, puis dimensionner.  
9. **2 capteurs, mobiles** · entrée + point le plus chaud. On **déménage** le kit.  
9b. **Ça s’emboîte** · **pas de soudure** · clips, cordons, USB. Tutos YouTube + captures sur le repo.  
10. **2 semaines** · avant ou pendant canicule, si on peut.  
11. **L’IA (pas « LLM »)** · consigne simple · moyennes · m² · isolation si connue · période été.  
12. **Le prompt vit sur GitHub** · pas collé dans les slides · liste matériel aussi.  
13. **Résultat** · une clim **adaptée**, pas 600 / 900 / 1200 € au hasard.

### 14–15 · Question bête (hauteur humaine)

14. **Pourquoi ne pas mettre un capteur au plafond ?**  
    Image : Spider-Man (caricature / pose grimpeur, **pas** une capture de film Marvel).  
    Texte : **Parce que je ne suis pas spider-man voyons !!!**

15. **Réponse sérieuse**  
    Texte : **Je n’ai pas mis de capteur au plafond car je ne suis pas un géant (personne de grande taille) donc je préfère proposer une solution adaptée pour chacun :)**  
    Images : **deux**, côte à côte.  
    - personne de grande taille (type basketteur)  
    - personne de taille moyenne  
    Idée visuelle : le capteur à hauteur de vie, pas au plafond. Tout le monde peut le poser / le déplacer.

### 16–18 · Bonus clim connectée (2–3 slides)

Placées **ici** : après « adapté à chacun », avant « quand acheter ». Ce n’est pas obligatoire pour suivre le deck. Mention **#maison connectée bricolée** sur la 16.

16. **Clim déjà connectée ?**  
    On peut la relier au Raspberry : le système **démarre tout seul** quand une température trop chaude est atteinte.

17. **Consigne + mode nuit**  
    Configurable **depuis le Raspberry** : on indique la température souhaitée, envoyée au climatiseur, la température idéale est maintenue. Quand la nuit arrive, le **mode nuit** du climatiseur (s’il en dispose) se met en place tout seul.

18. **Les capteurs veillent + le code**  
    Les capteurs surveillent qu’il n’y ait pas d’écart de température.  
    Le code est **préparé sur notre Raspberry**, prêt pour le **jour J** (achat de *ma* clim).  
    Réglages en live : on adapte, on **met à jour sur GitHub**.  
    (Si le temps presse : fusionner 17+18 en une slide.)

### Clôture

19. **Hors saison** · à Noël, cadeau à toi-même pour l’été suivant, tarif souvent plus doux, moins de rupture.  
20. **Lexique 1** · clim et énergie (voir liste).  
21. **Lexique 2** · lab, mesures, maison connectée (voir liste). **Minimum 2 pages.** Si ça déborde, page 21b.  
22. **Me joindre** · coordonnées · autres labs (Pi, WoL) sans noyer.

## Lexique (2 pages minimum)

À couvrir, sans tout mettre en gras d’un coup. Page 20 = grand public clim. Page 21 = lab + bonus.

**Page 20 (clim / logement)**  
BTU/h · kW froid (1 kW ≈ 3412 BTU/h) · frigories (une ligne) · DPE A–G · split / mobile · consigne · mode nuit · clim connectée · seuil « trop chaud ».

**Page 21 (lab / récit)**  
Datacenter · sonde · ESP · Raspberry Pi · relevé · moyenne (heure / tranche / jour) · brut 48 h · emboîtable / pas de soudure · GitHub · écart de température · #maison connectée bricolée (bricolée = on assemble, on n’achète pas une box magique).

Pas « BPU ». Pas « LLM » comme titre (l’IA, point).

## Visuels 14–15

| Slide | Image | Note |
|---|---|---|
| 14 | Spider-Man au plafond | Caricature ou stock « super-héros grimpeur ». Pas un extrait Marvel (FT / droits). |
| 15 | Basketteur (grand) + personne taille moyenne | Même cadre, deux silhouettes. Capteur à hauteur d’humain, pas au plafond. |

Ferrari / citadine (slide 4) inchangée.

## Code Pi (hors slides, lab réel)

Pas dans Gamma au-delà de la phrase « prêt sur le Raspberry, MAJ GitHub ».

| | |
|---|---|
| Où | `lab-chambre-canicule` (service sur `<hostname-pi>`) |
| Quoi | Seuil trop chaud → ordre clim ON · consigne °C · bascule mode nuit (si la machine l’a) · les ESP déjà en place donnent l’écart |
| Quand | Stub **avant** l’achat, pour ne pas improviser le jour J |
| Inconnu | Protocole de **cette** clim (IR, Wi-Fi marque, etc.) : se branche le jour de l’unbox |
| Live | Réglage → commit GitHub → pull / redéployer sur le Pi |

On n’annonce pas une marque. On n’invente pas une API.

## Gardes-fous (repris + un)

1. L’IA recommande une **puissance / famille**, pas un SKU magasin.  
2. « 2 semaines » = moyennes. Brut minute = 48 h, pas le récit.  
3. DPE et m² : demandés, jamais inventés.  
4. Clim connectée = **bonus**. Ça ne remplace pas le dimensionnement. Pas de chiffres E1/E2 dans les slides.  
5. Anecdote datacenter : sonde déplacée, **pas** de nom d’employeur.

## Lien lab ↔ slides

| Slide | Chez nous |
|---|---|
| 9 | E1 entrée · E2 coin PC (hauteur de vie, pas plafond) |
| 14–15 | Pourquoi on n’a **pas** collé au plafond |
| 16–18 | Collecteur Pi déjà là · **pont clim** = à écrire / stub |
| 12, 18 | Repo public plus tard, sans secrets |

## Limites

- Gamma pas encore ouvert : scénario, pas les slides collées.  
- Repo encore privé.  
- Stub clim : **pas** commencé au moment de ce plan.  
- 2 semaines de canicule : toujours pas dans le deck (méthode seulement).

## Ouverture

Coller dans Gamma = session dédiée (ce fil + visuels 14–15 + bonus 16–18).  
Stub clim Pi : **après** le deck, ou le soir si l’énergie reste. Pas empilé sur l’envoi IGEL.
