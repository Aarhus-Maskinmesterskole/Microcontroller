# 📈 Modul 03 – Real-tids Plot fra ESP32 med Python

I dette modul lærer du at læse realtidsdata fra din ESP32 via seriel port og visualisere det med det samme i et opdaterende plot. Det giver dig mulighed for at observere ændringer i dine sensordata live.

---

## 🎯 Læringsmål

✔️ Læse seriel data fra ESP32 i realtid med `pyserial`  
✔️ Parse CSV-linjer direkte fra seriel porten  
✔️ Plotte realtidsdata med `matplotlib.animation`  
✔️ Anvende glidende gennemsnit live (valgfrit)

---

## 🔧 Trin 1 – Tilslut ESP32 og installer bibliotek

Sørg for, at din ESP32 kører `main.py` fra Modul 01 og sender data i CSV-format.

Installer `pyserial` hvis du ikke har det:
```bash
pip install pyserial
```

---

## 🧪 Trin 2 – Realtidsplot i Python

Opret en fil `realtime_plot.py` og indsæt følgende eksempel:

```python
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Justér til din port (fx COM3 på Windows eller /dev/ttyUSB0 på Linux)
ser = serial.Serial('/dev/ttyUSB0', 115200)

x_data, y_data = [], []

fig, ax = plt.subplots()
line, = ax.plot([], [], label="Temperatur")

# Initialiser graf
def init():
    ax.set_xlim(0, 10000)
    ax.set_ylim(15, 35)
    ax.set_xlabel("Tid (ms)")
    ax.set_ylabel("Temperatur")
    ax.set_title("Live Temperatur fra ESP32")
    ax.legend()
    return line,

# Opdater funktion
def update(frame):
    try:
        raw = ser.readline().decode().strip()
        parts = raw.split(',')
        if len(parts) >= 2:
            t = int(parts[0])
            temp = float(parts[1])
            x_data.append(t)
            y_data.append(temp)
            line.set_data(x_data, y_data)
            ax.set_xlim(max(0, t - 10000), t + 1000)
    except:
        pass
    return line,

ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=200)
plt.show()
```

---

## 💡 Tips

- Brug `print()` til fejlfinding, hvis du ikke får data.
- Hvis du får fejl om port: tjek at ESP32 er tilsluttet og at COM-porten er korrekt.
- Du kan justere `ax.set_ylim()` og `set_xlim()` alt efter dine værdier.

---

## 🔁 Din opgave

1. Forbind ESP32 og start programmet  
2. Bekræft at du får en live temperaturgraf  
3. Tilføj et ekstra plot for `humidity`  
4. *(Valgfrit)* Implementér glidende gennemsnit direkte i `update()`

---

✅ Når du har styr på realtidsvisning, er du klar til at kombinere det hele i et mini-projekt i [`04_projekt`](../04_projekt/)!

