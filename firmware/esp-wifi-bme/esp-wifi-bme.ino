/*
  ESP Wi-Fi 2,4 GHz + BME280 + POST vers le Pi
  Identite = MAC (pas l'IP DHCP de l'ESP).
  Le Pi horodate. Intervalle 1 minute.
*/

#include <WiFi.h>
#include <WiFiClient.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include "secrets.h"

#ifndef COLLECTOR_HOST
#define COLLECTOR_HOST "192.168.1.25"
#endif
#ifndef COLLECTOR_PORT
#define COLLECTOR_PORT 8080
#endif

#define I2C_SDA 21
#define I2C_SCL 22
#define LED_PIN 2
#define PERIOD_MS 60000

Adafruit_BME280 bme;
bool bme_ok = false;

void connectWifi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("Wi-Fi ");
  Serial.println(WIFI_SSID);
  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - start < 25000) {
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    Serial.print(".");
    delay(400);
  }
  Serial.println();
  if (WiFi.status() == WL_CONNECTED) {
    Serial.print("sta_ip=");
    Serial.println(WiFi.localIP());
    Serial.print("mac=");
    Serial.println(WiFi.macAddress());
    digitalWrite(LED_PIN, HIGH);
  } else {
    Serial.println("Wi-Fi KO");
    digitalWrite(LED_PIN, LOW);
  }
}

bool postOnce() {
  if (WiFi.status() != WL_CONNECTED) {
    connectWifi();
    if (WiFi.status() != WL_CONNECTED) {
      return false;
    }
  }
  float t = bme_ok ? bme.readTemperature() : NAN;
  float h = bme_ok ? bme.readHumidity() : NAN;
  float p = bme_ok ? bme.readPressure() / 100.0F : NAN;

  char url[80];
  snprintf(url, sizeof(url), "http://%s:%d/ingest", COLLECTOR_HOST, COLLECTOR_PORT);

  char body[256];
  snprintf(
    body,
    sizeof(body),
    "{\"mac\":\"%s\",\"temp_c\":%.2f,\"hum_pct\":%.1f,\"press_hpa\":%.1f,\"rssi\":%d}",
    WiFi.macAddress().c_str(),
    t,
    h,
    p,
    WiFi.RSSI()
  );

  WiFiClient client;
  HTTPClient http;
  http.setTimeout(8000);
  if (!http.begin(client, url)) {
    Serial.println("http.begin KO");
    return false;
  }
  http.addHeader("Content-Type", "application/json");
  int code = http.POST(body);
  String resp = http.getString();
  http.end();
  Serial.print("POST ");
  Serial.print(code);
  Serial.print(" ");
  Serial.println(resp);
  return code == 200;
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  delay(2000);
  Serial.println("115200 + EN si vide. POST 1 min vers le Pi (id=MAC).");

  Wire.begin(I2C_SDA, I2C_SCL);
  bme_ok = bme.begin(0x76, &Wire);
  if (!bme_ok) {
    bme_ok = bme.begin(0x77, &Wire);
  }
  Serial.println(bme_ok ? "BME280 OK" : "BME280 KO");

  connectWifi();
  postOnce();
}

void loop() {
  bool ok = postOnce();
  digitalWrite(LED_PIN, ok ? HIGH : LOW);
  delay(PERIOD_MS);
}
