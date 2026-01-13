# 🔬 **Modul 6: Realtidsplotning af flere sensorer**

## 📌 **1️⃣ Hvorfor plotte flere sensorer?**
Når vi arbejder med en **DHT22-sensor**, får vi både **temperatur og fugtighed**.  
Ved at visualisere dem **samtidigt**, kan vi bedre forstå, hvordan de ændrer sig over tid.

✅ **Målet er at vise både temperatur og fugtighed i samme realtidsgraf!**  

---

## 📌 **2️⃣ Opdater ESP32-koden til at sende flere sensorer**
For at **sende både temperatur og fugtighed fra ESP32**, skal vi sikre, at ESP32-koden sender to værdier:  

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
        print(f"{utime.time()},{temp},{fugt}")  # Send data via seriel
    except Exception as e:
        print("Fejl ved læsning af sensor:", e)
    utime.sleep(1)  # Opdatering hvert sekund
```

✅ **ESP32 sender nu både temperatur og fugtighed!**  

---

## 📌 **3️⃣ Python-kode til at plotte flere sensorer**
Nu opdaterer vi **Python-koden** på PC'en, så den **læser og visualiserer både temperatur og fugtighed**.  

```python
import serial
import pandas as pd
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 115200)  # Udskift med din serielle port
df = pd.DataFrame(columns=["Tid", "Temperatur", "Fugtighed"])

plt.ion()  # Aktiver interaktiv tilstand

while True:
    try:
        linje = ser.readline().decode("utf-8").strip().split(",")
        df.loc[len(df)] = [int(linje[0]), float(linje[1]), float(linje[2])]

        plt.clf()  # Rens grafen før vi tegner igen
        plt.plot(df["Tid"], df["Temperatur"], marker="o", linestyle="-", label="Temperatur")
        plt.plot(df["Tid"], df["Fugtighed"], marker="s", linestyle="-.", label="Fugtighed")

        plt.xlabel("Tid")
        plt.ylabel("Målinger")
        plt.title("Realtidsplot af temperatur og fugtighed")
        plt.legend()
        plt.pause(1)  # Opdater grafen hvert sekund

    except Exception as e:
        print("Fejl ved læsning af data:", e)
```

✅ **Nu viser grafen både temperatur og fugtighed i realtid!**  

---

## 📌 **4️⃣ Tilpas grafen**
For at gøre grafen **mere læsbar**, kan vi tilføje:  

✅ **Farver:** Brug farveargumentet i `plt.plot()`  
✅ **Gitter:** Brug `plt.grid(True)`  
✅ **Forskellige akser:** Hvis temperatur og fugtighed har **meget forskellige skalaer**, kan vi **opdele dem i to akser**:  

```python
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()  # Opret en sekundær y-akse
ax1.plot(df["Tid"], df["Temperatur"], "g-", label="Temperatur (°C)")
ax2.plot(df["Tid"], df["Fugtighed"], "b-", label="Fugtighed (%)")

ax1.set_xlabel("Tid")
ax1.set_ylabel("Temperatur (°C)", color="g")
ax2.set_ylabel("Fugtighed (%)", color="b")

plt.title("Temperatur og fugtighed i realtid")
plt.legend()
plt.pause(1)
```

✅ **Nu vises temperatur og fugtighed på hver sin y-akse for bedre læsbarhed!**  

---

## 📌 **5️⃣ Fejlfinding**
🔹 **"Grafen opdateres for hurtigt"**  
➡️ Brug `plt.pause(2)` for at opdatere grafen sjældnere.  

🔹 **"Fugtighedsdata er meget lav i forhold til temperatur"**  
➡️ Brug **to y-akser** (`twinx()`).  

🔹 **"Grafen viser kun én sensor"**  
➡️ Sørg for, at **ESP32 sender både temperatur og fugtighed** korrekt i Thonny.  

✅ **Nu er din realtidsgraf optimeret til flere sensorer!**  

🚀 **Fortsæt til næste modul: [07-save-data.md](07-save-data.md)**  
