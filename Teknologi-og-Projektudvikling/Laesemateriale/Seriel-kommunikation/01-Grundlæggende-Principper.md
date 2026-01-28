# 📡 Grundlæggende Principper for Seriel Kommunikation

## 🎯 Introduktion
Seriel kommunikation er fundamentet for dataoverførsel mellem mikrocontrollere og computere. I modsætning til parallel kommunikation, hvor flere bits sendes samtidigt, sender seriel kommunikation data bit for bit over en enkelt forbindelse.

## 🔌 Hvad er Seriel Kommunikation?

### Definition
**Seriel kommunikation** er en metode til at overføre data sekventialt - én bit ad gangen - over en kommunikationskanal eller computerbuss.

### Fordele
- **Færre ledninger** - kun behov for 2-3 forbindelser
- **Lavere omkostninger** - mindre komplekse kredsløb
- **Større afstande** - mindre signal degradering
- **Mindre elektromagnetisk interferens**

### Ulemper
- **Langsommere** end parallel kommunikation
- **Mere kompleks timing** - kræver synchronization
- **Protokol overhead** - start/stop bits og error checking

---

## 📊 UART - Universal Asynchronous Receiver/Transmitter

### 🔧 UART Grundlag
UART er den mest almindelige form for seriel kommunikation mellem mikrocontrollere og computere via USB.

#### Hovedkomponenter:
- **TX (Transmit)**: Sender data
- **RX (Receive)**: Modtager data  
- **GND (Ground)**: Fælles reference

#### Signalformat:
```
Idle → Start Bit → Data Bits → Parity Bit → Stop Bit(s) → Idle
```

### ⚙️ UART Konfiguration

#### Baudrate
**Definition**: Antal bits per sekund (bps)

**Almindelige baudrates:**
- 9600 bps - langsom, meget pålidelig
- 19200 bps - standard for mange sensorer
- 57600 bps - hurtigere applikationer
- 115200 bps - høj hastighed, standard for ESP32
- 921600 bps - meget hurtig, kan være ustabil

#### Data Bits
- **5-9 bits** muligt
- **8 bits** er standard (1 byte per karakter)

#### Parity Bit
- **None** - ingen error checking (mest almindeligt)
- **Even** - lige antal 1'er
- **Odd** - ulige antal 1'er

#### Stop Bits
- **1 bit** - standard
- **2 bits** - ekstra sikkerhed ved høje hastigheder

---

## 🔄 Kommunikationsmønstre

### 1. Simplex
**Envejs kommunikation** - kun fra sender til modtager
```
ESP32 ──(TX)──→ PC
```

### 2. Half-Duplex
**Tovejs kommunikation** - men kun én retning ad gangen
```
ESP32 ←──(RX/TX)──→ PC
```

### 3. Full-Duplex
**Samtidig tovejs kommunikation**
```
ESP32 ──(TX)──→ ──(RX)── PC
ESP32 ──(RX)──← ──(TX)── PC
```

---

## 📝 Dataformater og Protokoller

### ASCII vs. Binær Data

#### ASCII (Text-based)
**Fordele:**
- Menneskeligt læsbart
- Let at debugge
- Fungerer med alle terminaler

**Eksempel:**
```
"TEMP:23.5,HUMID:65.2\n"
```

#### Binær Data
**Fordele:**
- Mere effektiv
- Mindre overhead
- Hurtigere transmission

**Eksempel:**
```
[0x01][0x17][0x0C][0x29][0x41]
```

### Strukturerede Dataformater

#### 1. CSV (Comma-Separated Values)
```
timestamp,temperature,humidity,light,gas
1634567890,23.5,65.2,456,87
```

#### 2. JSON (JavaScript Object Notation)
```json
{
  "timestamp": 1634567890,
  "sensors": {
    "temperature": 23.5,
    "humidity": 65.2,
    "light": 456,
    "gas": 87
  }
}
```

#### 3. Custom Protocol
```
<START>DATA,1634567890,23.5,65.2,456,87<END>
```

