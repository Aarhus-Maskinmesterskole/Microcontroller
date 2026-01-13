# 🔄 Modul 5: Numerisk integration med NumPy

## 📌 **Introduktion**
Numerisk integration bruges i **automations- og styringssystemer** til at **beregne arealer under kurver**, hvilket er nyttigt i fx **flowmåling, energiudregninger og signalbehandling**.

🔗 **Forrige modul:** [04-real-time-data.md](04-real-time-data.md)  
🔜 **Næste modul:** [06-filtering-techniques.md](06-filtering-techniques.md)  

---

## ✅ **Trin 1: Hvad er numerisk integration?**
Integration bruges ofte til at **summe diskrete datapunkter** for at finde en total værdi over tid.

NumPy har flere måder at integrere på:
- **Trapez-metoden (`np.trapz`)**  
- **Simpsons regel (`scipy.integrate.simps`)**  

---

## 📊 **Trin 2: Integrér et signal med NumPy**

Lad os beregne den **totale energi** af et signal ved hjælp af **trapez-reglen**.

```python
import numpy as np
import matplotlib.pyplot as plt

# Simuler en tidsakse (10 sekunder, 1000 samples)
t = np.linspace(0, 10, 1000)

# Simuler en strøm af data (fx en strømstyrke i en motor)
signal = np.sin(2 * np.pi * 0.5 * t) + 2  # Skift signalet op for at undgå negative værdier

# Integrér signalet for at finde den totale energi
integral = np.trapz(signal, t)

# Plot signalet
plt.plot(t, signal, label="Signal")
plt.fill_between(t, signal, alpha=0.3)  # Visualiser integrationen
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title(f"Numerisk integration: Areal = {integral:.2f}")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi beregnet den totale energi af signalet!**  

---

## 🔢 **Trin 3: Løbende integration i realtid**
Hvis vi modtager data i realtid, kan vi integrere **inkrementelt**:

```python
import numpy as np
import time

data_stream = []
integral = 0

for i in range(100):
    new_value = np.sin(2 * np.pi * 0.1 * i) + 2  # Simuleret sensorværdi
    data_stream.append(new_value)

    if len(data_stream) > 1:
        integral += (data_stream[-1] + data_stream[-2]) / 2 * 0.1  # Trapez-metoden
        print(f"Total integral (Areal): {integral:.3f}")
    
    time.sleep(0.1)  # Simuler realtidsmålinger
```

✅ **Nu integrerer vi sensorværdier i realtid!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Forstået, hvordan numerisk integration bruges i automation  
✔️ Beregnet **total energi af et signal**  
✔️ Implementeret **real-time integration af måledata**  

🔜 **Fortsæt til næste modul:** [06-filtering-techniques.md](06-filtering-techniques.md), hvor vi arbejder med **støjfiltrering i måledata**!  
