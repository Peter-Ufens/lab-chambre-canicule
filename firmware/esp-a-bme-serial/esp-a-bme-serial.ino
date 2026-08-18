/*
  ESP-A — lecture BME280 (série USB)
  Broches lab : Rouge 3V3 · Noir GND · Bleu GPIO21 SDA · Jaune GPIO22 SCL
  Adresse I2C : 0x76 (Pimoroni) puis 0x77 si besoin.
*/

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define I2C_SDA 21
#define I2C_SCL 22

Adafruit_BME280 bme;

void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("Ouvre le moniteur a 115200 puis appuie EN/RST si ecran vide.");
  Wire.begin(I2C_SDA, I2C_SCL);

  bool ok = bme.begin(0x76, &Wire);
  if (!ok) {
    ok = bme.begin(0x77, &Wire);
  }
  if (!ok) {
    Serial.println("BME280 introuvable. Verifier clips D21/D22/3V3/GND.");
    while (true) {
      delay(1000);
    }
  }
  Serial.println("BME280 OK");
}

void loop() {
  Serial.print("temp_c=");
  Serial.print(bme.readTemperature(), 2);
  Serial.print("  hum_pct=");
  Serial.print(bme.readHumidity(), 1);
  Serial.print("  press_hpa=");
  Serial.println(bme.readPressure() / 100.0F, 1);
  delay(2000);
}
