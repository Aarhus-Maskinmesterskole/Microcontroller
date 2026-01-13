# 🖥️ **Modul 3: PC Python - Læs seriel data fra ESP32**

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

## 📌 **2️⃣ Find din serielle port**
Find den korrekte **COM-port (Windows) eller tty-device (Linux/macOS)**:  

### **Windows:**  
1️⃣ Åbn **Enhedshåndtering** (`devmgmt.msc`)  
2️⃣ Find **"USB Serial Device (COMx)"**  

### **Linux/macOS:**  
```bash
ls /dev/ttyUSB*
```

**Notér porten**, fx `"COM3"` (Windows) eller `"/dev/ttyUSB0"` (Linux/macOS).  

---

## 📌 **3️⃣ Python-kode til at læse serielle data**
Kopier koden og gem den som **`read_serial.py`**, og kør den med `python read_serial.py`.

```python
import serial

# Udskift "COM3" med din port, fx "/dev/ttyUSB0" på Linux/macOS
ser = serial.Serial("COM3", 115200)

while True:
    linje = ser.readline().decode("utf-8").strip()
    print(linje)  # Udskriv ESP32's data i terminalen
```

✅ **Nu læser vi serielle data fra ESP32!**  

---

## 📌 **4️⃣ Fejlfinding**
🔹 **Fejl: "Porten eksisterer ikke"**  
➡️ Sørg for, at ESP32 er tilsluttet, og at den rigtige port er valgt.  

🔹 **Fejl: "Permission denied" (Linux/macOS)**  
➡️ Giv rettigheder til den serielle port:  
```bash
sudo chmod 666 /dev/ttyUSB0
```

🔹 **Fejl: "Data er tomme"**  
➡️ Sørg for, at ESP32 kører og sender data fra DHT22.  

✅ **Nu er din PC forbundet til ESP32 via seriel!**  

🚀 **Fortsæt til næste modul: [04-realtime-plot.md](04-realtime-plot.md)**  
