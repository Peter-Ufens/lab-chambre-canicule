# Deux remotes GitHub — barrière public / privé

| Remote | Repo | Visibilité | Rôle |
|---|---|---|---|
| **`origin`** | [`lab-chambre-canicule-private`](https://github.com/Peter-Ufens/lab-chambre-canicule-private) | **PRIVÉ** | Ops · plans · travail quotidien · **seul** endroit où un secret pourrait un jour vivre (et encore : préférer hors git) |
| **`public`** | [`lab-chambre-canicule`](https://github.com/Peter-Ufens/lab-chambre-canicule) | **PUBLIC** | Vitrine FT / Gamma / code pédagogique |

**≠ lab-wol** (autre projet · déjà privé).

## Règle anti-fuite

| Interdit sur **public** | OK |
|---|---|
| `secrets.h`, `.env`, mots de passe Wi-Fi | `secrets.h.example` avec placeholders |
| `clim_config.json` réel | `clim_config.example.json` |
| `*.sqlite` / bases mesures | docs + scripts |
| credentials / PERSONNES | jamais |

`.gitignore` local couvre déjà `secrets.h`, `clim_config.json`, `.env`, sqlite.

## Commandes

```powershell
# travail quotidien → privé
git push origin main

# publier la vitrine (après relecture : pas de secret)
git push public main
```

Clone frais ops :

```powershell
git clone https://github.com/Peter-Ufens/lab-chambre-canicule-private.git
cd lab-chambre-canicule-private
git remote add public https://github.com/Peter-Ufens/lab-chambre-canicule.git
```
