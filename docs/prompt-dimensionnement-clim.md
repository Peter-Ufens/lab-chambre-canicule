# Prompt IA — dimensionner une clim (jour J)

Copier-coller dans ChatGPT, Claude, Cursor, etc. **Après** 1 à 2 semaines de mesures.

## 1. Exporter les mesures (Pi)

```bash
cd ~/lab-canicule
bash export-mesures-pour-ia.sh > mesures.txt
cat mesures.txt
```

Coller le contenu de `mesures.txt` dans le bloc **MESURES** du prompt ci-dessous.

## 2. Prompt (à personnaliser)

Remplacer les `[CROCHETS]`. Ne pas inventer le DPE si inconnu.

---

```
Tu es un conseiller technique grand public, pas un vendeur. Réponds en français, clair, sans jargon inutile.

## Contexte matériel

J'ai mesuré la température et l'humidité de ma pièce avec :
- 2× ESP32 + capteur BME280 (température, humidité)
- 1× Raspberry Pi 5 qui agrège les relevés (1 mesure/minute, moyennes par heure et par tranche jour/nuit)
- Sonde A : près de l'entrée (souvent plus fraîche)
- Sonde B : au point le plus chaud (souvent coin PC)

Liste complète : voir BOM projet lab-chambre-canicule (GitHub Peter-Ufens).

## Période de mesure

Du [DATE_DEBUT] au [DATE_FIN] ([NB_JOURS] jours), pendant [canicule / été / période chaude].

## Mesures (extrait Raspberry Pi)

Coller ici le export mesures.txt :

MESURES :
[COLler ICI le contenu de mesures.txt]

## Logement

- Surface pièce (ou logement si pertinent) : [X] m²
- DPE / isolation si connue : [A à G, ou « inconnu (location) »]
- Ville / région (optionnel) : [Haguenau / Alsace / …]
- Préférence : climatisation **connectée** si possible

## Ce que je te demande

1. Résumer ce que disent les mesures (écart entrée vs point chaud, pics, nuit vs jour).
2. Recommander une **famille de puissance** (BTU/h et kW froid), pas un modèle magasin précis.
3. Comparer **clim mobile** vs **split fixe** pour mon cas, avantages/inconvénients.
4. Indiquer si ma préférence « connectée » est réaliste (app constructeur, ou Raspberry + IR/API).
5. Signaler les limites (m² seuls insuffisants, mesures courtes, etc.).

## Interdits

- Ne pas me donner un SKU Leroy Merlin / Amazon à 847 €.
- Ne pas inventer mon DPE si je l'ai marqué inconnu.
- Ne pas promettre une consommation électrique exacte sans fiche produit.

Format : sections courtes, tableaux OK, ton pédagogique.
```

---

## 3. Variante courte (si contexte limité)

```
Voici des moyennes horaires de température (2 sondes, Pi, période [X jours]) :

[COLLER mesures.txt]

Pièce [X] m², isolation [DPE ou inconnu]. Je veux une clim adaptée, de préférence connectée.
Compare mobile vs split. Donne une fourchette BTU/h / kW froid, pas un modèle précis.
```
