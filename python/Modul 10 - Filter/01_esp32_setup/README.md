# ⚙️ Modul 01 – ESP32 Setup og Seriel Data i CSV-format (MicroPython)

I dette modul lærer du at opsætte din ESP32 med MicroPython, så den sender seriel data i CSV-format, som du senere skal filtrere og visualisere i realtid med Python.

---

## 🎯 Læringsmål

✔️ Installere MicroPython på ESP32  
✔️ Bruge Thonny eller VS Code til at skrive og uploade kode  
✔️ Skrive MicroPython-kode, der sender CSV-format data via seriel port  
✔️ Verificere seriel output i terminal eller Python

---

## 🧰 Trin 1 – Installér MicroPython på ESP32

1. Gå til [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)  
2. Download den nyeste firmware (`.bin`-fil) til ESP32
3. Brug **Thonny** til at installere firmwaren:
   - Tilslut ESP32 med USB
   - Gå til `Værktøjer > MicroPython (ESP32)`
   - Vælg port og tryk på "Installér eller opgrader firmware"

---

## 📝 Trin 2 – Skriv MicroPython-kode

Åbn Thonny eller brug `mpremote` med din foretrukne editor. Indsæt følgende kode:

```python
from time import sleep_ms, ticks_ms
from random import uniform
from machine import Pin

while True:
    timestamp = ticks_ms()
    temp = round(uniform(20.0, 30.0), 1)       # Simuleret temperatur
    humidity = round(uniform(40.0, 70.0), 1)   # Simuleret fugtighed

    print(f"{timestamp},{temp},{humidity}")
    sleep_ms(500)
```

💡 Denne kode sender hver 500 ms et linjeskift med `timestamp, temperatur, fugtighed` i CSV-format.

---

## 🧪 Trin 3 – Test output

1. Kør scriptet i Thonny, og se output i bunden af editoren.
2. Alternativt, brug `mpremote` fra terminal:

```bash
mpremote run main.py
```

Du bør se noget lignende:
```
512,22.5,56.1
1012,22.7,55.8
1512,22.8,56.2
```

✅ Dette er CSV-output med 3 kolonner: `timestamp`, `temperature`, `humidity`.

---

## 💾 Trin 4 – Gem scriptet på ESP32 (valgfrit)

Hvis du vil have scriptet til at starte automatisk:

1. Gem filen som `main.py`
2. Brug Thonny eller `mpremote fs cp main.py :main.py`

---

## 🔁 Din opgave

1. Flash MicroPython på din ESP32 (hvis du ikke har gjort det før)  
2. Kør og forstå koden ovenfor  
3. Tilpas data eller forsøg at tilføje en rigtig sensor (DHT22, analog input, mv.)  
4. Bekræft, at dine data vises i CSV-format

---

## 🧠 Brug for hjælp?

- MicroPython dokumentation: [https://docs.micropython.org](https://docs.micropython.org)
- Brug `print()` til fejlfinding
- Spørg underviser eller medstuderende

---

✅ Klar til næste trin? Gå videre til [`02_csv_filtrering`](../02_csv_filtrering/) og begynd at analysere dine data i Python!

