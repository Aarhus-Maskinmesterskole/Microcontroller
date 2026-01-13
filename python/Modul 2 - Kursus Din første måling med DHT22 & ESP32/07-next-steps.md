# 🚀 Modul 2.7: Hvad nu? Udvidelse af dit DHT22-projekt

## 📌 **Introduktion**
Nu hvor du har fået **DHT22 til at fungere med ESP32**, kan vi udvide projektet med **datagenerering, logging, trådløs kommunikation og IoT-integration**.  

🔗 **Forrige modul:** [06-troubleshooting.md](06-troubleshooting.md)  

---

## 📡 **1. Send data til en server (IoT)**
En af de mest populære anvendelser af DHT22 er at sende måledata til en **server eller IoT-platform**.

### 🛠 **Mulige løsninger**
- **HTTP Request til en webserver** → Send data til en **Flask API**, **Node.js server**, eller en IoT-platform som **ThingSpeak**.  
- **MQTT (Message Queuing Telemetry Transport)** → Send data til en **MQTT-broker** som **Mosquitto eller HiveMQ**.  

📄 **Eksempel: Send data til en HTTP-server**
```python
import urequests

url = "http://example.com/api/dht22"
data = {"temperature": 22.5, "humidity": 48.7}

response = urequests.post(url, json=data)
print(response.text)
response.close()
```
🔗 Videre læsning: ESP32 som IoT-enhed med HTTP API eller MQTT.

---

## 📊 2. Log data over tid
Vil du gemme dine målinger til senere analyse? Her er et par måder at gøre det på:     
- 🔹 Mulige løsninger     
    - 🔹 Gem data i en lokal fil på ESP32’s hukommelse (med open() i MicroPython).     
    - 🔹 Gem data i en CSV-fil til senere analyse i Excel eller Pandas (Python).
    - 🔹 Send data til en database som SQLite, MariaDB eller Firebase.    

📄 Eksempel: Log data til en lokal fil
```python
with open("dht_log.csv", "a") as f:
    f.write(f"22.5,48.7,{time.time()}\n")
```
🔗 Videre læsning: Brug af CSV og databaser med MicroPython.

---

## 🌍 3. Lav en ESP32 Webserver
Med en ESP32 Webserver kan du se temperaturdata direkte i din browser, uden at skulle bruge en ekstern database.

📄 Eksempel: Enkel ESP32 Webserver
```python
import network
import socket

ssid = "WiFi-Navn"
password = "WiFi-Kode"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n")
    conn.send("<html><body><h1>Temperatur: 22.5°C</h1></body></html>")
    conn.close()
```
🔗 Videre læsning: ESP32 Webserver med HTML og JavaScript.

---

🤖 4. Brug Machine Learning til at forudsige værdier

Vil du tage projektet til næste niveau? Brug Machine Learning til at filtrere data, finde mønstre eller forudsige temperaturer.
- 🔹 Mulige løsninger
    - 🔹 Glidende gennemsnit (Moving Average) til datafiltrering.
    - 🔹 Brug af en Random Forest-model til at forudsige temperatur.
    - 🔹 LSTM (Long Short-Term Memory) til tidserieanalyse.

📄 Eksempel: Glidende gennemsnit i MicroPython

```python
def moving_average(data, window_size=3):
    return sum(data[-window_size:]) / window_size
```
🔗 Videre læsning: Machine Learning til sensorfiltrering med ESP32 og Python.

---

🎯 Opsummering: Hvad kan du gøre nu?
|🚀 Mulighed	|🛠 Hvad du lærer|
|-------------|----------------|
|📡 Send data til en IoT-server	|HTTP API, MQTT|
|📊 Log målinger over tid	|CSV, Databaser|
|🌍 Lav en ESP32 Webserver	|HTML, WebSockets|
|🤖 Brug Machine Learning	|Datafiltrering, Prediktion|
✅ Næste skridt

Vælg en udvidelse, og begynd at bygge videre på dit DHT22-projekt! 🚀

📢 Har du lavet en spændende udvidelse?
👉 Del dit projekt med os i et GitHub-repository eller en blogpost! 🎉
