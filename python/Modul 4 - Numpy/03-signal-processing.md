# 🎛 Modul 3: Signalbehandling med NumPy

## 📌 **Introduktion**
Dette modul dækker **grundlæggende signalbehandling** i NumPy, herunder **sampling, generering af signaler og filtrering**, som er vigtige i automation og måleteknik.

🔗 **Forrige modul:** [02-numpy-basics.md](02-numpy-basics.md)  
🔜 **Næste modul:** [04-real-time-data.md](04-real-time-data.md)  

---

## ✅ **Trin 1: Simulér et signal med NumPy**
I automation og signalbehandling arbejder vi ofte med **sinus- og firkantsignaler**.

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulér en tidsakse (1 sekund, 500 samples)
t = np.linspace(0, 1, 500)

# Generér et 5 Hz sinus-signal
signal = np.sin(2 * np.pi * 5 * t)

# Plot signalet
plt.plot(t, signal)
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Simuleret sinus-signal")
plt.grid(True)
plt.show()
```
✅ **Nu har vi simuleret et signal!**  

---

## 🎛 **Trin 2: Tilføj støj til signalet**
I virkelige målinger støder vi ofte på **støj**. Lad os simulere dette.

```python
# Tilføj hvid støj (Gaussisk støj) til signalet
noise = np.random.normal(0, 0.3, signal.shape)
noisy_signal = signal + noise

# Plot støjende signal
plt.plot(t, noisy_signal, label="Støjende signal")
plt.plot(t, signal, label="Originalt signal", linestyle="dashed")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Signal med støj")
plt.legend()
plt.grid(True)
plt.show()
```
✅ **Nu har vi tilføjet realistisk støj til signalet!**  

---

## 🎚 **Trin 3: Glat signalet med et glidende gennemsnit**
Filtrering bruges ofte i automationssystemer til **at reducere støj**.

```python
def moving_average(data, window_size=5):
    return np.convolve(data, np.ones(window_size)/window_size, mode="valid")

# Anvend glidende gennemsnit
filtered_signal = moving_average(noisy_signal, 10)

# Plot resultatet
plt.plot(t[:len(filtered_signal)], filtered_signal, label="Filtreret signal", color="red")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Glidende gennemsnitsfiltrering")
plt.legend()
plt.grid(True)
plt.show()
```
✅ **Nu har vi filtreret signalet med et simpelt glidende gennemsnit!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Simuleret et sinus-signal  
✔️ Tilføjet støj til signalet  
✔️ Anvendt **glidende gennemsnit** til filtrering  

🔜 **Fortsæt til næste modul:** [04-real-time-data.md](04-real-time-data.md), hvor vi arbejder med **realtidsdataanalyse i NumPy**!  
