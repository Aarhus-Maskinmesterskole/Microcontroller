# 🛠️ Arduino IDE Setup Guide til ESP32
**Installation og konfiguration af udviklingsenvironment**

## 🎯 Oversigt
Denne guide hjælper dig med at installere og konfigurere Arduino IDE til ESP32 udvikling. Arduino IDE er den mest brugervenlige måde at programmere ESP32 på og er perfekt til undervisningsbrug.

---

## 📥 Del 1: Arduino IDE Installation

### 1.1 Download Arduino IDE
1. **Gå til:** [arduino.cc/software](https://www.arduino.cc/en/software)
2. **Vælg:** Arduino IDE 2.0 eller nyere (anbefalet)
3. **Download** til dit operativsystem:
   - **Windows:** Arduino IDE 2.x.x Win32/Win64
   - **macOS:** Arduino IDE 2.x.x macOS
   - **Linux:** Arduino IDE 2.x.x Linux64

### 1.2 Installation Process

#### Windows:
1. **Kør** den downloadede `.exe` fil
2. **Acceptér** license agreement
3. **Vælg** installation directory (standard er OK)
4. **Vent** på installation completion
5. **Start** Arduino IDE fra Start Menu

#### macOS:
1. **Åbn** den downloadede `.dmg` fil
2. **Træk** Arduino IDE til Applications folder
3. **Start** Arduino IDE fra Applications

#### Linux:
1. **Udpak** den downloadede `.tar.xz` fil
2. **Kør** `install.sh` script som administrator
3. **Start** Arduino IDE fra applications menu

### 1.3 Første Opstart
Ved første opstart:
1. **Acceptér** privacy policy
2. **Tillad** firewall adgang (hvis spurgt)
3. **Verificér** at IDE starter korrekt

---

## 🔧 Del 2: ESP32 Board Support

### 2.1 Tilføj ESP32 Board Manager URL
1. **Åbn** Arduino IDE
2. **Gå til:** File → Preferences (Ctrl+Comma)
3. **Find:** "Additional boards manager URLs" feltet
4. **Tilføj:** `https://dl.espressif.com/dl/package_esp32_index.json`
   - Hvis der allerede er andre URLs, tilføj komma og denne URL
5. **Klik:** OK

### 2.2 Installer ESP32 Platform
1. **Åbn:** Tools → Board → Board Manager
2. **Søg:** "esp32"
3. **Find:** "esp32 by Espressif Systems"
4. **Klik:** Install
5. **Vent** på download og installation (kan tage 5-10 minutter)
6. **Verificér:** At installation er komplet

### 2.3 Vælg ESP32 Board
1. **Gå til:** Tools → Board
2. **Udvid:** ESP32 Arduino sektion
3. **Vælg:** "ESP32 Dev Module" (fungerer til de fleste ESP32 boards)

---

## 🔌 Del 3: USB Driver Installation

### 3.1 Identificér Din ESP32's USB Chip
ESP32 boards bruger typisk en af disse USB-serial chips:
- **CP2102/CP2104** (Silicon Labs)
- **CH340G** (WCH)
- **FTDI** (mindre almindelig)

### 3.2 Download og Installer Drivers

#### CP210x Drivers (Mest almindelig):
1. **Gå til:** [Silicon Labs CP210x Downloads](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
2. **Download** til dit OS
3. **Installer** følgende instruktioner

#### CH340 Drivers:
1. **Gå til:** [WCH CH340 Downloads](http://www.wch-ic.com/downloads/CH341SER_ZIP.html)
2. **Download** og installer

#### Automatisk Driver Installation:
- **Windows 10/11:** Prøv at tilslutte ESP32 først - Windows installerer ofte automatisk
- **macOS:** Moderne versioner har ofte built-in support
- **Linux:** De fleste distributioner har drivers inkluderet

### 3.3 Verificér Driver Installation
1. **Tilslut** ESP32 til computer via USB
2. **Åbn** Device Manager (Windows) eller System Information (macOS/Linux)
3. **Find** ESP32 under "Ports (COM & LPT)" som f.eks.:
   - "Silicon Labs CP210x USB to UART Bridge (COM3)"
   - "USB-SERIAL CH340 (COM5)"

---

## 🧪 Del 4: Test Installation

### 4.1 Første Test Program
Kopiér denne kode til Arduino IDE:

```cpp
void setup() {
  // Initialiser serial kommunikation
  Serial.begin(115200);
  
  // Konfigurer built-in LED
  pinMode(2, OUTPUT);
  
  Serial.println("ESP32 Test - LED Blink");
  Serial.println("Arduino IDE Setup Complete!");
}

void loop() {
  digitalWrite(2, HIGH);   // Tænd LED
  Serial.println("LED ON");
  delay(1000);             // Vent 1 sekund
  
  digitalWrite(2, LOW);    // Sluk LED
  Serial.println("LED OFF");
  delay(1000);             // Vent 1 sekund
}
```

### 4.2 Upload Process
1. **Vælg korrekt port:** Tools → Port → [Dit ESP32's COM port]
2. **Klik:** Upload knappen (→)
3. **Observer:** Compilation og upload progress
4. **Hvis fejl:** Tryk og hold "BOOT" knappen på ESP32 under upload

### 4.3 Verificér Funktionalitet
1. **LED test:** Built-in LED skal blinke hver sekund
2. **Serial output:** Åbn Serial Monitor (Ctrl+Shift+M)
   - Sæt baudrate til 115200
   - Du skal se "LED ON/OFF" beskeder

---

## 🔧 Del 5: Arduino IDE Konfiguration

### 5.1 ESP32 Board Settings
Anbefalet konfiguration (Tools menu):
- **Board:** ESP32 Dev Module
- **Upload Speed:** 921600
- **CPU Frequency:** 240MHz (WiFi/BT)
- **Flash Frequency:** 80MHz
- **Flash Mode:** QIO
- **Flash Size:** 4MB (32Mb)
- **Partition Scheme:** Default 4MB with spiffs

### 5.2 IDE Indstillinger
Optimér IDE for ESP32 udvikling:
1. **File → Preferences:**
   - ✅ Display line numbers
   - ✅ Enable code folding
   - ✅ Verify code after upload
   - **Editor font size:** 12-14 (juster efter præference)

### 5.3 Nyttige Genveje
- **Ctrl+R:** Verify/Compile
- **Ctrl+U:** Upload
- **Ctrl+Shift+M:** Serial Monitor
- **Ctrl+T:** Auto Format
- **Ctrl+/:** Comment/Uncomment

---

## 📚 Del 6: Biblioteker og Værktøjer

### 6.1 Essential Biblioteker
Installer via Library Manager (Tools → Manage Libraries):

**Sensorer:**
- **DHT sensor library** by Adafruit
- **Adafruit Unified Sensor**

**Display:**
- **U8g2** (til OLED displays)
- **TFT_eSPI** (til TFT displays)

**Kommunikation:**
- **WiFi** (included med ESP32)
- **ArduinoJson** (til JSON parsing)

### 6.2 Installér Bibliotek
1. **Åbn:** Tools → Manage Libraries
2. **Søg:** bibliotek navn
3. **Klik:** Install
4. **Vælg:** seneste version

### 6.3 Serial Monitor Setup
Optimér Serial Monitor til debugging:
- **Baudrate:** 115200 (standard for ESP32)
- **Line ending:** Both NL & CR
- **Autoscroll:** ✅ (til kontinuerlig output)

---

## ⚠️ Troubleshooting

### 📡 Upload Problemer

#### "Failed to connect to ESP32"
**Løsninger:**
1. **Check USB kabel** - nogle kabler er kun til opladning
2. **Tryk BOOT knap** under upload process
3. **Verificér COM port** i Device Manager
4. **Prøv lavere upload speed** (115200)

#### "Permission denied" (Linux/macOS)
```bash
# Tilføj bruger til dialout group
sudo usermod -a -G dialout $USER
# Log ud og ind igen
```

### 🔌 Port Detection Problemer

#### Windows - Driver Issues
1. **Uninstall** current driver i Device Manager
2. **Disconnect** ESP32
3. **Reinstall** korrekt driver
4. **Reconnect** ESP32

#### "Port not found"
1. **Check USB connection**
2. **Try different USB port**
3. **Restart Arduino IDE**
4. **Restart computer** (sidste udvej)

### 💾 Compilation Errors

#### "Board not found"
- **Verificér** ESP32 platform er installeret
- **Restart** Arduino IDE
- **Reinstallér** ESP32 platform hvis nødvendigt

#### "Library not found"
- **Check** library er installeret korrekt
- **Verificér** #include statements
- **Reinstallér** missing libraries

---

## ✅ Installation Checklist

### ☑️ Software Installation
- [ ] Arduino IDE 2.0+ downloadet og installeret
- [ ] ESP32 board manager URL tilføjet
- [ ] ESP32 platform installeret via Board Manager
- [ ] ESP32 Dev Module valgt som board

### ☑️ Hardware Setup
- [ ] USB driver installeret og fungerer
- [ ] ESP32 detekteres som COM port
- [ ] Korrekt COM port valgt i Arduino IDE

### ☑️ Functionality Test
- [ ] Test program uploader succesfuldt
- [ ] Built-in LED blinker
- [ ] Serial Monitor viser output korrekt
- [ ] Baudrate sat til 115200

### ☑️ Library Setup
- [ ] DHT sensor library installeret
- [ ] Essential biblioteker tilgængelige
- [ ] Library Manager fungerer korrekt

---

## 🔗 Nyttige Ressourcer

### Dokumentation
- **ESP32 Arduino Core:** [github.com/espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
- **ESP32 Datasheet:** [espressif.com/documentation](https://www.espressif.com/en/support/documentation/technical-documents)
- **Arduino Reference:** [arduino.cc/reference](https://www.arduino.cc/reference/en/)

### Community Support
- **Arduino Forum:** [forum.arduino.cc](https://forum.arduino.cc/)
- **ESP32 Community:** [esp32.com](https://esp32.com/)
- **Reddit:** r/esp32, r/arduino

### Video Tutorials
- Search for "ESP32 Arduino IDE setup" på YouTube
- Adafruit og SparkFun har gode tutorials

---

## 🎯 Næste Skridt

Nu hvor dit setup er komplet:
1. **Eksperimentér** med test programmet
2. **Modificér** blink hastighed og Serial output
3. **Forbered** dig til sensor integration i næste lektion
4. **Gem** dine projekter i organiserede mapper

**Tillykke! Du har nu et fuldt funktionelt ESP32 udviklingsenvironment! 🎉**

---

*Hvis du støder på problemer ikke covered i denne guide, så spørg i klassen eller check troubleshooting sektionen igen. De fleste problemer skyldes drivers eller kabel issues.*