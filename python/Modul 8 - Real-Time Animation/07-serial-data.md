# 🔌 Modul 06: Læs Sensor-Data via Seriel Port (ESP32 + Python)

## 📌 Hvad lærer du i dette modul?
✔️ Hvordan du **læser data fra en seriel port** (f.eks. fra en ESP32 eller Arduino)  
✔️ Hvordan du **visualiserer real-time data fra en sensor**  
✔️ Hvordan du **filtrerer data for bedre læsbarhed**  
✔️ Hvordan du **opsætter ESP32 til at sende JSON-data via seriel port**  

---

## 📌 Trin 1: Opsætning af ESP32
For at læse sensor-data fra en **ESP32** skal vi først programmere den til at sende data via **seriel port**.

### 🔧 **Forudsætninger**
✅ En ESP32 med en **DHT22-sensor** (temperatur og fugtighed) tilsluttet  
✅ `pyserial`-biblioteket installeret i Python:
```bash
pip install pyserial
```
✅ ESP32 programmeret via MicroPython  

---

## 📌 Trin 2: ESP32-kode til at sende seriel data
ESP32 koden sender **JSON-data** med temperatur- og fugtighedsværdier fra en DHT22-sensor.

🔹 **Upload følgende kode til din ESP32**:
```python
import machine
import dht
import time
import json
import sys

# Initialiser DHT22 på GPIO4
sensor = dht.DHT22(machine.Pin(4))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        # Opret JSON-streng
        data = json.dumps({"temperature": temp, "humidity": hum})

        # Send JSON-streng via seriel (print skriver til UART)
        print(data)

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)

    time.sleep(1)  # Vent 1 sekund mellem målinger
```

---

## 📌 Trin 3: Læs og Visualiser Sensor-Data i Real-Time i Python
Nu laver vi et Python-script, der **læser real-time data fra ESP32** og **animerer plottet**.

```python
import serial
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Åbn seriel port (tilpas denne til din enhed)
# Linux/Mac: Brug '/dev/ttyUSB0', på Windows: 'COM3'
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Opret figur og akse
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(15, 30)  # Temperaturinterval

xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', label="Temperatur")

def init():
    ln.set_data([], [])
    return ln,

def update(frame):
    line = ser.readline().decode(errors='ignore').strip()
    try:
        data = json.loads(line)  # Konverter JSON-streng til dictionary
        xdata.append(frame)
        ydata.append(data["temperature"])
        ln.set_data(xdata[-100:], ydata[-100:])  # Vis kun de seneste 100 målinger
    except:
        pass
    return ln,

# Opret animation
ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, interval=500, blit=False)

plt.legend()
plt.show()
```

---

## 🔥 Hvordan fungerer koden?
1️⃣ **ESP32 måler temperatur og fugtighed** og sender data via **seriel port** i JSON-format.  
2️⃣ **Python-scriptet læser seriel data**, dekoder JSON og **opdaterer grafen i realtid**.  
3️⃣ **Grafen viser kun de seneste 100 målinger**, så den ikke bliver for stor.  

---

## ✅ Opgaver
1️⃣ Upload ESP32-koden og verificér, at den sender JSON-data.  
2️⃣ Kør Python-scriptet og se temperaturgrafen opdatere sig i real-time.  
3️⃣ Tilføj en **blå linje for fugtighedsmålinger**.  
4️⃣ Gem dataene i en **CSV-fil** i realtid.  

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
