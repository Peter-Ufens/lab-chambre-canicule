# Collecteur (Pi)

L’ESP est **client**. Il POST vers le Pi. Identité = **MAC**, pas l’IP DHCP de l’ESP (`.26` / `.27` = journal seulement).

- URL : `http://192.168.1.25:8080/ingest` (IPv4 du Pi ; `lab-tiny-peter.home` résout souvent en IPv6, l’ESP32 aime mal)
- Santé : `http://192.168.1.25:8080/health`
- Dernier point : `http://192.168.1.25:8080/latest`

Si le DHCP du **Pi** bouge, on change `COLLECTOR_HOST` dans `secrets.h` (une IP, celle du serveur). Les ESP gardent leur MAC.

Brut 48 h, moyennes heure / tranche / jour avec `n_samples`. Trou > 3 min = événement `down`. Écriture SQLite par lots (~5 min).
