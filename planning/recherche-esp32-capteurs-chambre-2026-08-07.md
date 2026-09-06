# Recherche ESP32 · capteurs chambre (W2bis)

**Date :** 2026-08-07  
**Statut :** avis Sharon **OK avec réserves** · panier C ajusté (3× BME · LDLC conditionnel) · **pas d’achat** tant que étape 0 + **GO Peter**  
**Avis :** `planning/avis-sharon-esp32-ecosysteme-2026-08-07.md`  
**Panier :** `planning/panier-commande-esp32-solution-c-2026-08-07.md`  
**Périmètre Parc :** matériel, emplacements, alim, inventaire, MAC/IP plus tard  
**Hors Parc :** conclusions clim / dimensionnement → Canicule · webhook / n8n → Nora · Pi/CF → file U / Cloudflare

## Objectif Peter (session)

Se renseigner sur l’ESP32 + **adaptateur / alim** + **matériel nécessaire** pour **2 points** :
1. Entrée de la chambre  
2. Coin PC (NZXT)

Mesure continue temp (+ humidité) · données utiles plus tard pour Canicule (~02/2027), sans rouvrir l’achat clim.

## Emplacements + alimentation (Peter 07/08 · figé en prep)

| Point | Prise / topologie | Alim ESP32 |
|---|---|---|
| **Entrée chambre** | Prise murale déjà prise par le **répéteur Wi-Fi** · Peter met une **multiprise triangle** | Répéteur + **chargeur USB mural 5 V** (ESP32) sur la multiprise · **secteur**, pas « USB box » |
| **Coin PC** | **Prise dispo** · multiprise bureau | Achat d’une **alim USB 5 V** (chargeur mural) branchée sur multiprise · **pas** dépendre du USB de la tour |

Les deux ESP32 = **USB 5 V continu via chargeur secteur** (mesure périodique ≠ pile CR123 WoL).

## Rôles des 2 ESP32 (Peter 07/08 · clarifié)

| Unité | Rôle phase 1 | Après Raspberry (file U) |
|---|---|---|
| **ESP32 entrée** | **Lecture thermique** (temp/humidité) · **vocation durable** | Reste capteur chambre |
| **ESP32 coin PC** | Lecture thermique **dans un premier temps** | Libérable → **W1 WoL lab** et/ou autre micro-projet écosystème |

Parc = objets + inventaire · Canicule = lecture thermique plus tard · Nora = flux (plus tard) · Pi = always-on distant (autre fil).

## Décisions techniques proposées (Karen + Sharon, 07/08)

| Choix | Décision | Pourquoi |
|---|---|---|
| Capteur | **BME280** (I2C) | Temp + humidité + pression · plus fiable que DHT22 |
| Alt. OK | AHT20 | Si pas besoin pression |
| Alimentation | **2× chargeur USB 5 V mural** + multiprises | Entrée = triangle avec répéteur · coin PC = prise dispo |
| Quantité | 2× ESP32 DevKit + 2× BME280 | Deux emplacements |
| Raspberry | **Hors** ce fil | Chantier Pi / CF / WoL = file U · après STC ~28/08 |

## Check LDLC (2026-08-07 · Karen)

| Recherche LDLC.com | Résultat observé |
|---|---|
| `esp32` / `ESP32` | **Aucun résultat** produit DIY DevKit |
| `bme280` | **Aucun résultat** module BME280 |
| Chargeurs / câbles USB / multiprises | Catalogue LDLC **oui** |
| Raspberry Pi | **Oui** (file **U** · magasin Haguenau pour le Pi) |

**Conclusion :** ESP32 + BME280 + Dupont → **Gotronic** (ou Amazon) · **pas** LDLC.  
Chez **LDLC** : **2× chargeurs USB 5 V** (+ multiprise triangle entrée si besoin) · Pi = autre panier.

### BOM concrète ×2 kits (Gotronic + LDLC alim · prix TTC ~07/08)

