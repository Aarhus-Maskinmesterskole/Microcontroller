# 🔌 Modul 2.1: Tilslutning af DHT22 til ESP32

## 📡 **Hvad er DHT22?**
DHT22 er en digital sensor, der måler **temperatur og luftfugtighed**. Den er nem at bruge med ESP32 og er populær i IoT-projekter.

### 📊 **Specifikationer for DHT22**
| Egenskab | Specifikation |
|----------|--------------|
| 🌡 **Temperaturområde** | -40°C til 80°C |
| ❄ **Temperaturpræcision** | ± 0.5°C |
| 💧 **Luftfugtighedsområde** | 0% til 100% RH |
| 📏 **Luftfugtighedspræcision** | ± 2-5% |
| ⚡ **Forsyningsspænding** | 3.3V - 5V |
| 🔄 **Samplingstid** | Hver 2 sekunder |
| 📶 **Kommunikation** | 1-wire digital data |

---

## 🛠 **Hardware, du skal bruge**
✔️ **ESP32** (eller ESP8266)  
✔️ **DHT22-sensor**  
✔️ **3 x jumper wires** (hunk/hank)  
✔️ *(Valgfrit)* 10kΩ pull-up modstand  

---

## 🔌 **Tilslutning af DHT22 til ESP32**

| DHT22 Pin | ESP32 Pin |
|-----------|-----------|
| **VCC** (3.3V eller 5V) | **3.3V (Vin)** |
| **GND** (Jord) | **GND** |
| **DATA** | **GPIO4** (eller en anden ledig GPIO) |

💡 **Tip:**  
- Hvis du bruger en **DHT22 uden pull-up modstand**, kan du tilføje en **10kΩ modstand** mellem **VCC og DATA** for et stærkere signal.  
- Husk at **bruge 3.3V**, da ESP32’s GPIO'er ikke er 5V-tolerante.

---

## 🖼️ **Diagram for forbindelser**  

DHT22       ESP32

+------+ +------+ | VCC | --> | 3.3V | | GND | --> | GND | | DATA | --> | GPIO4| +------+ +------+


## 🔗 **Hvis du bruger en breadboard-opsætning**, kan du forbinde komponenterne som vist nedenfor:

       +----+
       | DHT|
       | 22 |
       +----+
          |
      GPIO4 (ESP32)

---

## ✅ **Tjek dine forbindelser**
1. **Sørg for, at alle ledninger sidder korrekt.**  
2. **Tjek, at ESP32 får strøm** (LED’en på boardet skal lyse).  
3. **Brug et multimeter** til at sikre, at **VCC giver korrekt spænding (3.3V)**.  
4. **Hvis din DHT22 ikke reagerer**, prøv en anden GPIO-pin (fx GPIO15).  

---

## 📌 **Hvad er næste skridt?**
🔜 **Fortsæt til næste modul:**  
📄 **[02-micropython-setup.md](02-micropython-setup.md)** – Opsætning af MicroPython på ESP32  

