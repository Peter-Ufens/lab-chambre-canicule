# Prompts Gamma canicule — 3 lots v2 (max 10 cartes)

**Date :** 2026-08-19 07h08  
**Auteur :** Karen (Cursor) pour Peter  
**Plan source :** `planning/2026-08-19_06h48_plan-v4_gamma-canicule.md`  
**Statut :** ACTIF · supplante `planning/2026-08-19_06h48_prompts-gamma-canicule-3-lots.md`

**Changements v2 (Peter ~07h08) :**
- **Aucun tiret cadratin** (`—`) dans le texte des cartes.
- Admin système = **expérience passée**. Aujourd’hui Peter **vise l’IA**, pas un retour admin sys.
- Carte 24 : portrait = **même image que GitHub** (`peter-ufens-avatar-github-2026-04.jpeg`).

**Avatar canon (Peter, sur ton PC) :**
`<workspace>\Obsidian\vault\00-Meta\profil-peter\media\peter-ufens-avatar-github-2026-04.jpeg`  
Copies : `<workspace>\Suivi-Pro\pieces\images\` · Bureau `Importants\CV\` · fiche vault `Avatar-visuel-Peter.md`

---

## PROMPT CORRECTION (deck déjà généré)

Si le Gamma existe déjà, coller **ce bloc seul** dans Gamma (mode édition / régénérer texte) :

```
Révise le texte de TOUTES les cartes de cette présentation. Ne change pas la structure (24 cartes). Ne régénère pas les visuels sauf la carte 24.

1) STYLE : supprime TOUS les tirets cadratin (—). Utilise virgules, points, deux-points ou parenthèses. Français naturel, pas de style traduction anglaise.

2) ADMIN SYSTÈME vs IA : je ne suis PAS admin système aujourd’hui. J’ai été admin système (datacenter). Aujourd’hui je vise l’IA. Quand je parle du datacenter ou des sondes, c’est mon EXPÉRIENCE PASSÉE qui rend la méthode crédible. Ce n’est pas une candidature pour rester admin sys.

Cartes à corriger en priorité :
- Carte 5 « D’où je parle » : j’ai été admin système… aujourd’hui je m’oriente vers l’IA…
- Carte 20 « Même exigence qu’au datacenter » : mon expérience d’admin système (passé), pas « mon métier actuel »
- Carte 24 « Me joindre » : ligne d’accroche = orientation IA · expérience admin sys en arrière-plan · lab canicule

3) Carte 24 portrait : utilise la photo de profil GitHub de Peter Ufens (même illustration que github.com/Peter-Ufens). L’utilisateur uploadera le fichier local si Gamma le demande.

Garde l’humour (Spider-Man carte 15), le hashtag #maison connectée bricolée, les interdits (pas de chiffres lab, pas d’adresse, pas de nom d’employeur).
```

---

## LOT 1 — slides 1 à 10

```
Crée une présentation Gamma en FRANÇAIS, exactement 10 cartes, pas une de plus.

Public : grand public + conseiller France Travail. Ton : clair, humain, un peu d’humour, jamais corporate, jamais « LLM », jamais « BPU ».
Auteur : Peter Ufens. J’ai été admin système (datacenter). Aujourd’hui je vise l’IA : ce deck parle de mon expérience passée, pas d’un projet pour rester admin sys. Pas de nom d’employeur.
Sujet : canicule, pas de clim, comment choisir un appareil adapté grâce à 2 capteurs et un Raspberry, puis éventuellement piloter une clim connectée.

Interdits :
- aucun tiret cadratin (—) : virgules, points, deux-points ou parenthèses seulement
- aucun chiffre de relevé réel (pas de °C de chambre, pas de RSSI, pas de n_samples)
- aucun mot de passe, aucune adresse, aucun SKU magasin, aucun prix « 847 € »
- pas d’extrait de film Marvel (Spider-Man seulement au lot 2)
- pas de logo d’entreprise
- ne pas présenter Peter comme admin système AUJOURD’HUI

Style visuel : propre, chaleureux, photos ou illustrations simples, pas cyberpunk, pas de slides trop chargées.

