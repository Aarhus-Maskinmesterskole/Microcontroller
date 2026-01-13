# 🌡️ Modul 04: Real-Time Temperaturmåling (Simuleret)

## 📌 Hvad lærer du i dette modul?
✔️ Hvordan du **animerer temperaturdata i realtid**  
✔️ Hvordan du **holder grafen opdateret med nye målinger**  
✔️ Hvordan du **begrænser antal viste datapunkter**  

---

## 📌 Trin 1: Opret en Real-Time Temperaturgraf
I dette eksempel simulerer vi en temperaturmåling, hvor data **ændrer sig over tid**.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Opret figur og akse
fig, ax = plt.subplots()
ax.set_xlim(0, 50)  # Vi viser kun de seneste 50 målinger
ax.set_ylim(20, 30)  # Temperaturinterval

# Tomme lister til at gemme data
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', label="Temperatur")

def init():
    ln.set_data([], [])
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(22 + np.random.normal(0, 0.5))  # Temperatur + støj
    ln.set_data(xdata[-50:], ydata[-50:])  # Kun de seneste 50 punkter
    return ln,

# Opret animation
ani = FuncAnimation(fig, update, frames=range(100), init_func=init, interval=500, blit=False)

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

2️⃣ **Vi sætter x-aksen til at vise de seneste 50 målinger:**  
   ```python
   ax.set_xlim(0, 50)
   ```

3️⃣ **Vi definerer `update(frame)`, der tilføjer nye målinger til grafen:**  
   ```python
   def update(frame):
       xdata.append(frame)
       ydata.append(22 + np.random.normal(0, 0.5))  # Temperatur med støj
       ln.set_data(xdata[-50:], ydata[-50:])  # Viser kun de seneste 50 målinger
       return ln,
   ```

4️⃣ **Vi opretter en animation med `FuncAnimation()`, der opdaterer grafen i realtid:**  
   ```python
   ani = FuncAnimation(fig, update, frames=range(100), init_func=init, interval=500, blit=False)
   ```

5️⃣ **Vi tilføjer en forklaring med `plt.legend()`**, så vi kan se, hvad grafen viser:  
   ```python
   plt.legend()
   ```

---

## ✅ Opgaver
1️⃣ Kør koden og se den real-time temperaturgraf.  
2️⃣ Prøv at **ændre `interval=200`** – hvad sker der?  
3️⃣ Tilføj en **blå linje for fugtighedsmålinger**.  
4️⃣ Gem animationen som en **GIF**.  

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
