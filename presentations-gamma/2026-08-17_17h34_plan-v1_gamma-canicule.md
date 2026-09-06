# Plan v1 — Présentation Gamma canicule

**Date :** 2026-08-17 17h34 (horodatage message Peter, dictée Windows)  
**Auteur :** Karen (Cursor) pour Peter  
**Statut :** SUPPLANTÉ par v2 `planning/2026-08-19_06h32_plan-v2_gamma-canicule.md`  
**But :** caler le récit Gamma (grand public + FT) **avant** assemblage ESP.  
**19/08 :** Peter confirme : les **vrais chiffres** du lab (E1/E2, `n_samples`) **ne vont pas** dans Gamma. Plafond + clim connectée + lexique 2 pages : voir v2.

> **Anti-hallucination :** observé = dictées 17h34 + 17h40 (emboîtable, pas de soudure, YouTube + captures tout public sur le repo). Déduit = BTU/h rayon clim. Inconnu = visuels Gamma · DPE chambre.

Données / rétention : `planning/2026-08-17_17h22_plan-v1_donnees-canicule-retention.md` (1 min, 48 h brut, moyennes 2 semaines).

Repo public visé : `lab-chambre-canicule` (aujourd’hui **privé**, on ouvre plus tard, prompt **sans** secrets).

## Verdict Karen

**Oui, c’est cohérent.** Un fil clair : problème vécu (mauvaise clim, sonde mal placée) → méthode (2 capteurs mobiles, 2 semaines) → IA qui **dimensionne** → on n’achète pas une Ferrari pour aller à Lidl.  
Le datacenter n’est pas une divagation : c’est le **pourquoi tu es crédible** (admin sys, alertes temp, sonde déplacée). Ça parle à FT et au tout public si le lexique suit.

Trois gardes-fous pour que ça **tienne** :

1. L’IA recommande une **puissance / famille** (BTU/h, kW froid, mobile vs split), **pas** un SKU Leroy Merlin à 847 €. Sinon on survend.  
2. « 2 semaines » = les **moyennes** (heures + 3 tranches). Le brut minute ne reste que 48 h. Aligné avec le plan data.  
3. DPE A–E et m² : on les **demande** au prompt. Si inconnus (location), on le dit, on ne les invente pas.

## Trigrammes clim (lexique)

| Sigle | Usage dans le deck |
|---|---|
| **BTU/h** | Celui du rayon. C’est le bon trigramme grand public. |
| **kW froid** | Même chose, version « pro / fiche ». 1 kW ≈ 3412 BTU/h. |
| DPE A–G | Isolation du logement (tu as dit A B C E : on met A à G, on n’invente pas la lettre de ta chambre). |

Pas « BPU ». Frigories : une ligne lexique, pas le titre.

## Fil du deck (pages)

Ordre proposé. Titres de travail, pas encore Gamma.

1. **Titre** · Canicule, pas de clim, comment ne pas se tromper d’appareil.  
2. **Ça nous concerne** · malchanceux sans clim · actualité (chaleur), pas un hobby geek.  
3. **Le piège** · 25 m² vs 42 m² après déménagement · le web sans vendeur Leroy Merlin.  
4. **Citadine, pas Ferrari** · 1 image caricaturale · mon besoin ≠ moteur de sport.  
5. **D’où je parle** · admin sys, datacenter : les serveurs doivent rester au frais.  
6. **Anecdote sonde** · alerte température = souvent la **sonde a bougé**, pas la salle en feu. Même leçon à la maison.  
7. **Lexique express** · datacenter (une phrase). Le gros lexique = fin.  
8. **Le projet en une phrase** · mesurer la pièce, puis dimensionner.  
9. **2 capteurs, mobiles** · entrée + point le plus chaud. On **déménage** le kit.  
9b. **Ça s’emboîte** · **pas de soudure** · pas un kit « gros technicien » · clips, cordons, USB. Les tutos YouTube + **captures du lab** sont sur le repo, **tout public** (quand on ouvre).  
10. **2 semaines** · avant ou pendant canicule, si on peut.  
11. **L’IA (pas « LLM »)** · consigne simple · moyennes · m² · isolation si connue · période été.  
12. **Le prompt vit sur GitHub** (public, plus tard) · pas collé dans les slides · liste matériel aussi.  
13. **Résultat** · une clim **adaptée**, pas 600 / 900 / 1200 € au hasard.  
14. **Hors saison** · note amusante et utile : à Noël, cadeau à toi-même pour l’été suivant, tarif souvent plus doux, moins de rupture.  
15. **Lexique** · 2 pages (BTU/h, kW, DPE, datacenter, sonde, ESP, relevé, moyenne, split / mobile…).  
16. **Me joindre** · coordonnées · **autres labs** (Pi, WoL, etc., sans noyer).

## Accessible (slide 9b + repo)

Ce n’est **pas** de l’électronique à souder. Case Pi = clips. BME = Qwiic / Dupont. USB. Un amateur suit une vidéo.

Sur `lab-chambre-canicule` (déjà en `docs/captures/`, tutos à coller) :

- Captures Peter 17/08 : Imager, hostname, SSH, Connect (sanitisées, pas de mot de passe).  
- Liens YouTube **suivis** : case officielle `urzWrq4FySo` · dissipateur `I1-7vJMhkio` · Imager / flash ESP (fiche Parc `planning/liens-tutos-youtube-esp-pi-2026-08-17.md`).

Le deck Gamma **pointe** vers le repo. On ne recopie pas 12 minutes de vidéo dans Gamma.

## Lien avec le lab réel

| Slide | Chez nous |
|---|---|
| 2 capteurs | E1 entrée · E2 coin PC |
| 2 semaines | couches `hour` / `slice` / `day` |
| 48 h « zoom » | couche `raw` 1 min |
| Prompt public | fichier dans `lab-chambre-canicule` (quand le repo passe public) |
| Mobile | même ESP, autre pièce / autre appart |
| Accessible | emboîtable, pas de soudure · YouTube + captures repo |

## Hors slides (repo)

- Prompt générique **FR**, tout public, variables : CSV/moyennes, m², DPE si connu, ville.  
- BOM matériel.  
- Tutos YouTube + captures Imager/Connect (déjà dans `docs/captures/`).  
- Pas de Wi-Fi, pas d’adresse, pas de bail scanné.

## Limites

- Gamma pas encore ouvert : ceci est le **scénario**, pas les slides.  
- Repo encore privé : « public » = intention FT.  
- 2 semaines de vraie canicule : on n’a pas les données **aujourd’hui**. Le deck peut d’abord raconter la **méthode**, puis une MAJ avec chiffres.  
- L’anecdote datacenter : rester factuel (sonde déplacée), pas de nom d’employeur.

## Ouverture

GO assemblage ESP (un par un) quand Peter le dit.  
Slides Gamma = session dédiée (copie de ce fil + visuels).