CARTE 1 — Titre
Titre : Canicule, pas de clim : comment ne pas se tromper d’appareil
Sous-titre : Mesurer d’abord, dimensionner ensuite. Une méthode simple, à la maison.
Visuel : canicule / ville en été, pas un data center.

CARTE 2 — Ça nous concerne
Texte : Ça touche les malchanceux qui n’ont pas la clim. Ce n’est pas un hobby geek. C’est l’actualité chaleur, et un logement qu’il faut rendre vivable.
Visuel : quotidien (appart, ventilateur, fenêtre), pas un labo.

CARTE 3 — Le piège
Titre : Le piège des m²
Texte : Un appart de 25 m² puis un autre de 42 m², ce n’est pas le même besoin. Sur le web, sans vendeur en rayon, on achète trop petit ou trop gros.
Visuel : deux pièces de tailles différentes, ou un mètre / plan simple.

CARTE 4 — Citadine, pas Ferrari
Titre : Une citadine, pas une Ferrari
Texte : Mon besoin n’est pas un moteur de sport. On n’achète pas une Ferrari pour aller à Lidl. Même idée pour la clim : la puissance juste, pas le prestige.
Visuel : UNE image caricaturale citadine vs Ferrari (illustration, pas une pub de marque).

CARTE 5 — D’où je parle
Titre : D’où je parle
Texte : J’ai été admin système. Dans un datacenter, les serveurs doivent rester au frais et on surveille la température. Aujourd’hui je vise l’IA : je parle ici de cette expérience passée, pas d’un métier que je souhaite garder. Elle m’aide à expliquer pourquoi mesurer avant d’acheter une clim.
Visuel : salle serveurs calme (pas d’alarme rouge, pas de logo entreprise).

CARTE 6 — Anecdote sonde
Titre : Quand la sonde a bougé
Texte : Une alerte température, ce n’est pas toujours la salle en feu. Souvent, la sonde a simplement bougé. Même leçon à la maison : on mesure au bon endroit, sinon on se trompe d’appareil.
Visuel : capteur / sonde déplacée, pas un incendie.

CARTE 7 — Lexique express
Titre : Datacenter, en une phrase
Texte : Un datacenter, c’est un lieu où des serveurs tournent 24 h/24 : on les garde au frais, on surveille, on répare. Le gros lexique (BTU/h, DPE, consigne…) arrive à la fin.
Visuel : pictogramme simple (bâtiment + thermomètre), peu de texte autour.

CARTE 8 — Le projet en une phrase
Titre : Le projet, en une phrase
Texte : Mesurer la pièce avec 2 capteurs, puis dimensionner une clim adaptée. L’IA aide à choisir une FAMILLE d’appareil (puissance), pas un modèle magasin.
Visuel : 2 petits capteurs + une pièce, schéma simple.

CARTE 9 — 2 capteurs, mobiles
Titre : 2 capteurs, et on les déménage
Texte : Un à l’entrée (souvent plus frais), un au point le plus chaud (souvent le coin PC). Le kit est mobile : autre pièce, autre logement, on recommence la mesure.
Visuel : deux points dans une pièce (entrée + zone chaude), hauteur d’humain, PAS au plafond.

CARTE 10 — Ça s’emboîte
Titre : Ça s’emboîte. Pas de soudure.
Texte : Ce n’est pas un kit « gros technicien ». Clips, cordons, USB. Un amateur suit une vidéo. Les tutos YouTube et les captures sont sur GitHub, tout public.
Visuel : clips / cordons / USB, ambiance bricolage accessible, pas un fer à souder.

Termine après ces 10 cartes. N’ajoute pas de lexique long, pas de clim connectée, pas de GitHub détaillé (juste l’allusion tutos).
```

---

## LOT 2 — slides 11 à 20

```
SUITE d’une présentation Gamma déjà commencée (lot 1 = cartes 1 à 10).
Langue : FRANÇAIS. Ajoute EXACTEMENT 10 cartes nouvelles, numérotées 11 à 20. Pas une de plus. Ne régénère pas les cartes 1 à 10. Même ton : clair, humain, un peu d’humour, pas corporate.