| Qté | Article | Où | Prix u. ~ | Sous-total ~ |
|---:|---|---|---:|---:|
| 2 | NodeMCU **ESP32** USB-C | Gotronic [39126](https://www.gotronic.fr/art-module-nodemcu-esp32-usb-c-47499.htm) | **14,30 €** | 28,60 € |
| 2 | Module **BME280** budget | Gotronic [38419](https://www.gotronic.fr/art-module-bme280-sku27347-37634.htm) | ~**8–12 €** | ~16–24 € |
| 1 | Lot fils Dupont F-F | Gotronic / Amazon | ~**3–6 €** | 3–6 € |
| 2 | Câble USB (A→C) | Gotronic / maison / LDLC | 0–4 € | 0–8 € |
| **2** | **Chargeur mural USB 5 V ≥1 A** | **LDLC** (ou chargeur téléphone déjà là) | ~**8–15 €** | ~16–30 € |
| **1** | **Multiprise triangle** (entrée) | — | **Déjà chez Peter** | **0 €** |
| **2** | **Chargeur mural USB 5 V ≥1 A** | **LDLC** | ~**8–15 €** | ~16–30 € |

**Ordre de grandeur 2 kits + 2 alims (sans triangle) :** ~**65–95 €** TTC + ports.

**Panier liens prêts :** `planning/panier-commande-esp32-solution-c-2026-08-07.md`  
**Brief Sharon :** `planning/brief-sharon-esp32-ecosysteme-2026-08-07.md`  
**Câblage I2C :** BME280 VIN → **3,3 V** · GND · SDA → GPIO21 · SCL → GPIO22.

## 3 propositions d’achat (Karen 07/08 · pas de GO)

### Verdict magasins « informatiques »

| Enseigne | ESP32 DIY | BME280 | Dupont | Chargeur USB mural | Multiprise | Tout-en-un ? |
|---|---|---|---|---|---|---|
| **Materiel.net** | **Non** (0 résultat `esp32`) | Non (faux positifs Wi-Fi « BE ») | Non utile | **Oui** | **Oui** | **Non** |
| **LDLC** | **Non** | **Non** | Non | **Oui** | **Oui** | **Non** (Pi oui · file U) |
| **Kubii** | **Oui** (~14,40 € ESP32-WROOM) | **Oui** (14,00 € · stock) | **Oui** (kits jumper) | Partiel (pas idéal mur PC) | **Non** | Quasi DIY · alim à part |
| **Gotronic** | **Oui** (13,90–14,30 €) | **Oui** | **Oui** | Non focus | Non | DIY · alim à part |
| **Amazon.fr** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** (1 panier) |

### Proposition A · Amazon (1 commande)

Tout le W2bis dans **un seul panier** Prime : 2× ESP32 USB-C · 2× BME280 · Dupont · 2× chargeurs USB 5 V · 1× multiprise triangle.  
**+** simplicité · **−** marques variables · vérifier « vrai BME280 » (pas BMP280).  
Budget typique : ~**55–90 €**.

### Proposition B · Kubii (DIY) + LDLC ou Materiel.net (secteur)

1. **Kubii** : 2× ESP32 (~14,40 €) + 2× BME280 (14 €) + kit jumper (~quelques €).  
2. **LDLC** (Haguenau / web) **ou Materiel.net** : 2× chargeurs USB 5 V + multiprise triangle.  
**+** FR / qualité DIY · **−** **2 commandes**.  
Budget DIY Kubii ~**50–60 €** + alim/multiprise ~**20–40 €**.

### Proposition C · Gotronic (DIY) + LDLC (secteur) · reco Karen si pas Amazon

1. **Gotronic** : panier déjà chiffré (ESP32 USB-C 14,30 € · BME budget · Dupont).  
2. **LDLC** : chargeurs + triangle (même magasin que le futur **Pi**).  
**+** prix ESP32 connus · cohérence Pi chez LDLC · **−** 2 commandes.

**Materiel.net seul = impossible** pour le cœur ESP32/BME280. Utile seulement pour la partie **secteur** (comme LDLC).

## Checklist prep (avant panier)

- [x] Topologie **entrée** : multiprise triangle · répéteur + ESP32 (secteur via chargeur USB)
- [x] Topologie **coin PC** : prise dispo · alim USB murale à prévoir sur multiprise
- [x] Rôles : entrée = thermique durable · coin PC = thermique puis recyclable (WoL / autre) après Pi
- [x] Multiprise triangle déjà à la maison
- [ ] Capteur figé panier : **BME280** (défaut) vs AHT20
- [x] ESP32 **USB-C** (solution C)
- [ ] 0 / 1 / 2 chargeurs USB 5 V déjà dispo ? (panier LDLC = 2 si 0)
- [x] Brief Sharon préparé · attente avis
- [ ] **GO Peter** avant commande · maj inventaire seulement au GO

## Liens

- Pistes : `context/pistes-esp32.md`
- A-traiter : `entree/redirections/archive/route_vers/hub-materiel/2026-08-07-depuis-evacuation-esp32-canicule-parc.md`
- Vault idées : `04-Idees/IDEE-Wake-on-LAN-ESP32.md` · `ESP32-vs-Raspberry-Pi-Comparatif.md`

## Hors scope cette fiche

Tunnel Cloudflare · RDP · Finances · casque/webcam · clim · Companion-OS · achat Raspberry (file U).
