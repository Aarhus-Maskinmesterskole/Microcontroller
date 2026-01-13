# 📡 **Realtidsplotning med ESP32 & Python**

Dette kursus guider dig igennem **realtidsplotning af DHT22-sensordata** fra en ESP32 til en PC, hvor Python bruges til at **læse, behandle og visualisere data**.

⚠️ **Forudsætninger:**  
✅ ESP32 er **allerede flashed med MicroPython**  
✅ **Thonny** er installeret og kan forbinde til ESP32  
✅ **Python er installeret** på din PC  

---

## 📌 **Indhold:**
| Modul | Emne |
|-------|------|
| 📄 [01-setup.md](01-setup.md) | 🔧 Installér nødvendige Python-biblioteker |
| 📄 [02-esp32-serial.md](02-esp32-serial.md) | 📡 ESP32: Send DHT22 data via seriel (USB) |
| 📄 [03-pc-read-serial.md](03-pc-read-serial.md) | 🖥️ PC Python: Læs seriel data fra ESP32 |
| 📄 [04-realtime-plot.md](04-realtime-plot.md) | 📊 Realtidsplotning af DHT22-data |
| 📄 [05-moving-average.md](05-moving-average.md) | 🔄 Glidende gennemsnit i realtid |
| 📄 [06-multiple-sensors.md](06-multiple-sensors.md) | 🔬 Flere sensorer i samme plot |
| 📄 [07-save-data.md](07-save-data.md) | 💾 Gem og hent realtidsdata |
| 📄 [08-advanced-plot.md](08-advanced-plot.md) | 🚀 Interaktive grafer med `FuncAnimation` |

---

## 📌 **Krav og opsætning**

### **1️⃣ Installér Python-pakker på PC**
```bash
pip install pyserial pandas matplotlib numpy
```

### **2️⃣ Forbind DHT22 til ESP32**
| DHT22 Pin | ESP32 Pin |
|-----------|----------|
| **VCC**   | 3.3V |
| **GND**   | GND |
| **DATA**  | GPIO4 |

---

## 📌 **Hvad lærer vi?**
✔️ ESP32 sender **DHT22-temperatur og luftfugtighed** via seriel  
✔️ Python læser **serielle data og plotter dem i realtid**  
✔️ Vi anvender **glidende gennemsnit for jævnere grafer**  
✔️ Realtidsplotning af **flere sensorer** samtidig  
✔️ **Gemning af målinger** til en CSV-fil  

🚀 **Lad os komme i gang!** 🎉  