---

## 🛡️ Error Detection og Handling

### 1. Parity Checking
Simple error detection - kan fange enkelte bit fejl

### 2. Checksum
Matematisk validering af data integritet
```cpp
// Simpel checksum
uint8_t calculateChecksum(String data) {
  uint8_t sum = 0;
  for (int i = 0; i < data.length(); i++) {
    sum += data[i];
  }
  return sum;
}
```

### 3. CRC (Cyclic Redundancy Check)
Avanceret error detection med høj nøjagtighed

### 4. Acknowledgment (ACK/NAK)
Confirmation of successful data reception
```
PC → ESP32: "GET_TEMP"
ESP32 → PC: "ACK,23.5"
```

---

## 🔧 Praktisk Implementation på ESP32

### Basic Serial Setup
```cpp
void setup() {
  Serial.begin(115200);  // Initialize UART
  while (!Serial) {      // Wait for connection
    delay(10);
  }
  Serial.println("ESP32 Ready");
}
```

### Data Transmission
```cpp
void sendSensorData() {
  String dataPacket = "DATA,";
  dataPacket += millis();
  dataPacket += ",";
  dataPacket += temperature;
  dataPacket += ",";
  dataPacket += humidity;
  
  Serial.println(dataPacket);
}
```

### Command Processing
```cpp
void processCommands() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "GET_TEMP") {
      Serial.println("TEMP," + String(temperature));
    } else if (command == "GET_ALL") {
      sendSensorData();
    } else {
      Serial.println("ERROR,UNKNOWN_COMMAND");
    }
  }
}
```

---

## 🌍 Real-World Applications

### Industrial Automation
- **PLC kommunikation** med sensorer
- **SCADA systemer** data collection
- **Motor controllers** og drives

### Consumer Electronics
- **GPS enheder** og navigation
- **Bluetooth** og WiFi moduler
- **LCD displays** og touch screens

### Scientific Instruments
- **Data loggers** og measurement equipment
- **Laboratory instruments**
- **Environmental monitoring**

---

## 📋 Best Practices

### 1. Protocol Design
- **Keep it simple** - kompleksitet fører til fejl
- **Consistent formatting** - samme struktur altid
- **Clear error messages** - let at debugge
- **Version your protocol** - plan for fremtidige ændringer

### 2. Error Handling
- **Always validate data** - check for NaN, out-of-range
- **Implement timeouts** - don't wait forever
- **Graceful degradation** - system continues with partial data
- **Log errors** - facilitate debugging

### 3. Performance
- **Choose appropriate baudrate** - balance speed vs reliability
- **Minimize overhead** - efficient data formats
- **Buffer management** - handle burst transmissions
- **Flow control** - prevent data loss

---

## 🔗 Sammenligning med Andre Protokoller

| Protokol | Hastighed | Kompleksitet | Afstand | Anvendelse |
|----------|-----------|--------------|---------|------------|
| UART/Serial | Medium | Lav | Kort-medium | Debug, basic communication |
| SPI | Høj | Medium | Kort | High-speed peripherals |
| I2C | Lav-medium | Medium | Kort | Multiple devices, sensors |
| CAN | Medium | Høj | Lang | Automotive, industrial |
| Ethernet | Meget høj | Høj | Meget lang | Networking, Internet |

---

## 🎯 Sammenfatning

Seriel kommunikation via UART er en fundamental teknologi for embedded systems. Det giver en:

- **Simpel og pålidelig** metode til dataoverførsel
- **Fleksibel protokol design** muligheder
- **Bred kompatibilitet** på tværs af platforme
- **Solid foundation** for komplekse kommunikationssystemer

I de næste lektioner vil vi bygge videre på disse grundprincipper og implementere praktiske løsninger med ESP32, Python, Node-RED og Home Assistant.

---

*Husk: Seriel kommunikation handler ikke kun om at sende data - det handler om at skabe pålidelige, robuste forbindelser mellem systemer! 📡*