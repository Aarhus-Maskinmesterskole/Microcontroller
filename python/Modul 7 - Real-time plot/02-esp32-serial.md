# 📡 **Modul 2: ESP32 - Send DHT22 data via seriel (USB)**

## 📌 **Forudsætninger**
✅ **ESP32 er allerede flashed med MicroPython**  
✅ **Thonny er installeret og sat op**  
✅ **Python og nødvendige pakker er installeret på PC**  
✅ **DHT22-sensor er tilsluttet ESP32**  

---

## 📌 **1️⃣ Tilslut DHT22 til ESP32**  
| DHT22 Pin | ESP32 Pin |
|-----------|----------|
| **VCC**   | 3.3V |
| **GND**   | GND |
| **DATA**  | GPIO4 |

**Bemærk:** Husk at bruge en **10kΩ pull-up modstand** mellem **VCC og DATA**.

---

## 📌 **2️⃣ Installer MicroPython-bibliotek til DHT22**  
For at kunne **læse data fra DHT22**, skal vi installere MicroPython's **dht**-modul.

1️⃣ Åbn **Thonny**, og tilslut din ESP32  
2️⃣ Kør følgende kommando i REPL:

```python
import upip
upip.install("micropython-dht")
```

✅ **Nu er DHT22-biblioteket installeret!**  

---

## 📌 **3️⃣ ESP32-kode til at læse og sende DHT22-data**
Kopier koden nedenfor og upload den til din ESP32 med Thonny.

```python
import dht
import machine
import utime

sensor = dht.DHT22(machine.Pin(4))  # DHT22 tilsluttet GPIO4

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()  # Temperatur i °C
        fugt = sensor.humidity()     # Luftfugtighed i %
        print(f"{utime.time()},{temp:.2f},{fugt:.2f}")  # Send data via seriel
    except Exception as e:
        print("Fejl ved læsning af sensor:", e)
    utime.sleep(1)  # Opdatering hvert sekund
```

✅ **Nu sender ESP32 temperatur- og fugtighedsdata via seriel (USB)!**  

---

## 📌 **4️⃣ Test serielle data fra ESP32**
For at **teste**, om ESP32 sender data korrekt, kan du åbne **Thonny's terminal** og se, om data bliver udskrevet i formatet:

```
1710342345,22.5,45.3
1710342346,22.6,45.1
1710342347,22.7,44.9
```

✅ **Nu er ESP32 klar til at sende DHT22-data!**  

🚀 **Fortsæt til næste modul: [03-pc-read-serial.md](03-pc-read-serial.md)**  
