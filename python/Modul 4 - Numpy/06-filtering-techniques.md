# 🎚 Modul 6: Filtrering af støj i måledata med NumPy

## 📌 **Introduktion**
I automation og signalbehandling støder vi ofte på **støj i måledata**. Dette modul viser, hvordan vi **filtrerer data** for at opnå mere præcise målinger.

🔗 **Forrige modul:** [05-numerical-integration.md](05-numerical-integration.md)  
🔜 **Næste modul:** [07-transformations.md](07-transformations.md)  

---

## ✅ **Trin 1: Simulér støjende måledata**
Vi starter med at simulere **måledata med støj**, fx fra en temperatur- eller tryksensor.

```python
import numpy as np
import matplotlib.pyplot as plt

# Simuler en tidsakse (10 sekunder, 1000 samples)
t = np.linspace(0, 10, 1000)

# Simuler et signal (fx en temperaturmåling) med støj
signal = np.sin(2 * np.pi * 0.5 * t) + np.random.normal(0, 0.3, size=len(t))

# Plot signalet
plt.plot(t, signal, label="Støjende signal")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Simuleret sensor med støj")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi genereret et støjende signal!**  

---

## 🎚 **Trin 2: Glidende gennemsnitsfilter**
Et **simpelt glidende gennemsnit** kan hjælpe med at reducere støj.

```python
def moving_average(data, window_size=10):
    return np.convolve(data, np.ones(window_size)/window_size, mode="valid")

# Filtrer signalet med glidende gennemsnit
filtered_signal = moving_average(signal, 20)

# Plot resultatet
plt.plot(t[:len(filtered_signal)], filtered_signal, label="Filtreret signal", color="red")
plt.plot(t, signal, alpha=0.4, label="Støjende signal", linestyle="dashed")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Glidende gennemsnitsfiltrering")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi reduceret støjen med et glidende gennemsnit!**  

---

## 🛠 **Trin 3: Eksponentiel glatning (EMA)**
Eksponentiel glatning giver et **mere dynamisk filter**, der tilpasser sig hurtigere til ændringer.

```python
def exponential_moving_average(data, alpha=0.1):
    filtered = np.zeros_like(data)
    filtered[0] = data[0]
    for i in range(1, len(data)):
        filtered[i] = alpha * data[i] + (1 - alpha) * filtered[i - 1]
    return filtered

# Filtrer signalet med eksponentiel glatning
filtered_signal_ema = exponential_moving_average(signal, 0.1)

# Plot resultatet
plt.plot(t, filtered_signal_ema, label="Eksponentielt glattet signal", color="green")
plt.plot(t, signal, alpha=0.4, label="Støjende signal", linestyle="dashed")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Eksponentiel glatning (EMA)")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi brugt en mere avanceret filtreringsmetode!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Simuleret støjende måledata  
✔️ Implementeret **glidende gennemsnitsfilter**  
✔️ Implementeret **eksponentiel glatning**  

🔜 **Fortsæt til næste modul:** [07-transformations.md](07-transformations.md), hvor vi arbejder med **Fourier- og spektralanalyse!**  
