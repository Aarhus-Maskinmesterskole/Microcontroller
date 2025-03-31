# 🛠️ Installation af MicroPython på ESP32

I dette modul installerer vi MicroPython på din ESP32 og forbinder den til din PC, så du kan skrive og køre Python-kode direkte på den.

---

## 📦 Krav og forberedelse

### Hardware
- ESP32 (alle modeller med WiFi understøttes)
- USB-kabel (USB-C eller micro-USB afhængigt af model)

### Software
- [Thonny](https://thonny.org/) (anbefalet IDE)
- Alternativ: `mpremote`, `rshell` eller `ampy`
- [MicroPython firmware til ESP32](https://micropython.org/download/esp32/)

---

## 🔥 Flash MicroPython på ESP32

1. Slut ESP32 til din PC med USB
2. Installer `esptool` hvis nødvendigt:
```bash
pip install esptool
```
3. Find din COM-port:
   - Windows: Enhedshåndtering → Porte (fx COM5)
   - Mac/Linux: `ls /dev/ttyUSB*` eller `ls /dev/tty.SLAB*`
4. Slet eksisterende firmware (valgfrit, men anbefalet):
```bash
esptool.py --port COM5 erase_flash
```
5. Flash MicroPython-firmware:
```bash
esptool.py --chip esp32 --port COM5 --baud 460800 write_flash -z 0x1000 micropython.bin
```
Udskift `COM5` med din port og `micropython.bin` med den firmwarefil du har downloadet.

---

## 🧪 Test med Thonny
1. Åbn Thonny og vælg:
   - Kør → Vælg fortolker → MicroPython (ESP32)
   - Port: COM5 (eller hvad du bruger)
2. Klik **Kør** eller skriv i REPL:
```python
print("ESP32 kører MicroPython!")
```

---

## 📁 Upload Python-filer til ESP32
Du kan nu bruge Thonny eller `mpremote` til at overføre og afvikle scripts:
```bash
mpremote connect COM5 fs ls
mpremote connect COM5 run main.py
```

---

Nu er din ESP32 klar til at køre MicroPython og kommunikere via netværk! I næste modul: `03-modbus-client.md` begynder vi at sende Modbus TCP-forespørgsler fra ESP32 🚀
