# 📊 Modul 7: Fourier- og spektralanalyse med NumPy

## 📌 **Introduktion**
I automation og signalbehandling bruges **Fourier-transformation** til at **analysere frekvensindholdet** i et signal.  
Dette er nyttigt til **detektion af periodiske mønstre**, **fejldiagnostik** og **filtrering af uønskede frekvenser**.

🔗 **Forrige modul:** [06-filtering-techniques.md](06-filtering-techniques.md)  
🔜 **Næste modul:** [08-next-steps.md](08-next-steps.md)  

---

## ✅ **Trin 1: Generér et signal med flere frekvenser**
Lad os oprette et **komplekst signal**, der indeholder flere frekvenser.

```python
import numpy as np
import matplotlib.pyplot as plt

# Simuler en tidsakse (1 sekund, 1000 samples)
t = np.linspace(0, 1, 1000, endpoint=False)

# Generér et signal med to frekvenser (5 Hz og 50 Hz)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)

# Plot signalet
plt.plot(t, signal)
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Signal med flere frekvenser")
plt.grid(True)
plt.show()
```

✅ **Nu har vi et signal med to frekvenser!**  

---

## 🔎 **Trin 2: Fourier-transformation (FFT)**
Fourier-transformation bruges til **at finde signalets frekvensindhold**.

```python
# Beregn Fourier-transformation (FFT)
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), d=t[1] - t[0])  # Beregn frekvensaksen

# Plot spektret
plt.plot(frequencies[:500], np.abs(fft_result)[:500])  # Kun positive frekvenser
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.title("Spektralanalyse med Fourier-transformation")
plt.grid(True)
plt.show()
```

✅ **Nu kan vi se signalets frekvensindhold!**  

---

## 🛠 **Trin 3: Filtrér en uønsket frekvens**
Lad os **filtrere 50 Hz-komponenten væk** ved at fjerne dens spektrum-komponent.

```python
# Lav en kopi af FFT-resultatet
filtered_fft = fft_result.copy()

# Fjern 50 Hz-komponenten
filtered_fft[(frequencies > 49) & (frequencies < 51)] = 0

# Invers FFT for at få det filtrerede signal tilbage
filtered_signal = np.fft.ifft(filtered_fft)

# Plot det filtrerede signal
plt.plot(t, filtered_signal.real, label="Filtreret signal")
plt.plot(t, signal, alpha=0.4, label="Originalt signal", linestyle="dashed")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Signal efter fjernelse af 50 Hz støj")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi fjernet 50 Hz-støjen fra signalet!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Oprettet et signal med **flere frekvenser**  
✔️ Anvendt **Fourier-transformation (FFT)** til spektralanalyse  
✔️ Filtreret en **uønsket frekvens** fra signalet  
