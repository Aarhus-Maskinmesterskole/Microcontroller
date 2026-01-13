# 🎬 Modul 01: Introduktion til Animationer

## 📌 Hvad er `FuncAnimation`?
Matplotlib er normalt et **statisk** bibliotek, men `FuncAnimation` gør det muligt at opdatere plots **i realtid**.  
Vi kan bruge det til at **visualisere dynamiske data**, f.eks. sensormålinger.

---

## 🎯 Hvad lærer du i dette modul?
✔️ Hvad `FuncAnimation` er, og hvordan det fungerer  
✔️ Hvordan en animation opdaterer et plot løbende  
✔️ Hvordan vi kan bruge animationer til at vise real-time data  

---

## 📌 Hvordan fungerer `FuncAnimation`?
Tænk på `FuncAnimation` som en **automatisk loop**, der **gentager en funktion flere gange** for at opdatere plottet.
```python
FuncAnimation(fig, update, frames, init_func, interval)
`````

| **Parameter** | **Beskrivelse** |
|--------------|----------------|
| `fig` | Figuren (hele plottet), der skal animeres |
| `update` | Funktionen, der opdaterer plottet for hver frame |
| `frames` | Hvor mange gange `update()` skal kaldes |
| `init_func` | Funktion, der initialiserer plottet |
| `interval` | Hvor lang tid (ms) der går mellem hver opdatering |

---

## 🔹 Eksempel: Simpel Animation af en Bevægende Prik
Denne kode viser en **rød prik**, der bevæger sig på x-aksen:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur og akse
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # X-akse område
ax.set_ylim(0, 10)  # Y-akse område

# Opret lister til data
xdata, ydata = [], []

# Opret en rød prik, der skal animeres
ln, = ax.plot([], [], 'ro')

def init():
    ln.set_data([], [])
    return ln,

def update(frame):
    xdata.append(frame)  # Tilføj ny x-værdi
    ydata.append(np.random.uniform(0, 10))  # Tilføj ny y-værdi
    ln.set_data(xdata, ydata)  # Opdater plottet
    return ln,

# Opret animation
ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, blit=True)

# Vis animation
plt.show()
```

---

## 🔥 Hvad sker der her?
1️⃣ `init()` **nulstiller plottet**.  
2️⃣ `update(frame)` **opdaterer prikken** ved at tilføje nye x- og y-værdier.  
3️⃣ `FuncAnimation(fig, update, frames=10, interval=500)` **gentager `update()` 10 gange**.

---

## ✅ Opgaver
1️⃣ Kør koden og se animationen.  
2️⃣ Prøv at **ændre intervallet** – hvad sker der?  
3️⃣ Tilføj en **grøn prik**, der bevæger sig hurtigere.

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
