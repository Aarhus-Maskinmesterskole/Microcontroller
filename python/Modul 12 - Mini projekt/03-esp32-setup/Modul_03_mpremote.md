# 📄 Modul 3 (alternativ) – Opsætning af ESP32 med mpremote

## 🎯 Formål
Dette dokument guider dig gennem installation og brug af MicroPython på ESP32 ved hjælp af `mpremote`, et terminalbaseret værktøj til MicroPython.

Denne metode er særligt nyttig, hvis du arbejder med Linux, WSL, macOS eller foretrækker kommandolinje frem for IDE.

---

## 🛠️ Forudsætninger

- ESP32 DevKit v1 eller lignende.
- USB-kabel med dataledninger.
- Python 3.x installeret.
- MicroPython firmware til ESP32: [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/).
- Driver til USB-seriel chip:
  - **CP210x**: [https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
  - **CH340**: [https://sparks.gogo.co.nz/ch340.html](https://sparks.gogo.co.nz/ch340.html)

> Hvis din ESP32 ikke bliver genkendt som en COM-port, mangler du højst sandsynligt en af disse drivere.

- ESP32 WROOM eller lignende.
- USB-kabel med dataledninger.
- Python 3.x installeret.
- MicroPython firmware til ESP32: [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/).

---

## 🧪 Trin 1: Installer esptool og mpremote
```bash
pip install esptool mpremote
```

## 🧪 Trin 2: Find COM-port
Find din ESP32 port:
- Windows: Enhedshåndtering (fx COM3).
- macOS/Linux: `ls /dev/ttyUSB*` eller `ls /dev/tty.*`.

---

## 🔥 Trin 3: Flash MicroPython firmware

1. Slet eksisterende firmware:
```bash
esptool.py --port COM3 erase_flash
```
2. Flash den nye firmware (skift `esp32-*.bin` ud med din fil):
```bash
esptool.py --chip esp32 --port COM3 write_flash -z 0x1000 esp32-2023*.bin
```

---

## 🔌 Trin 4: Forbind med mpremote

Test at MicroPython virker:
```bash
#Windows: COM3, Linux: ttyUSB0
mpremote connect COM3
>>> print("Hello fra ESP32")
```

### Udforsk filsystem
```bash
#Windows: COM3, Linux: ttyUSB0
mpremote connect COM3 fs ls
```

### Upload kodefil
```bash
#Windows: COM3, Linux: ttyUSB0
mpremote connect COM3 fs cp blink.py :main.py
```

### Kør program uden at gemme det
```bash
#Windows: COM3, Linux: ttyUSB0
mpremote connect COM3 run blink.py
```

---

## 🧪 Testprogram: blink.py

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
while True:
    led.value(not led.value())
    sleep(0.5)
```

Gem denne som `blink.py` og kør med mpremote. LED bør blinke hvert 0.5 sekund.

---

## 📝 Opgave
1. Installer MicroPython med `esptool`.
2. Brug `mpremote` til at teste og uploade blink-kode.
3. Forbind sensorer til GPIO-pins:
   - DHT22 til IO14.
   - MQ2 til IO35.
   - LDR til IO34.
4. Dokumentér hele processen (inkl. skærmbilleder og pinouts).

## ✅ Output
- ESP32 kører MicroPython.
- LED blinker.
- Sensorer er forbundet.
- mpremote bruges til upload og interaktion.

---

## 💡 Tips
- Brug `mpremote connect <port> repl` til interaktiv terminal.
- Brug `Ctrl+A Ctrl+D` for at slippe forbindelsen (eller `exit()`).
- Du kan bruge `--help` til alle mpremote-kommandoer.

Med `mpremote` har du fuld terminalbaseret kontrol over din ESP32!

