# 📝 Hjemmeopgave 1: ESP32 Opsætning og Grundlæggende Programmering
**Uge 1 - Afleveres før Lektion 4**

## 🎯 Formål
Denne opgave sikrer at du har et fungerende ESP32 setup og forstår grundlæggende programmering. Det er fundamentet for resten af kurset.

---

## 📋 Opgave Del A: Installation og Opsætning (40 point)

### A1. Udviklingsenvironment (15 point)
**Installer og konfigurer dit udviklingsenvironment:**

1. **Arduino IDE Installation**
   - Download og installer Arduino IDE 2.0+ fra arduino.cc
   - Start IDE og verificer at det fungerer

2. **ESP32 Board Support**
   - Tilføj ESP32 board manager URL: `https://dl.espressif.com/dl/package_esp32_index.json`
   - Installer "ESP32 by Espressif Systems" via Board Manager
   - Verificer at "ESP32 Dev Module" er tilgængelig

3. **USB Driver**
   - Installer passende USB driver (CP210x eller CH340)
   - Test at ESP32 bliver genkendt som COM port

**Aflever:** Screenshots af:
- Arduino IDE med ESP32 board valgt
- Board Manager med ESP32 installeret
- Device Manager/System Information der viser ESP32 COM port

### A2. Hardware Test (15 point)
**Upload og test grundlæggende funktionalitet:**

```cpp
// Test program - kopiér og upload dette
void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);  // Built-in LED
  Serial.println("ESP32 Test Program Started");
}

void loop() {
  digitalWrite(2, HIGH);
  Serial.println("LED ON");
  delay(1000);
  
  digitalWrite(2, LOW);
  Serial.println("LED OFF");
  delay(1000);
}
```

**Verifikation:**
- LED på ESP32 blinker hver sekund
- Serial Monitor viser "LED ON/OFF" beskeder
- Baudrate sat til 115200

**Aflever:** Video (10-15 sekunder) der viser blinkende LED og Serial Monitor output

### A3. Pin Layout Forståelse (10 point)
**Lær ESP32 pinout:**

1. Find officielt ESP32 pinout diagram
2. Identificer følgende pins på dit board:
   - GPIO pins brugt til digital I/O
   - Analog input pins (A0, A3, etc.)
   - Power pins (3.3V, 5V, GND)
   - SPI/I2C pins

**Aflever:** 
- Annoteret foto af dit ESP32 board med vigtige pins markeret
- Kort beskrivelse (3-5 linjer) af forskellen mellem GPIO og analog pins

---

## 📋 Opgave Del B: Sensor Integration (40 point)

### B1. DHT22 Sensor (20 point)
**Tilslut og programmer DHT22 temperatur/luftfugtighed sensor:**

**Hardware tilslutning:**
- VCC → 3.3V
- GND → GND  
- DATA → GPIO 4

**Software (start med dette skelet):**
```cpp
#include "DHT.h"

#define DHT_PIN 4
#define DHT_TYPE DHT22

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println("DHT22 Test Started");
}

void loop() {
  // DIN KODE HER:
  // 1. Læs temperatur og luftfugtighed
  // 2. Check for fejl (isnan())
  // 3. Print til Serial Monitor
  // 4. Vent 2 sekunder
}
```

**Krav:**
- Læs temperatur og luftfugtighed hver 2. sekund
- Håndter fejl hvis sensor ikke svarer
- Format output: "Temp: XX.X°C, Humidity: XX.X%"

**Aflever:** 
- Din komplette kode
- Screenshot af Serial Monitor med mindst 5 målinger

### B2. LDR Lyssensor (20 point)
**Tilslut og programmer LDR (Light Dependent Resistor):**

**Hardware tilslutning:**
```
ESP32 A0 ────┬──── LDR ──── 3.3V
             │
             └──── 10kΩ ──── GND
```

**Software krav:**
- Læs analog værdi fra A0
- Konverter til procent (0-100%)
- Print format: "Light Level: XXX (XX%)"
- Sample hver sekund

**Tip:** Brug `map()` function til at konvertere 0-4095 til 0-100%

**Aflever:**
- Din kode
- Test data: Mørk, normal, lys (mindst 3 målinger af hver)

---

## 📋 Opgave Del C: Kombination og Optimering (20 point)

### C1. Multi-Sensor Program (15 point)
**Kombiner DHT22 og LDR i et program:**

