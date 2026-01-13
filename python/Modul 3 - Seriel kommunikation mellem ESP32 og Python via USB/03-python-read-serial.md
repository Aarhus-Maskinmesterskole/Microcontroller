# 📡 Modul 3: Python læser serielle data fra ESP32

## 📌 **Introduktion**
Nu hvor ESP32 sender serielle data via USB, skal vi **læse dataene i en Python-applikation**.

Vi bruger **PySerial** til at lytte til ESP32’s serielle output og vise det i realtid.

🔗 **Forrige modul:** [02-serial-print-esp32.md](02-serial-print-esp32.md)  
🔜 **Næste modul:** [04-troubleshooting.md](04-troubleshooting.md)  

---

## ✅ **Trin 1: Installer PySerial**
For at Python kan kommunikere med ESP32 via USB, skal vi installere **PySerial**.

Åbn en terminal eller kommandoprompt på din computer, og kør:
```bash
pip install pyserial
```

✅ **Nu er PySerial installeret og klar til brug!**  

---

## 📡 **Trin 2: Læs serielle data med Python**
Opret en ny **Python-fil på din computer** (`esp32_serial_read.py`) og indsæt følgende kode:

```python
import serial

ser = serial.Serial("COM3", 115200, timeout=1)  # Windows (tjek din COM-port!)
# ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)  # Linux/Mac

while True:
    line = ser.readline().decode("utf-8").strip()
    if line:
        print(f"ESP32: {line}")
```

💡 **Tip:**  
- Udskift `"COM3"` med den port, du fandt i **Modul 1** (fx `"COM4"` på Windows eller `"/dev/ttyUSB0"` på Linux/Mac).  
- Hvis du bruger en **Mac med CP210x**, kan du prøve `"/dev/tty.SLAB_USBtoUART"` i stedet for `"/dev/ttyUSB0"`.  

---

## ▶️ **Trin 3: Kør Python-scriptet**
1. Åbn en terminal eller kommandoprompt.  
2. Navigér til den mappe, hvor du har gemt `esp32_serial_read.py`.  
3. Kør scriptet:  
   ```bash
   python esp32_serial_read.py
   ```

✅ **Hvis alt fungerer, ser du ESP32’s serielle output i realtid!**  

Eksempel på output:
```
ESP32: TEMP:22.5C HUM:50.1%
ESP32: TEMP:22.6C HUM:49.8%
ESP32: TEMP:22.5C HUM:50.0%
```

---

## 🔍 **Trin 4: Forstå, hvad Python-scriptet gør**
🔹 **`serial.Serial("COM3", 115200, timeout=1)`** → Opretter en forbindelse til ESP32 via USB  
🔹 **`ser.readline()`** → Læser én linje fra ESP32  
🔹 **`.decode("utf-8").strip()`** → Oversætter byte-data til tekst  
🔹 **`print(f"ESP32: {line}")`** → Viser ESP32’s data i terminalen  

---

## ✅ **Hvad har vi opnået?**
✔️ ESP32 sender data via USB-seriel  
✔️ Vi har **installeret PySerial** på computeren  
✔️ Python kan nu **læse ESP32’s data i realtid**  

🔜 **Fortsæt til næste modul:** [04-troubleshooting.md](04-troubleshooting.md), hvor vi fejlfinder typiske problemer!  
