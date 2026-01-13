# 📊 **Modul 4: Realtidsplotning af DHT22-data**

## 📌 **1️⃣ Forbind ESP32 til din PC**
Sørg for, at **ESP32 er forbundet til din PC via USB**, og at **den sender data fra DHT22**.  

**Test i Thonny**: Åbn terminalen og se, om data udskrives i formatet:
```
1710342345,22.5,45.3
1710342346,22.6,45.1
1710342347,22.7,44.9
```
✅ **Hvis du ser dette, er ESP32 klar!**  

---

## 📌 **2️⃣ Sørg for, at PC'en kan læse data**
Vi kan bruge Python til at **læse de serielle data** fra ESP32.

**Test seriel forbindelse med følgende kode:**
```python
import serial

ser = serial.Serial("COM3", 115200)  # Udskift med din port, fx "/dev/ttyUSB0" på Linux/macOS

while True:
    linje = ser.readline().decode("utf-8").strip()
    print(linje)  # Udskriv ESP32's data i terminalen
```
✅ **Hvis du ser DHT22-data i terminalen, er din PC forbundet korrekt til ESP32!**  

🚀 **Fortsæt til næste trin: Realtidsplotning af data.**
