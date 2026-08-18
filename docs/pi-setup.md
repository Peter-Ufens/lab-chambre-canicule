# Lab-Tiny-Peter — plateforme (17/08/2026)

Machine unique pour **ce lab** et pour [`lab-wol`](https://github.com/Peter-Ufens/lab-wol).  
Hub Cursor : `D:\IA-CURSOR\Parc-Maison` (pas un 2ᵉ projet Cursor).

Pas de mot de passe, pas de secret Wi-Fi dans ce dépôt.

## Fait

| Point | Valeur |
|---|---|
| Matériel | Raspberry Pi 5 **8 Go** · case officielle · dissipateur CPU · alim **27 W** |
| Hostname | `Lab-Tiny-Peter` |
| OS | Raspberry Pi OS **64-bit** (Trixie) · Imager **v2.0.10** |
| Support install | SanDisk microSD 64 Go (boot SSD Kingston = plus tard) |
| LAN | IPv4 **192.168.1.25** (DHCP, peut bouger) · MAC Wi-Fi `88-A2-9E-9A-F1-44` |
| SSH | `ssh peter@192.168.1.25` (user **minuscules**) |
| Bureau navigateur | Raspberry Pi Connect · client **2.12.2** · [devices](https://connect.raspberrypi.com/devices) |
| Collecteur | **OK 18/08** · `http://192.168.1.25:8080/health` · systemd user `canicule-collector` · code dans `collector/` |

HDMI PC classique : **incompatible** (il faut un câble **micro-HDMI**). Headless + Connect = volontaire.

## Captures (Gamma / FT)

| Fichier | Quoi |
|---|---|
| [imager-os-64bit](captures/2026-08-17-imager-os-64bit.png) | Choix OS 64-bit (pas 32, pas Legacy) |
| [imager-stockage-sandisk](captures/2026-08-17-imager-stockage-sandisk.png) | Volume ~59,5 Go / F: (pas le Kingston) |
| [imager-hostname](captures/2026-08-17-imager-hostname.png) | Étape nom d’hôte |
| [imager-connect-off](captures/2026-08-17-imager-connect-off.png) | Connect **éteint** dans Imager (activé ensuite en SSH) |
| [imager-ecriture-terminee](captures/2026-08-17-imager-ecriture-terminee.png) | Write OK · hostname, locale, user, Wi-Fi, SSH |
| [connect-signin-ok](captures/2026-08-17-connect-signin-ok.png) | Appareil lié au compte Raspberry |
| [connect-lab-tiny-peter-online](captures/2026-08-17-connect-lab-tiny-peter-online.png) | Online · Screen sharing + Remote shell |

## Recette courte

1. Imager : Pi 5 · OS 64-bit · SanDisk · personnalisation (hostname, user `peter`, SSH, Wi-Fi, clavier FR). Connect Imager = non.
2. Alim **coupée** avant d’insérer la carte. Puis **27 W** seulement.
3. SSH. Si `known_hosts` râle après reflash : `ssh-keygen -R 192.168.1.25`.
4. `sudo apt update && sudo apt full-upgrade -y` · `rpi-connect on` · `rpi-connect signin` (URL sur le PC).
5. Auto-login bureau (`raspi-config` B4) + `loginctl enable-linger` pour le partage d’écran sans HDMI.

Détail Parc : `planning/liens-tutos-youtube-esp-pi-2026-08-17.md`.
