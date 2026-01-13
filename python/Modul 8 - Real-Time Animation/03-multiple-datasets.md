# 🔵 Modul 03: Animation af Flere Datasæt

## 📌 Hvad lærer du i dette modul?
✔️ Hvordan du **animerer flere datasæt samtidig**  
✔️ Hvordan du **tilføjer flere grafer i samme animation**  
✔️ Hvordan du **opdaterer flere linjer i real-time**  

---

## 📌 Trin 1: Opret en Animation med Flere Prikker
Nu laver vi en animation med **to prikker** – en **rød og en blå**.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur og akse
fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Opret to prikker: rød og blå
ln1, = ax.plot([], [], 'ro', label="Prik 1")
ln2, = ax.plot([], [], 'bo', label="Prik 2")

xdata, y1data, y2data = [], [], []

def init():
    ln1.set_data([], [])
    ln2.set_data([], [])
    return ln1, ln2

def update(frame):
    xdata.append(frame)
    y1data.append(np.random.uniform(0, 10))
    y2data.append(np.random.uniform(0, 10))
    ln1.set_data(xdata, y1data)
    ln2.set_data(xdata, y2data)
    return ln1, ln2

# Opret animation
ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, blit=True)

# Vis legend og animation
plt.legend()
plt.show()
```

---

## 🔥 Hvordan fungerer koden?
1️⃣ **Vi opretter en figur og en akse:**  
   ```python
   fig, ax = plt.subplots()
   ```

2️⃣ **Vi laver to prikker:**  
   ```python
   ln1, = ax.plot([], [], 'ro', label="Prik 1")  # Rød prik
   ln2, = ax.plot([], [], 'bo', label="Prik 2")  # Blå prik
   ```

3️⃣ **Vi definerer `init()`, der nulstiller begge prikker:**  
   ```python
   def init():
       ln1.set_data([], [])
       ln2.set_data([], [])
       return ln1, ln2
   ```

4️⃣ **Vi definerer `update(frame)`, der opdaterer begge prikker:**  
   ```python
   def update(frame):
       x = frame
       y1 = np.random.uniform(0, 10)  # Tilfældig y-værdi for rød prik
       y2 = np.random.uniform(0, 10)  # Tilfældig y-værdi for blå prik
       ln1.set_data(x, y1)
       ln2.set_data(x, y2)
       return ln1, ln2
   ```

5️⃣ **Vi opretter en animation med `FuncAnimation()`**, der animerer begge prikker:  
   ```python
   ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, blit=True)
   ```

6️⃣ **Vi tilføjer en forklaring med `plt.legend()`**, så vi kan se hvilken prik der er hvilken:  
   ```python
   plt.legend()
   ```

---

## ✅ Opgaver
1️⃣ Kør koden og se animationen.  
2️⃣ Prøv at **ændre `interval=200`** – hvad sker der?  
3️⃣ Tilføj en **tredje prik (grøn)**, der bevæger sig hurtigere end de andre.  

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
