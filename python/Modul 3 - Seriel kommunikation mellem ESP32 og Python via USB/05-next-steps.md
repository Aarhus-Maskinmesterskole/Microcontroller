# 🚀 Modul 5: Udvidelser og næste skridt

## 📌 **Introduktion**
Nu hvor din **ESP32 sender serielle data** til Python, er du klar til at udvide projektet! 🎉  
Her er nogle ideer til, hvordan du kan forbedre og bruge din serielle data mere effektivt.

🔗 **Forrige modul:** [04-troubleshooting.md](04-troubleshooting.md)  

---

## 📡 **1. Log data til en fil**
I stedet for kun at vise data i terminalen, kan vi **gemme målinger til en fil**.

### 🛠 **Hvordan?**
- **Gem data i en CSV-fil** for senere analyse i **Excel eller Pandas**.  
- **Gem data i en database** som **SQLite eller Firebase**.  

📄 **Eksempel: Log data til en lokal fil**
```python
import serial
import time

ser = serial.Serial("COM3", 115200, timeout=1)

with open("dht_log.csv", "a") as f:
    while True:
        line = ser.readline().decode("utf-8").strip()
        if line:
            f.write(f"{time.time()},{line}\n")
            print(f"Data gemt: {line}")
```
✅ **Nu gemmes alle målinger i `dht_log.csv`!**  

---

## 🌍 **2. Send data til en webserver**
ESP32 kan sende måledata til en **server eller cloud-tjeneste**, så du kan overvåge dataene eksternt.

### 🛠 **Mulige løsninger**
- **Brug MQTT** til at sende data til en IoT-platform.  
- **Brug HTTP POST** til at sende data til en webserver.  

📄 **Eksempel: Send data via HTTP**
```python
import urequests

url = "http://example.com/api/dht22"
data = {"temperature": 22.5, "humidity": 48.7}

response = urequests.post(url, json=data)
print(response.text)
response.close()
```
🔗 **Videre læsning:** Opsætning af **ESP32 som en IoT-enhed** med HTTP API eller MQTT.

---

## 📊 **3. Visualisering af data i realtid**
Vil du **se dine måledata i en graf i realtid**? Python kan bruge **Matplotlib** til at vise temperatur og luftfugtighed visuelt.

📄 **Eksempel: Real-time graf med Matplotlib**
```python
import serial
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 115200, timeout=1)

temps, hums = [], []
plt.ion()  # Aktiver real-time opdatering

while True:
    line = ser.readline().decode("utf-8").strip()
    if line.startswith("TEMP:"):
        temp = float(line.split(" ")[0].split(":")[1][:-1])
        hum = float(line.split(" ")[1].split(":")[1][:-1])

        temps.append(temp)
        hums.append(hum)

        plt.clf()
        plt.plot(temps, label="Temperatur (C)")
        plt.plot(hums, label="Luftfugtighed (%)")
        plt.legend()
        plt.pause(0.1)  # Opdater grafen
```
✅ **Nu opdateres grafen i realtid med ESP32’s data!**  

---

## 🤖 **4. Brug Machine Learning til at forudsige værdier**
Hvis du vil **tage projektet til næste niveau**, kan du bruge **Machine Learning** til at **filtrere data, finde mønstre eller forudsige fremtidige temperaturer**.

### 🔹 **Mulige løsninger**
- **Glidende gennemsnit (Moving Average) til datafiltrering.**  
- **Brug af en Random Forest-model til at forudsige temperatur.**  
- **LSTM (Long Short-Term Memory) til tidserieanalyse**.  

📄 **Eksempel: Glidende gennemsnit i Python**
```python
def moving_average(data, window_size=3):
    return sum(data[-window_size:]) / window_size
```
🔗 **Videre læsning:** Brug Machine Learning til **sensorfiltrering med ESP32 og Python**.

---

## 🎯 **Opsummering: Hvad kan du gøre nu?**
| 🚀 **Mulighed** | 🛠 **Hvad du lærer** |
|---------------|----------------|
| 📡 Send data til en IoT-server | HTTP API, MQTT |
| 📊 Log målinger over tid | CSV, Databaser |
| 🌍 Visualiser data i en real-time graf | Matplotlib |
| 🤖 Brug Machine Learning | Datafiltrering, Prediktion |

---

## ✅ **Næste skridt**
Vælg en **udvidelse**, og begynd at bygge videre på dit ESP32-projekt! 🚀  

📢 **Har du lavet en spændende udvidelse?**  
👉 Del dit projekt med os i et **GitHub-repository eller en blogpost!** 🎉  
