# Consignes Graphify — lab-chambre-canicule

**Workspace :** ce projet (`<workspace>\lab-chambre-canicule`)  
**Canon ops :** `<workspace>\Vault-Obsidian\planning\BRIEF-AGENT-GRAPHIFY-PARC-SUIVI-2026-09-05.md`  
**Statut local :** `OK` · run **2026-09-06** (déterministe · sans LLM · sans HTML)  
**Projet :** `stable` · collecte continue · vitrine FT clôturée 19/08 · Graphify = cartographie lecture seule  

## Pour l’agent (ordre)

1. Lire **ce fichier** + le brief canon.  
2. Confirmer **GO Peter**.  
3. Lancer Graphify **pour ce repo** (workspace lab-chambre-canicule OK).  
4. Modèle : **`graphifyy`** · sans LLM · sans HTML · venv partagé Vault-Obsidian.  
5. Sortie : `<workspace>\Vault-Obsidian\graphify-out\lab-chambre-canicule`  
6. Audit `graph.json` (0 hit PERSONNES / credentials / Zone A).  
7. MAJ **Statut local** ci-dessous.  
8. **Append** une ligne au **Journal des runs** du brief canon Vault-Obsidian  
   `planning/BRIEF-AGENT-GRAPHIFY-PARC-SUIVI-2026-09-05.md`  
   (si run déjà OK pour cette racine → ne pas refaire sauf GO force).

### Commande type

CLI `graphify extract` 0.9.54 exige un LLM pour les `.md`.  
Run = extracteurs **déterministes** via :

```powershell
<workspace>\Vault-Obsidian\_tools\graphify-venv\Scripts\python.exe `
  <workspace>\Vault-Obsidian\_tools\run-graphify-lab-chambre-canicule.py
```

### Excludes

`.graphifyignore` à la racine : secrets, `credentials/`, `<prive>.md`, `*.eml`, `*.pdf`, images, `.git/`, venv, `__pycache__/`, `graphify-out/`.  
(Repo a aussi un `.gitignore` pour `secrets.h` / `clim_config.json` / sqlite — l’ignore Graphify reste obligatoire pour images et Zone A.)

### Vague G1 (contexte)

| Racine | Out | Note |
|---|---|---|
| Canicule | `graphify-out\canicule` | OK 06/09 |
| lab-wol | `graphify-out\lab-wol` | OK 06/09 |
| lab-chambre-canicule | `graphify-out\lab-chambre-canicule` | **ce workspace** · OK 06/09 |

hub-materiel · Suivi-Pro · Lyla-Vision = déjà OK (05/09).  
**Vague G1 (Canicule + 2 labs) = complète 06/09.**

## Statut local

| Champ | Valeur |
|---|---|
| Dernier run | **2026-09-06 ~07:45** · GO Peter (workspace lab-chambre-canicule) |
| Sortie | `<workspace>\Vault-Obsidian\graphify-out\lab-chambre-canicule\graph.json` (~78 Ko) |
| Corpus | 9 docs + 8 code · ignore 9 (`.graphifyignore`) |
| Graphe | **92** nœuds · **131** arêtes |
| Exit / audit | **OK** · 0 hit `<prive>` / credentials / `<prive>` / `<prive>` |
| Notes | déterministe `extract_markdown` + AST · `parallel=False` · sans `--backend` · sans HTML · `RUN-META.json` · script `_tools/run-graphify-lab-chambre-canicule.py` · hub Cursor historique = Parc · ops mesure = ici |

## Interdits

Move fichiers Parc · install globale Graphify · commit de `graphify-out/` · `--backend` LLM · HTML.