Rappel auteur : Peter a été admin système, aujourd’hui il vise l’IA. Le datacenter = expérience passée, pas métier visé.

Interdits :
- aucun tiret cadratin (—)
- aucun chiffre de relevé réel
- aucun SKU, aucun nom d’employeur, aucune adresse
- pas d’extrait de film Marvel (Spider-Man = caricature / super-héros grimpeur générique)
- ne pas dire que Peter est admin système aujourd’hui

CARTE 11 — 2 semaines
Titre : 2 semaines, si on peut
Texte : On mesure avant ou pendant la canicule. Ce qui compte, ce sont les MOYENNES (heure, journée, matin / après-midi / soir), pas chaque minute. Assez pour dimensionner, pas un rapport de labo.

CARTE 12 — L’IA
Titre : L’IA dimensionne (pas un oracle magasin)
Texte : Une consigne simple : on lui donne les moyennes, les m², l’isolation si on la connaît (DPE), la période été. Elle propose une puissance / une famille (mobile ou split), pas « achetez le modèle X à 847 € ». Si le DPE est inconnu (location), on le dit, on n’invente pas.

CARTE 13 — Le prompt vit sur GitHub
Titre : Le prompt vit sur GitHub
Texte : Le texte pour l’IA n’est pas collé dans ces slides. Il est sur GitHub, public, avec la liste du matériel. Ici on raconte la méthode. Là-bas on copie-colle et on l’adapte à son logement.
Visuel : logo GitHub générique / ordi, pas de capture d’écran de code secret.

CARTE 14 — Résultat
Titre : Une clim adaptée
Texte : Le résultat, c’est la bonne famille d’appareil : assez forte, pas trop. Pas 600, 900 ou 1200 € au hasard. Citadine, pas Ferrari.

CARTE 15 — Question bête, plafond
Titre : Pourquoi ne pas mettre un capteur au plafond ?
Texte EXACT (gros, humour) : Parce que je ne suis pas spider-man voyons !!!
Visuel : caricature d’un super-héros grimpeur au plafond (pas une capture de film, pas de logo Marvel). Une seule blague, elle porte la carte.

CARTE 16 — Réponse sérieuse
Titre : Une solution à hauteur d’humain
Texte EXACT : Je n’ai pas mis de capteur au plafond car je ne suis pas un géant (personne de grande taille) donc je préfère proposer une solution adaptée pour chacun :)
Visuel OBLIGATOIRE : DEUX images côte à côte. 1) personne de grande taille type basketteur. 2) personne de taille moyenne. L’idée : le capteur se pose et se déplace sans échelle, pour tout le monde.

CARTE 17 — Clim connectée ?
Titre : Et si la clim est déjà connectée ?
Texte : On peut la relier à un Raspberry Pi. Quand il fait trop chaud, le système peut démarrer tout seul.
Hashtag visible une fois : #maison connectée bricolée
Visuel : clim + petit ordinateur type Raspberry, bricolage, pas une box domotique de luxe.

CARTE 18 — Consigne + mode nuit
Titre : Consigne, et mode nuit
Texte : On indique sur le Raspberry la température souhaitée : elle est envoyée au climatiseur, la température idéale se maintient. Quand la nuit arrive, le mode nuit du climatiseur (s’il en dispose) se met en place tout seul.

CARTE 19 — Les capteurs veillent + le code
Titre : Les capteurs veillent. Le code est prêt.
Texte : Les capteurs surveillent qu’il n’y ait pas d’écart de température. Le code est préparé sur notre Raspberry, prêt pour le jour J (quand j’achète ma clim). Un réglage en live : on met à jour sur GitHub, puis sur le Pi. On n’invente pas la marque ni la télécommande dans ces slides.

