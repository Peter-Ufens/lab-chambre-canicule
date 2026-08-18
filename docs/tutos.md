# Tutos visuels (tout public)

Rien à souder. Case Pi = **clips**. Capteur BME = cordon Qwiic / Dupont. USB.

Captures du lab (Imager, hostname, Connect) : [`captures/`](captures/).

## Raspberry Pi 5

| Quoi | Lien |
|---|---|
| Case officielle (clips, pas de vis) | https://www.youtube.com/watch?v=urzWrq4FySo |
| Petit dissipateur sur le CPU | https://www.youtube.com/watch?v=I1-7vJMhkio |
| Case officielle (vue démontage) | https://www.youtube.com/watch?v=vYUF1H-_7TQ |
| Raspberry Pi Imager | https://www.youtube.com/watch?v=MepM1juFYzA |
| Téléchargement Imager | https://www.raspberrypi.com/software/ |

## ESP32 (USB-C chez nous)

| Quoi | Lien |
|---|---|
| Premier flash Arduino IDE | https://www.youtube.com/watch?v=AitCKcyjHuQ |
| Article FR Arduino + ESP32 | https://tropratik.fr/programmer-la-carte-esp32-devkitc-avec-larduino-ide |
| BME280 + ESP32 | https://randomnerdtutorials.com/esp32-bme280-arduino-ide-pressure-temperature-humidity/ |

Les vidéos ESP montrent parfois du **micro-USB**. Nos cartes Gotronic sont en **USB-C**. Même logique (port COM).

## Recette flash USB (18/08)

- Câble **Gotronic** uniquement (pas le StarTech du SSD Pi). Jamais USB PC + prise 5 V en même temps.
- Driver : **CP210x Universal Windows Driver** (zip Silicon Labs). Port : **COM3** (un ESP branché à la fois).
- Arduino IDE 2.3.10 · gestionnaire de cartes : **esp32** par Espressif (pas « Arduino ESP32 Boards » / Nano).
- Carte : **ESP32 Dev Module**. Blink : GPIO **2** (`LED_BUILTIN` n’existe pas).
- BME : Rouge 3V3 · Noir GND · Bleu D21 · Jaune D22 · clip Qwiic **sur** le BME. Sketch dans `firmware/esp-a-bme-serial/`.
- Moniteur série **115200**. Si écran blanc : bouton **EN** / RST sur l’ESP.
- Firmware Wi-Fi + POST 1 min : `firmware/esp-wifi-bme/` (identité = MAC, pas l’IP ESP). Collecteur : `http://192.168.1.25:8080/health`
- Les °C sur le bureau sont plus hauts (auto-chauffe USB). Placement E1/E2 plus tard.
