# Avis Sharon · ESP32 W2bis · 2026-08-07

> Collé par Peter 07/08. Condensation fidèle du message Sharon (lecture seule).  
> Brief source : `planning/brief-sharon-esp32-ecosysteme-2026-08-07.md`  
> Panier : `planning/panier-commande-esp32-solution-c-2026-08-07.md`

## Verdict global

**OK avec réserves.** Panier C techniquement juste (ESP32 DevKit + BME280 + alim secteur). Réserves = méthode (auto-échauffement, hauteur, appairage) + vérif amont WoL (MAC Ethernet NZXT). Budget = investissement portfolio (firmware/repo/W1), pas le thermomètre le moins cher.

## Par usage

| Usage | Verdict | Commentaire | Alt. si besoin |
|---|---|---|---|
| **Parc W2bis** | **OK** | Cœur du panier | — |
| **Canicule** (logger) | **OK avec réserves** | Protocole : offset, hauteur, appairage | — |
| **BME280 vs AHT20 / SHT** | **BME280 confirmé** | Humidité = critère clim | AHT20 si rupture · SHT31 si budget |
| **Nora** | **OK, sens inversé** | ESP32 expose `/metrics` · **n8n pull** 5 min | MQTT **non** phase 1 (pas de broker always-on) |
| **Parc W1 WoL lab** | **Bloqué en amont** | ESP32 UDP Wi-Fi OK · problème = **cible** NZXT | Pas de module Ethernet ESP32 |
| **Cloudflare / RDP** | **Aucun ESP32 derrière CF** | Pi = tunnel · ESP32 = LAN | — |
| **Lyla W3** | **Pas maintenant** | LED embarquée GPIO2 suffit | — |
| **Lyla-App / Memory / Orch.** | N/A | — | — |
| **Lyla-Vision / Avatar** | N/A | Pas de dérive CAM | — |
| **ESP32-S3** | **Non justifié** | WROOM-32 classique OK | — |

## Matériel

| Élément | Avis Sharon |
|---|---|
| ESP32 USB-C NodeMCU **39126** | **Adapté** · garder USB-C |
| BME280 budget **38419** | **Adapté** · commander **3** (pas 2) : appairage 24 h + spare |
| Dupont F/F **12331** | **Critique** · éloigner BME280 de la carte (≥20 cm) |
| Alim LDLC | **Souvent inutile** · d’abord tiroir chargeurs · si achat : **USB-A** 5 V/2 A (pas PD-only USB-C) |
| Boîtier | Manque · priorité basse (~3–5 €) |
| LED/bouton / Ethernet / S3 | Non |
| Météo ext. Haguenau | API Nora **avant** réception matos |

## Positions E1 / E2

Rôles **confirmés**. Ajustements gratuits :
1. **Même hauteur** 1,1–1,5 m pour les deux  
2. **E1** : BME280 à 20–30 cm du répéteur · ~10 cm du mur · ESP32 peut rester bas  
3. **E2** : ~50 cm de la tour · hors flux extraction  

**Protocole** : 24 h côte à côte · noter offsets · puis pose définitive.

## Risques (synthèse)

| # | Risque | Action |
|---|---|---|
| **R1** | NZXT : seule MAC **Wi-Fi** documentée · WoL S5 souvent KO en Wi-Fi | Relever MAC **Ethernet** · BIOS WoL · câble RJ45 **avant** achat ESP32 **et** Pi |
| **R2** | Auto-échauffement +1–3 °C | Firmware forced · OS bas · light sleep · BME déporté Dupont |
| **R3** | Faux BMP280 | Test registre ID `0x60` vs `0x58` à réception |
| **R4** | ESP32 = 2,4 GHz / WPA2 | Vérifier SSID box avant commande |
| **R5** | Broadcast / répéteur (W1) | Associer unité WoL au même AP que la cible |
| **R6** | Trous si push HTTP PC éteint | Prefer **pull** n8n |
| **R7** | Périmètre | Objet→Parc · thermique→Canicule · flux→Nora |

## Recommandation Sharon avant GO

**Étape 0 (0 €) :**
1. MAC Ethernet NZXT + BIOS + RJ45 (R1)  
2. SSID 2,4 GHz / WPA2 (R4)  
3. Tiroir chargeurs (supprimer panier LDLC si 2 trouvés)  
4. Réf. météo ext. Nora à vide  

**Au GO :**
5. Gotronic avec **3× BME280**  
6. Consignes firmware (forced, `/metrics` pull, pas de MAC WoL tant que R1 ouvert)  
7. Appairage 24 h avant pose  

**Timing :** technique prêt · trésorerie / impôts / STC ~28/08 · 4 vérifs gratuites d’abord. Pic chaleur sous 10 j = seule justification d’avancer (alors maj vault « gel 14/08 », pas contourner).

## Note Sharon hors format

Travail Karen validé (brief, périmètre, alternatives). **Valeur = protocole**, pas seulement le matos.
