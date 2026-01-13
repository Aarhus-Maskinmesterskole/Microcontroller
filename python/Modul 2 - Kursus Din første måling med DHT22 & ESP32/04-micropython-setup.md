# 🛠️ Modul 2.4: Opsætning af MicroPython på ESP32

## 📌 **Introduktion**
Før vi kan begynde at måle temperatur og luftfugtighed med DHT22, skal vi installere **MicroPython** på ESP32 og konfigurere Thonny som vores udviklingsmiljø. 

🔗 **Forrige modul:** [01-hardware-setup.md](01-hardware-setup.md)  
🔜 **Næste modul:** [03-install-dht-library.md](03-install-dht-library.md)  

---

## 🛠️ **Krav før installation**
✅ **ESP32-board** (eller ESP8266)  
✅ **USB-kabel (dataoverførsel, ikke kun opladning!)**  
✅ **Thonny installeret** ([Hent her](https://thonny.org/))  
✅ **MicroPython firmware** (skal downloades)  

---

## 📥 **Trin 1: Download MicroPython til ESP32**
1. Gå til den officielle MicroPython-side:  
   🔗 [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)  
2. Vælg den nyeste `.bin`-fil for **ESP32** (fx `esp32-2024xxxx-v1.20.bin`).  
3. Gem filen på din computer (fx i `Downloads`-mappen).

---

## 🔌 **Trin 2: Installer MicroPython på ESP32**
Vi bruger **esptool.py** til at installere firmwaren på ESP32.

### 📦 **Installer esptool**
Åbn en **terminal/kommandoprompt** og kør:
```bash
pip install esptool
```
## 🏭 Slet tidligere firmware (valgfrit, men anbefales)

esptool.py --port COM3 erase_flash

(Erstat COM3 med den port, som din ESP32 bruger – se næste trin for hjælp til at finde den.)

## 📲 Flash MicroPython til ESP32

esptool.py --port COM3 --baud 460800 write_flash -z 0x1000 esp32-2024xxxx-v1.20.bin

(Udskift esp32-2024xxxx-v1.20.bin med navnet på din downloadede firmwarefil.)

💡 Tip: Hvis du får fejl, så prøv at holde BOOT-knappen på ESP32 nede, mens du flasher.   
🔎 Trin 3: Find din ESP32’s COM-port

Før vi forbinder til Thonny, skal vi finde den rigtige COM-port.

## 🖥️ Windows
- Tryk Win + X → Enhedshåndtering
- Find "USB-to-Serial" under Porte (COM & LPT)
- Notér COM-portnummeret (fx COM3).

## 🖥️ Mac/Linux
Brug terminalen:
```terminal
ls /dev/ttyUSB*
```

Typisk vil den hedde noget som /dev/ttyUSB0 eller /dev/tty.SLAB_USBtoUART.

## 🏗️ Trin 4: Opsæt Thonny med MicroPython
1. Åbn Thonny
2. Gå til Tools → Options
3. Vælg Interpreter
4. Vælg "MicroPython (ESP32)"
5. Vælg COM-porten du fandt tidligere
6. Klik OK, og åbn Shell-vinduet nederst

✅ Hvis alt virker, ser du MicroPython-prompten:

```python
MicroPython v1.20 on 2024-xx-xx; ESP32 module
>>> _
```

(Prompten >>> betyder, at ESP32 er klar til at modtage MicroPython-kommandoer!)

## 📝 Test, at alt fungerer
For at sikre, at installationen er korrekt, kan du køre:
```python
print("Hello from ESP32!")
```

Hvis Hello from ESP32! vises i Shell, er alt sat op korrekt. ✅

## 🚀 Næste skridt
Vi er nu klar til at installere DHT22-biblioteket og begynde at måle temperatur og luftfugtighed!
🔜 Fortsæt til næste modul:
📄 03-install-dht-library.md
