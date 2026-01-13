# ⏱ Modul 4: Realtidsdataanalyse med NumPy

## 📌 **Introduktion**
I automationssystemer er det ofte nødvendigt at **behandle data i realtid**. Dette modul viser, hvordan vi kan håndtere **indkomne sensordata og analysere dem dynamisk** med NumPy.

🔗 **Forrige modul:** [03-signal-processing.md](03-signal-processing.md)  
🔜 **Næste modul:** [05-numerical-integration.md](05-numerical-integration.md)  

---

## ✅ **Trin 1: Simulér realtidsmålinger**
I mange systemer opsamles data **løbende** fra sensorer. Lad os simulere dette:

```python
import numpy as np
import matplotlib.pyplot as plt
import time

# Simuler en tom datastrøm
data_stream = []

plt.ion()  # Interaktiv tilstand

for i in range(100):
    new_value = np.sin(2 * np.pi * 0.1 * i) + np.random.normal(0, 0.1)  # Simuleret sensorværdi
    data_stream.append(new_value)

    # Opdater graf
    plt.clf()
    plt.plot(data_stream, label="Sensor data")
    plt.xlabel("Tid (samples)")
    plt.ylabel("Sensorværdi")
    plt.title("Realtidsdataanalyse")
    plt.legend()
    plt.pause(0.1)  # Simuler realtidsopdatering

plt.ioff()
plt.show()
```
✅ **Nu kan vi visualisere indkommende data i realtid!**  

---

## 🔎 **Trin 2: Udregn statistikker i realtid**
For at overvåge **trend og variation** i måledata kan vi beregne **middelværdi og standardafvigelse** i realtid.

```python
data_stream = []

for i in range(100):
    new_value = np.sin(2 * np.pi * 0.1 * i) + np.random.normal(0, 0.1)
    data_stream.append(new_value)

    if len(data_stream) > 10:
        window = data_stream[-10:]  # Tag de sidste 10 målinger
        mean = np.mean(window)
        std_dev = np.std(window)
        print(f"Seneste middelværdi: {mean:.3f}, Standardafvigelse: {std_dev:.3f}")
    
    time.sleep(0.1)  # Simuler realtidsmålinger
```
✅ **Nu beregner vi middelværdi og variation i realtid!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Simuleret en strøm af realtidsmålinger  
✔️ Visualiseret dataopdateringer løbende  
✔️ Beregnet middelværdi og variation i realtid  

🔜 **Fortsæt til næste modul:** [05-numerical-integration.md](05-numerical-integration.md), hvor vi arbejder med **numerisk integration af data!**  