CARTE 20 — Boucle datacenter / maison
Titre : Même exigence qu’au datacenter
Texte : Une clim connectée et fonctionnelle, ça ramène à mon expérience d’admin système (passé). Au datacenter, la sonde température veillait sur les serveurs. Chez soi, on vise la même idée : une température idéale, comme pour nos machines. Le confort humain mérite le même soin. Ce n’est pas un retour vers le métier d’admin, c’est la même rigueur appliquée à la maison.
Visuel OBLIGATOIRE : DEUX images côte à côte. 1) datacenter calme, température « ça va » (pas d’alarme, pas de logo entreprise). 2) pièce de vie à la maison, même impression de confort tenu. Aucun chiffre °C réel.

Termine après la carte 20. Pas de lexique encore, pas de « hors saison », pas de page contact.
```

---

## LOT 3 — slides 21 à 24

```
FIN de la présentation Gamma (cartes 1 à 20 déjà là).
Langue : FRANÇAIS. Ajoute EXACTEMENT 4 cartes, numérotées 21 à 24. Pas une 5e. Même ton. Ne régénère pas le début.

Interdits : pas de tirets cadratin (—), pas de chiffres de relevé, pas d’adresse, pas de nom d’employeur, pas « LLM » comme titre, pas « BPU ». Peter vise l’IA aujourd’hui, pas un poste admin sys.

CARTE 21 — Hors saison
Titre : Hors saison, cadeau à soi
Texte : Note utile (et un peu amusante) : à Noël, on peut s’offrir la clim pour l’été suivant. Souvent moins cher, moins de rupture. On dimensionne maintenant, on achète au bon moment.

CARTE 22 — Lexique 1 · clim et logement
Titre : Lexique (1/2) : la clim
Présente ces termes, définitions COURTES, français simple, pas un dictionnaire d’ingénieur, pas de tirets cadratin :
- BTU/h : l’unité du rayon, la puissance de froid grand public
- kW froid : la même chose, version fiche technique (1 kW ≈ 3412 BTU/h)
- Frigories : une ligne seulement, on n’en fait pas un titre
- DPE A à G : isolation du logement ; si on ne la connaît pas, on ne l’invente pas
- Split / mobile : fixé au mur vs appareil qu’on déplace
- Consigne : la température qu’on demande à la clim
- Mode nuit : programme plus silencieux / plus doux, s’il existe
- Clim connectée : on peut la piloter (app, ou un Raspberry)
- Seuil « trop chaud » : au-delà, on démarre

CARTE 23 — Lexique 2 · lab et récit
Titre : Lexique (2/2) : le petit lab
Définitions COURTES, pas de tirets cadratin :
- Datacenter : lieu des serveurs, à garder au frais
- Sonde : capteur de température (mal placée = fausse alerte)
- ESP : petit module Wi-Fi + capteur, emboîtable, pas de soudure
- Raspberry Pi : petit ordinateur qui recueille les mesures et, plus tard, peut parler à la clim
- Relevé / moyenne : une mesure vs le résumé sur une heure, une tranche, un jour
- Brut 48 h : on garde le détail seulement 2 jours, le récit ce sont les moyennes
- GitHub : où vivent le prompt, la liste matériel, les tutos
- Écart de température : différence entre deux points de la pièce (entrée vs coin chaud)
- Maison connectée bricolée : on assemble soi-même, on n’achète pas une box magique

CARTE 24 — Me joindre
Titre : Me joindre
Texte :
Peter Ufens
Orientation IA · expérience admin système (datacenter) · lab maison (capteurs, Raspberry, méthode canicule)
GitHub : https://github.com/Peter-Ufens
Site : https://peter-ufens.dev
LinkedIn : https://www.linkedin.com/in/peter-ufens/
Une ligne : d’autres labs (réveil PC, Raspberry) existent, sans tout détailler ici.
Visuel OBLIGATOIRE : portrait Peter Ufens, la MÊME illustration que sa photo de profil GitHub (avatar github.com/Peter-Ufens). Même image, mêmes liens. L’utilisateur uploadera le fichier `peter-ufens-avatar-github-2026-04.jpeg` si Gamma le demande. Pas de photo d’appartement, pas d’adresse.

Fin du deck. N’ajoute pas de slide « merci » ni de QR inventé.
```