**Krav:**
- Læs begge sensorer hver 3. sekund
- Struktureret output format
- Fejlhåndtering for DHT22
- Tilføj timestamp (millis())

**Forventet output format:**
```
[12345] Temp: 23.5°C, Humid: 65.2%, Light: 456 (45%)
[15345] Temp: 23.6°C, Humid: 65.1%, Light: 489 (48%)
```

### C2. Serial Kommandoer (5 point)
**Tilføj grundlæggende kommando funktionalitet:**

Programmet skal kunne modtage kommandoer via Serial Monitor:
- "GET_TEMP" → returner kun temperatur
- "GET_LIGHT" → returner kun lys niveau
- "GET_ALL" → returner alle sensor data

**Aflever:** 
- Komplet kode
- Screenshot der viser kommando test (send mindst 3 forskellige kommandoer)

---

## 📖 Refleksion og Læring (Bonus: 10 point)

**Besvar følgende spørgsmål (2-3 linjer hver):**

1. **Udfordringer:** Hvilke problemer stødte du på, og hvordan løste du dem?

2. **Sensor sammenligning:** Hvad er forskellen mellem DHT22 (digital) og LDR (analog) kommunikation?

3. **Timing:** Hvorfor er der forskellige delays for forskellige sensorer?

4. **Fremtidige ideer:** Hvordan kunne du forbedre dit program yderligere?

5. **Projektideer:** Hvilke projekter kunne du lave med disse sensorer?

---

## 📋 Aflevering

### Format
- **Én ZIP fil** med navnet: `Fornavn_Efternavn_Hjemmeopgave1.zip`
- **Mappestruktur:**
  ```
  Hjemmeopgave1/
  ├── Arduino_Kode/
  │   ├── test_program.ino
  │   ├── dht22_test.ino
  │   ├── ldr_test.ino
  │   └── multi_sensor.ino
  ├── Screenshots/
  │   ├── arduino_setup.png
  │   ├── serial_output.png
  │   └── hardware_photo.jpg
  ├── Video/
  │   └── hardware_test.mp4
  └── refleksion.txt
  ```

### Deadline
**Afleveres senest:** Søndag kl. 23:59 før Lektion 4

### Evaluering

| Kriterium | Fremragende (90-100%) | Tilfredsstillende (70-89%) | Acceptabel (50-69%) | Utilstrækkelig (0-49%) |
|-----------|----------------------|---------------------------|-------------------|----------------------|
| **Installation** | Alt fungerer perfekt | Mindre problemer løst | Grundlæggende setup | Ikke fungerende |
| **DHT22** | Robust med fejlhåndtering | Grundlæggende funktionalitet | Fungerer delvist | Ikke fungerende |
| **LDR** | Præcis kalibrering | Fungerer korrekt | Grundlæggende læsning | Ikke fungerende |
| **Kombination** | Elegant integration | Fungerer sammen | Basic kombination | Ikke integreret |
| **Kode kvalitet** | Velstruktureret og kommenteret | God struktur | Fungerende kode | Dårlig kvalitet |

---

## 💡 Tips og Hjælp

### Debugging Tips
1. **Serial Monitor baudrate** - sørg for den matcher Serial.begin()
2. **DHT22 timing** - kræver 2+ sekunder mellem læsninger
3. **LDR kalibrering** - test under forskellige lysforhold
4. **Power supply** - nogle sensorer kræver ekstern strøm

### Hvor Finder Du Hjælp
- **Arduino Reference:** arduino.cc/reference
- **ESP32 dokumentation:** docs.espressif.com
- **DHT bibliotek:** Adafruit DHT sensor library
- **Discord/Teams:** Still spørgsmål til dine klassekammerater

### Almindelige Fejl
- **DHT22 returnerer NaN:** Tjek forbindelser og delays
- **LDR giver konstant værdi:** Verificer voltage divider
- **Serial Monitor blank:** Tjek baudrate og USB driver

---

## 🎯 Læringsudbytter

Efter denne opgave skal du kunne:
- **Installere** og konfigurere ESP32 udviklingsenvironment
- **Tilslutte** og programmere digitale og analoge sensorer
- **Implementere** grundlæggende fejlhåndtering
- **Kombinere** multiple sensorer i samme program
- **Debugge** hardware og software problemer

---

**Held og lykke! 🚀 Husk at stille spørgsmål hvis du sidder fast - det er bedre at spørge end at give op!**