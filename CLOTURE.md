# Clôture — lab-chambre-canicule

| | |
|---|---|
| **Date clôture** | 2026-09-06 |
| **Statut INDEX** | **`cloture`** (exploitation collecte **continue** · reprise ops après fibre rue ~**16/09/2026** + GO Peter) |
| **Décideur** | Peter UFENS |
| **GitHub privé (ops)** | https://github.com/Peter-Ufens/lab-chambre-canicule-private · remote `origin` |
| **GitHub public (vitrine)** | https://github.com/Peter-Ufens/lab-chambre-canicule · remote `public` |
| **Gamma (04c)** | https://gamma.app/docs/Canicule-pas-de-clim-comment-ne-pas-se-tromper-dappareil-0y21j1gd58cd990 |

Voir [`REPOS.md`](REPOS.md). **≠ lab-wol.**

## Pourquoi on clôture (pas abandon)

- Fibre Orange encore HS · rétablissement rue estimé **~16/09** (appel 05/09).
- **Pas** de check LAN / retouche Wi-Fi Pi tant que la fibre n’est pas revenue **et stable** (évite de changer les paramètres Wi-Fi du Pi pendant la panne).
- Vitrine FT / Gamma / repo public déjà livrés (19/08).
- Plans ops + Gamma **canon ici** (moves 06/09 depuis hub-materiel).
- Karen / Cursor : **pas de travail actif** ici avant reprise ou **GO Peter**.

## Ce qui est livré (capital)

| Bloc | État |
|---|---|
| Pi + collecteur HTTP `:8080` + SQLite | **OK** · collecte continue |
| ESP-A (E1) + ESP-B (E2) POST 1/min (id = MAC) | **OK** · exploitation |
| Watchdog Wi-Fi Pi | **OK** · installé |
| clim-controller stub (`enabled=false`) | **OK** · prêt jour J |
| Prompt dimensionnement + BOM + tutos | **OK** · `docs/` |
| Plans ops mesure | **OK** · `planning/` (12) |
| Gamma 04c + plans/prompts | **OK** · `presentations-gamma/` (7) |
| Graphify | **OK** 06/09 · out `Vault-Obsidian/graphify-out/lab-chambre-canicule` |
| Repo public + captures Imager/Connect | **OK** |

## Suite au dégel (ordre Peter · 06/09)

1. **Fibre revenue + stable** (~16/09 confirmé) · **ne pas** modifier Wi-Fi Pi d’ici là.
2. **Check LAN / relevés complets** : agrégats depuis **19/08** jusqu’au **jour de résolution fibre** (cas réel panne · ajuster retention / watchdog / export si besoin). Pas seulement la fenêtre courte 20–26/08.
3. **Kingston XS2000** : configurer et brancher **directement** sur le Pi (après checks).
4. **Mini-LLM Pi** : **pas ici** · prévu dans **`lab-wol`** (diag réseau faible).
5. Export mesures + prompt clim (jour J) quand Peter veut dimensionner · achat clim côté `Canicule` ~02/2027.

## Interdits pendant la clôture

- Check LAN / reconfig Wi-Fi ESP ou Pi « pour la panne »
- Brancher Kingston avant GO post-fibre
- Ajouter mini-LLM dans ce repo (territoire **lab-wol**)
- Committer `graphify-out/` · secrets (`secrets.h`, `clim_config.json`, `.env`)
- Pousser un secret sur le remote **`public`** (vitrine)

## Liens

| Sujet | Où |
|---|---|
| Matos Pi | `hub-materiel` |
| Frère WoL + mini-LLM | `lab-wol` |
| Achat clim archive | `Canicule` |
| Vault | `02-Projets/lab-chambre-canicule.md` |
| INDEX | `<workspace>\INDEX.md` |
| Redirection A-traiter checks | `A-traiter/entree/redirections/2026-08-26-evac-lab-canicule-checks-panne.md` |
