# 📖 Lektion 7: ESP32 til PC Kommunikation
**Mandag, Uge 3 - 45 minutter**

## 🎯 Lektionsmål
- Etablere pålidelig seriel kommunikation mellem ESP32 og PC
- Forstå UART protokol og dataformater
- Implementere struktureret data transmission
- Designe robust kommunikationsprotokoller

---

## ⏰ Tidsplan (45 min)

### 📡 UART Protokol Teori (8 min)
**Grundlæggende principper:**
- **Baudrate** - data transmission hastighed (9600, 115200)
- **Data bits** - typisk 8 bit per karakter
- **Stop bits** - signal slutning (1 eller 2 bits)
- **Parity** - error detection (none, even, odd)
- **Flow control** - RTS/CTS eller software

**Praktisk demonstration:**
```cpp
Serial.begin(115200);  // Start seriel kommunikation
Serial.println("Hello PC!");  // Send enkelt besked
```

### 📊 Dataformat Design (10 min)
**Strukturerede vs. ustrukturerede data:**

**❌ Dårligt eksempel:**
```
Temp: 23.5°C Humidity: 65% Light: 456
```

**✅ Godt eksempel (CSV):**
```
23.5,65.2,456,87
```

**✅ Endnu bedre (JSON):**
```json
{"temp":23.5,"humid":65.2,"light":456,"gas":87,"time":"12:34:56"}
```

### 💻 Praktisk Implementation (20 min)
**ESP32 kode - struktureret data sender:**

```cpp
#include "DHT.h"

#define DHT_PIN 4
#define DHT_TYPE DHT22
#define LDR_PIN A0
#define GAS_PIN A3

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  Serial.println("ESP32,Ready,Start");  // Startup signal
}

void loop() {
  // Læs sensor data
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();
  int light = analogRead(LDR_PIN);
  int gas = analogRead(GAS_PIN);
  
  // Valider data
  if (isnan(temp) || isnan(humid)) {
    Serial.println("ERROR,DHT22,Read_Failed");
    delay(2000);
    return;
  }
  
  // Send struktureret data (CSV format)
  Serial.print("DATA,");
  Serial.print(millis());  // Timestamp
  Serial.print(",");
  Serial.print(temp, 1);   // 1 decimal
  Serial.print(",");
  Serial.print(humid, 1);
  Serial.print(",");
  Serial.print(light);
  Serial.print(",");
  Serial.println(gas);
  
  delay(5000);  // Send hver 5. sekund
}
```

**Aktivitet**: Teams implementerer ovenstående kode og tester output

### 🔧 Serial Monitor Testing (5 min)
**Verifikation af output:**
- Åbn Arduino IDE Serial Monitor
- Sæt baudrate til 115200
- Observér struktureret data output
- Test disconnect/reconnect scenarios

### 🛡️ Error Handling og Protokol Robusthed (2 min)
**Best practices:**
- **Consistent formatting** - samme format hver gang
- **Error messages** - klare fejlbeskeder
- **Startup signals** - PC ved hvornår ESP32 er klar
- **Heartbeat** - regelmæssige "alive" signaler
- **Data validation** - check for NaN, out-of-range values

---

## 📚 Undervisningsmateriale

### 🔌 Hardware Setup
- **ESP32** tilsluttet via USB
- **DHT22** på pin 4
- **LDR** på A0 med 10kΩ pull-down
- **Gas sensor** på A3

### 💻 Software
- **Arduino IDE** eller **PlatformIO**
- **Serial Monitor** til testing
- **DHT sensor library** (DHT sensor library by Adafruit)

---

## 🎯 Aktiviteter

### 🔧 Hands-on Coding
1. **Implementér** den givne ESP32 kode
2. **Test** serial output i Arduino IDE
3. **Modificér** output format (prøv JSON i stedet for CSV)
4. **Eksperimentér** med forskellige baudrates

### 📊 Protocol Design Exercise
**Gruppe diskussion:**
- Hvilke fordele/ulemper har CSV vs JSON?
- Hvordan ville I håndtere sensor fejl?
- Hvad sker hvis USB forbindelsen bliver afbrudt?

---

## 📝 Hjemmeopgaver til Næste Gang

### 💻 Praktisk Opgave (45 min)
1. **Udvid protokollen** med timestamp formatting
2. **Tilføj error recovery** - hvad sker ved sensor fejl?
3. **Eksperimentér** med JSON output format
4. **Test** forskellige baudrates og dokumentér forskelle

### 📖 Læsning (30 min)
- [Python Serial Programming](../../Laesemateriale/Programmering/01-Python-Serial.md)
- [Protocol Design Principles](../../Laesemateriale/Seriel-kommunikation/03-Protokol-Design.md)

### 🐍 Python Forberedelse
**Installer Python pakker til næste lektion:**
```bash
pip install pyserial
pip install matplotlib
```

---

## 🎯 Læringsudbytte Check

### ✅ Den studerende kan nu:
- [ ] **Konfigurere** UART kommunikation mellem ESP32 og PC
- [ ] **Designe** strukturerede dataformater (CSV/JSON)
- [ ] **Implementere** robust error handling
- [ ] **Validere** og debugge seriel kommunikation
- [ ] **Dokumentere** protokol design beslutninger

### 🔍 Evaluering
- **Funktionel kode**: ESP32 sender struktureret data (60%)
- **Error handling**: Robust fejlhåndtering implementeret (25%)
- **Protocol design**: Velbegrundet format valg (15%)

---

## ⚠️ Almindelige Problemer og Løsninger

### 🚨 USB Driver Issues
**Problem**: ESP32 ikke fundet som seriel port
**Løsning**: Installer CP210x eller CH340 drivers

### 📡 Data Corruption
**Problem**: Ødelagte karakterer i serial output
**Løsning**: Tjek baudrate match mellem ESP32 og Serial Monitor

### 📊 Inconsistent Data Format
**Problem**: Nogle linjer har forkert antal kommaer
**Løsning**: Valider alle sensor readings før transmission

---

## ➡️ Forbindelse til Næste Lektion
Lektion 8 vil bygge videre med:
- **Python serial client** til at modtage ESP32 data
- **Real-time parsing** og data processing
- **Bidirectional communication** - PC sender kommandoer til ESP32

---

*Seriel kommunikation er rygraden i embedded systems - mestre dette, og I har en stærk foundation! 📡*