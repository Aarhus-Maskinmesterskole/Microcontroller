# 🌡️ Modul 2.5: Din første måling med DHT22 & ESP32

## 📌 **Introduktion**
Nu hvor vi har installeret MicroPython og DHT22-biblioteket, er vi klar til at tage vores **første måling** af temperatur og luftfugtighed.

🔗 **Forrige modul:** [03-install-dht-library.md](03-install-dht-library.md)  
🔜 **Næste modul:** [05-troubleshooting.md](05-troubleshooting.md)  

---

## 🛠️ **Trin 1: Forbind DHT22 korrekt**
Sørg for, at din DHT22 er **korrekt tilsluttet** ESP32:

| DHT22 Pin | ESP32 Pin |
|-----------|-----------|
| **VCC** (3.3V eller 5V) | **3.3V (Vin)** |
| **GND** (Jord) | **GND** |
| **DATA** | **GPIO4** (eller en anden ledig GPIO) |

💡 **Tip:**  
- **Husk en 10kΩ pull-up modstand** mellem **VCC og DATA**, hvis din DHT22 ikke har én indbygget.  
- Sørg for, at **GPIO4** er fri og ikke bruges af andre enheder.

---

## 📄 **Trin 2: Opret en ny Python-fil i Thonny**
1. **Åbn Thonny** og opret en ny fil (**File → New**).  
2. **Gem filen som `dht22_test.py`** (`File → Save As`).  

---

## 📝 **Trin 3: Skriv kode for at aflæse temperatur og luftfugtighed**
Kopier følgende kode ind i din nye fil:

```python
import machine
import dht
import time

# Initialiser DHT22 på GPIO4
dht_pin = machine.Pin(4)
sensor = dht.DHT22(dht_pin)

while True:
    try:
        sensor.measure()  # Udløs en måling
        temp = sensor.temperature()  # Hent temperatur (Celsius)
        hum = sensor.humidity()  # Hent luftfugtighed (%)

        print(f"Temperatur: {temp:.1f} C   Luftfugtighed: {hum:.1f}%")
        
        time.sleep(2)  # Vent 2 sekunder før næste måling
    except OSError as e:
        print("Fejl ved aflæsning af DHT22:", e)
```
---
## ▶️ Trin 4: Kør koden i Thonny
1. Klik "Run" (▶️) eller tryk F5.
2. Se resultaterne i Shell:
```shell
Temperatur: 23.5°C  Luftfugtighed: 48.2%
Temperatur: 23.6°C  Luftfugtighed: 48.3%
```
3. Hvis du får en fejl, så tjek forbindelserne og fortsæt til fejlfinding i næste modul.

---

## 🔄 Trin 5: Forstå, hvad koden gør
🔹 sensor.measure() – Starter en ny måling    
🔹 sensor.temperature() – Henter temperaturen i Celsius    
🔹 sensor.humidity() – Henter luftfugtigheden i procent (%)    
🔹 print(f"Temperatur: {temp:.1f} C  Luftfugtighed: {hum:.1f}%") – Viser resultatet pænt i Shell    
🔹 time.sleep(2) – Venter 2 sekunder før næste måling    

💡 Tip: Hvis du vil vise temperatur i Fahrenheit, kan du tilføje:
```python
temp_f = temp * 9/5 + 32
print(f"Temperatur: {temp_f:.1f}°F")
```
---
## ✅ Trin 6: Tjek, at alt virker
Hvis du ser temperatur- og luftfugtighedsværdier i Shell, fungerer din DHT22! ✅    
Hvis du får "Fejl ved aflæsning af DHT22", så gå videre til fejlfinding i næste modul.

🔜 Fortsæt til næste modul:     
📄 [06-troubleshooting](06-troubleshooting.md)
