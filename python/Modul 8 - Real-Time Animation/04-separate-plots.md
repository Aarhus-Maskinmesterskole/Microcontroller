# 🖼️ Modul 04: Separate Plots i Subplots

## 📌 Hvad lærer du i dette modul?
✔️ Hvordan du **opretter flere separate plots (subplots)**  
✔️ Hvordan du **animerer flere datasæt i forskellige plots samtidig**  
✔️ Hvordan du **håndterer aksebegrænsninger og labels for hvert subplot**  

---

## 📌 Trin 1: Opret en animation med separate plots
I dette eksempel laver vi en animation, hvor **temperatur og fugtighed vises i separate subplots**.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur med to subplots (1 række, 2 kolonner)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Indstil aksegrænser
ax1.set_xlim(0, 10)
ax1.set_ylim(20, 30)
ax1.set_title("Temperatur")

ax2.set_xlim(0, 10)
ax2.set_ylim(40, 60)
ax2.set_title("Fugtighed")

# Opret linjer for temperatur og fugtighed i hvert subplot
ln1, = ax1.plot([], [], 'ro', label="Temperatur")
ln2, = ax2.plot([], [], 'bo', label="Fugtighed")

xdata, temp_data, hum_data = [], [], []

def init():
    ln1.set_data([], [])
    ln2.set_data([], [])
    return ln1, ln2

def update(frame):
    xdata.append(frame)
    temp_data.append(22 + np.random.normal(0, 0.5))  # Simuleret temperatur
    hum_data.append(50 + np.random.normal(0, 2))  # Simuleret fugtighed

    ln1.set_data(xdata, temp_data)
    ln2.set_data(xdata, hum_data)
    return ln1, ln2

# Opret animation
ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, blit=False)

plt.legend()
plt.tight_layout()
plt.show()
```

---

## 🔥 Hvordan fungerer koden?
1️⃣ **Vi opretter en figur med to separate subplots**:  
   ```python
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
   ```
   - `ax1` bruges til **temperatur**
   - `ax2` bruges til **fugtighed**

2️⃣ **Vi sætter forskellige aksegrænser for hvert subplot**:  
   ```python
   ax1.set_xlim(0, 10)
   ax1.set_ylim(20, 30)
   ax2.set_xlim(0, 10)
   ax2.set_ylim(40, 60)
   ```

3️⃣ **Vi definerer `update(frame)`, der opdaterer hvert subplot individuelt**:  
   ```python
   temp_data.append(22 + np.random.normal(0, 0.5))  # Temperatur
   hum_data.append(50 + np.random.normal(0, 2))  # Fugtighed
   ln1.set_data(xdata, temp_data)
   ln2.set_data(xdata, hum_data)
   ```

4️⃣ **Vi opretter en animation med `FuncAnimation()`**, der opdaterer begge plots:  
   ```python
   ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, blit=False)
   ```

---

## ✅ Opgaver
1️⃣ Kør koden og se animationen med to separate plots.  
2️⃣ Prøv at **ændre `interval=200`** – hvad sker der?  
3️⃣ Tilføj en **tredje subplot for lufttryk** (`ax3`).  
4️⃣ Eksperimentér med **forskellige skalaer** for at se, hvordan det påvirker læsbarheden.  

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
