# 💻 Praktiske Eksempler

Denne mappe indeholder komplette, fungerende kodeeksempler for alle platforme og teknologier brugt i kurset.

## 📁 Struktur

### 📡 [Serial Communication](Serial-Communication/)
Grundlæggende og avancerede eksempler på seriel kommunikation mellem ESP32 og computer.

**Eksempler:**
- [ESP32-Python Basic](Serial-Communication/ESP32-Python-Basic.md) - Komplet kommunikationssystem
- ESP32-CSV-Logger - Data logging i CSV format
- ESP32-JSON-Protocol - JSON-baseret protokol
- Bidirectional-Commands - Command-response system
- Error-Recovery - Robust error handling

### 🐍 [ESP32-Python](ESP32-Python/)
Integrerede systemer der kombinerer ESP32 firmware med Python applikationer.

**Eksempler:**
- Real-time Plotter - Live data visualization
- Multi-sensor Dashboard - Complete monitoring system  
- Data Analysis Tool - Statistical analysis
- Alert System - Threshold-based notifications
- Configuration Manager - Dynamic ESP32 configuration

### 🔄 [ESP32-NodeRED](ESP32-NodeRED/)
ESP32 integration med Node-RED for flow-baseret automation.

**Eksempler:**
- Basic Flow Setup - Getting started
- Dashboard Creation - Interactive visualizations
- MQTT Integration - Wireless communication
- Database Logging - Persistent data storage
- Automation Rules - Intelligent triggering

### 🏠 [ESP32-HomeAssistant](ESP32-HomeAssistant/)
Komplet integration med Home Assistant for hjemmeautomatisering.

**Eksempler:**
- MQTT Discovery - Automatic device setup
- Custom Sensors - ESP32 as HA sensors
- Automation Scripts - HA automation examples
- Dashboard Design - Lovelace configurations
- Mobile Notifications - Alert systems

---

## 🚀 Kom i gang

### Forudsætninger
Før du kan køre eksemplerne skal du have:
- **ESP32** med sensorer tilsluttet
- **Arduino IDE** installeret og konfigureret
- **Python 3.8+** med nødvendige pakker
- **Node-RED** (for Node-RED eksempler)
- **Home Assistant** (for HA eksempler)

### Installation Guide
```bash
# Python dependencies
pip install pyserial matplotlib pandas numpy

# Optional for advanced examples
pip install influxdb-client paho-mqtt
```

### Hardware Setup
Standard sensor tilslutninger:
```
ESP32 Pin → Sensor
GPIO 4    → DHT22 Data
A0        → LDR (med 10kΩ pull-down)
A3        → Gas sensor
3.3V      → Sensor VCC
GND       → Sensor GND
```

---

## 📚 Eksempel Kategorier

### 🎯 Begynderniveau
**Mål:** Lær grundlæggende koncepter
- Serial communication basics
- Simpel sensor læsning
- Basic Python data processing

### 🔧 Intermediate niveau  
**Mål:** Kombiner teknologier
- Multi-platform integration
- Real-time visualization
- Error handling og robusthed

### 🚀 Avanceret niveau
**Mål:** Professionelle løsninger
- Scalable architecture
- Advanced automation
- Production-ready systems

---

## 💡 Sådan Bruger Du Eksemplerne

### 1. Start med Basics
- **Læs** README for hvert eksempel
- **Forstå** hardware requirements
- **Download** og test basic versioner først

### 2. Modificér og Eksperimentér
- **Ændr** sensor readings
- **Tilføj** nye features  
- **Kombiner** forskellige eksempler

### 3. Byg Videre
- **Brug** eksempler som templates
- **Integrer** i dine egne projekter
- **Del** forbedringer med klassen

---

## 🔧 Troubleshooting

### Almindelige Problemer

#### ESP32 Upload Fejl
```
Solution: Hold BOOT button during upload
Check: USB cable og driver installation
```

#### Python Import Errors
```bash
# Installer missing packages
pip install --upgrade [package-name]

# Check Python version
python --version  # Should be 3.8+
```

#### Node-RED Connection Issues
```
Check: ESP32 COM port i Node-RED settings
Verify: Baudrate matches (115200)
```

### Debug Tips
1. **Start simpelt** - test basic funktionalitet først
2. **Use Serial Monitor** - verificer ESP32 output
3. **Check connections** - loose wires er almindelige
4. **Isolation testing** - test hver komponent separat

---

## 📖 Dokumentation Standard

Alle eksempler følger denne struktur:
```
Eksempel-navn/
├── README.md           # Beskrivelse og setup guide
├── ESP32-Code/         # Arduino/ESP32 firmware
│   └── main.ino
├── Python-Code/        # Python applikationer
│   └── main.py
├── Node-RED-Flow/      # Node-RED flow exports
│   └── flow.json
├── Documentation/      # Detaljeret dokumentation
│   └── architecture.md
└── Screenshots/        # Billeder af resultater
    └── example.png
```

---

## 🤝 Bidrag og Forbedringer

### Rapporter Fejl
- **Beskrivelse** - hvad gik galt?
- **Steps to reproduce** - hvordan?
- **Environment** - OS, software versioner
- **Expected vs Actual** - hvad forventede du?

### Foreslå Forbedringer
- **Use cases** - hvornår ville det være nyttigt?
- **Implementation** - hvordan kunne det laves?
- **Benefits** - hvilke fordele giver det?

### Del Dine Eksempler
- **Follow documentation standard**
- **Test thoroughly** før deling
- **Include clear comments** i koden

---

*Disse eksempler er designet til læring og eksperimentering. Modificér, kombiner og byg videre på dem! 🚀*