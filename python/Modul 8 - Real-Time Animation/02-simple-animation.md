# 🔴 Modul 02: Simpel Animation af en Bevægende Prik

## 📌 Hvad lærer du i dette modul?
✔️ Hvordan du opretter en **simpel animation**  
✔️ Hvordan du **opdaterer et plot i realtid**  
✔️ Hvordan du **forbinder animation til data**  

---

## 📌 Trin 1: Opret en Simpel Animation
I dette eksempel laver vi en **rød prik, der bevæger sig** på x-aksen.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur og akse
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # X-akse interval
ax.set_ylim(0, 10)  # Y-akse interval

# Opret en rød prik, der skal animeres
ln, = ax.plot([], [], 'ro')

# Opretter lister for de to akser
xdata, ydata = [], []

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

## 🔥 Hvordan fungerer koden?
1️⃣ **Vi opretter en figur og en akse:**  
   ```python
   # Opret figur og akse
   fig, ax = plt.subplots()
   ax.set_xlim(0, 10)  # X-akse interval
   ax.set_ylim(0, 10)  # Y-akse interval
   ```

2️⃣ **Vi laver en rød prik og opretter to lister:**  
   ```python
    
    # Opret en rød prik, der skal animeres
    ln, = ax.plot([], [], 'ro')
    
    # Opretter lister for de to akser
    xdata, ydata = [], []
   ```

3️⃣ **Vi definerer `init()`, der nulstiller plottet:**  
   ```python
   def init():
       ln.set_data([], [])
       return ln,
   ```

4️⃣ **Vi definerer `update(frame)`, der opdaterer prikken:**  
   ```python
    def update(frame):
        xdata.append(frame)  # Tilføj ny x-værdi
        ydata.append(np.random.uniform(0, 10))  # Tilføj ny y-værdi
        ln.set_data(xdata, ydata)  # Opdater plottet
        return ln,
   ```

5️⃣ **Vi opretter en animation med `FuncAnimation()`, der kalder `update()` 10 gange:**  
   ```python
   ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, blit=True)
   ```

---

## ✅ Opgaver
1️⃣ Kør koden og se animationen.  
2️⃣ Prøv at **ændre `interval=200`** – hvad sker der?  
3️⃣ Tilføj en **grøn prik**, der bevæger sig hurtigere.  

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
