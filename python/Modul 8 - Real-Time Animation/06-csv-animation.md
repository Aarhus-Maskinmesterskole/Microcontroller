# 📂 Modul 05: Animation af Sensor-Data fra CSV

## 📌 Hvad lærer du i dette modul?
✔️ Hvordan du **læser data fra en CSV-fil**  
✔️ Hvordan du **animerer sensor-data fra en fil**  
✔️ Hvordan du **opdaterer en graf i real-time baseret på lagrede data**  

---

## 📌 Trin 1: Opret en CSV-fil med sensor-data
For at kunne animere sensor-data, har vi brug for en **CSV-fil**, der indeholder temperatur- og fugtighedsmålinger.

📌 **Eksempel på `data.csv`**:
```csv
timestamp,temperature,humidity
2025-03-16 13:44:19,22.1,48.2
2025-03-16 13:44:20,22.2,48.3
2025-03-16 13:44:21,22.3,48.4
2025-03-16 13:44:22,22.2,48.3
2025-03-16 13:44:23,22.1,48.2
```

---

## 📌 Trin 2: Animering af CSV-data i Python
Nu laver vi en animation, hvor vi **læser data fra `data.csv`** og viser temperaturen i realtid.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Læs CSV-fil
data = pd.read_csv("data.csv")

fig, ax = plt.subplots()
ax.set_xlim(0, len(data))  # Tilpas x-akse
ax.set_ylim(data['temperature'].min() - 1, data['temperature'].max() + 1)

xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', label="Temperatur")

def init():
    ln.set_data([], [])
    return ln,

def update(frame):
    if frame < len(data):
        xdata.append(frame)
        ydata.append(data['temperature'].iloc[frame])
        ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(len(data)), init_func=init, interval=500, blit=False)

plt.legend()
plt.show()
```

---

## 🔥 Hvordan fungerer koden?
1️⃣ **Vi læser CSV-filen ind i en Pandas DataFrame:**  
   ```python
   data = pd.read_csv("data.csv")
   ```

2️⃣ **Vi sætter x- og y-aksen dynamisk efter antal rækker i CSV:**  
   ```python
   ax.set_xlim(0, len(data))
   ax.set_ylim(data['temperature'].min() - 1, data['temperature'].max() + 1)
   ```

3️⃣ **Vi definerer `update(frame)`, der henter én række fra CSV ad gangen:**  
   ```python
   def update(frame):
       if frame < len(data):
           xdata.append(frame)
           ydata.append(data['temperature'].iloc[frame])
           ln.set_data(xdata, ydata)
       return ln,
   ```

4️⃣ **Vi bruger `FuncAnimation()` til at opdatere plottet i real-time:**  
   ```python
   ani = FuncAnimation(fig, update, frames=range(len(data)), init_func=init, interval=500, blit=False)
   ```

5️⃣ **Vi tilføjer en forklaring med `plt.legend()`, så vi kan se, hvad grafen viser:**  
   ```python
   plt.legend()
   ```

---

## ✅ Opgaver
1️⃣ Kør koden og se temperaturgrafen opdatere sig fra CSV.  
2️⃣ Tilføj en **blå linje for fugtighedsmålinger**.  
3️⃣ Prøv at **ændre `interval=200`** – hvordan ændrer det animationen?  
4️⃣ Gem animationen som en **GIF**.  

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
