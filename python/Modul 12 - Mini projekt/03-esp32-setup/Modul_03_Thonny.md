# 📄 Modul 3 (alternativ) – Opsætning af ESP32 med Thonny

## 🎯 Formål
Dette dokument guider dig gennem installation og brug af MicroPython på ESP32 ved hjælp af **Thonny IDE**, en grafisk udviklingsplatform velegnet til begyndere.

Denne metode er særlig god til undervisning, da den kræver minimal opsætning og har et simpelt brugerinterface.

---

## 🛠️ Forudsætninger

- ESP32 DevKit v1 eller lignende.
- USB-kabel med dataledninger.
- Windows, macOS eller Linux.
- [Thonny IDE](https://thonny.org/) installeret.
- MicroPython firmware til ESP32: [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)
- Driver til USB-seriel chip:
  - **CP210x**: [https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).
  - **CH340**: [https://sparks.gogo.co.nz/ch340.html](https://sparks.gogo.co.nz/ch340.html).

> Hvis ESP32 ikke dukker op i Thonny, skal du installere den relevante driver og genstarte din computer.

---

## 🧪 Trin 1: Installer Thonny

1. Gå til [https://thonny.org](https://thonny.org).
2. Vælg version til dit styresystem og installer.
3. Start Thonny og gå til `Værktøjer` → `Indstillinger`.

---

## ⚙️ Trin 2: Konfigurer fortolker (MicroPython)

1. Vælg fanen "Fortolker".
2. Vælg `MicroPython (ESP32)` i listen.
3. Vælg korrekt port (fx COM3 på Windows, `/dev/ttyUSB0` på Linux).
4. Tryk "OK".

> Hvis porten ikke vises: genstart Thonny eller kontroller driverinstallation

---

## 🔥 Trin 3: Installer MicroPython firmware

1. Gå til `Værktøjer` → `Installer MicroPython på et kort`.
2. Vælg `ESP32` som type.
3. Vælg den serielle port (COMx eller ttyUSBx).
4. Tryk på "Installer firmware".

> Thonny henter automatisk den nyeste MicroPython firmware og installerer den. Det tager ca. 20-30 sekunder.

Når installationen er færdig, vil terminalen i bunden vise MicroPython-prompten (`>>>`).

---

## 🧪 Testprogram – Blink med LED

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
while True:
    led.value(not led.value())
    sleep(0.5)
```

1. Skriv koden i Thonny.
2. Tryk "Kør" (grøn pil).
3. Hvis den indbyggede LED blinker, virker alt korrekt.

---

## 📝 Opgave

1. Installer Thonny og konfigurer fortolker.
2. Installer MicroPython på din ESP32 via Thonny.
3. Upload og kør blink-program.
4. Forbind sensorer til følgende pins:
   - DHT22 → GPIO14.
   - MQ2 → GPIO35 (analog).
   - LDR → GPIO34 (analog).
5. Dokumentér hele processen med noter og skærmbilleder.

## ✅ Output

- ESP32 programmeret med MicroPython.
- LED blinker.
- Sensorer forbundet og klar til brug.
- Thonny anvendes som udviklingsmiljø.

---

## 💡 Tips
- Brug "Gem som main.py" for at gøre programmet persistent efter genstart.
- Du kan bruge REPL-terminalen i bunden til at teste enkeltlinjer.
- Hvis du får fejlen `OSError: [Errno 5] EIO`, så genstart både Thonny og ESP32.

Med Thonny er du hurtigt i gang – og klar til at kode ESP32 med MicroPython!