# 🧹 Modul 08 – Støjreduktion: Rens dine data med filtre

I dette afsluttende modul anvender du dine filtre til at fjerne støj fra datasæt, som du selv har forurenet i modul 07. Her får du mulighed for at sammenligne filterteknikker og vurdere, hvor godt de fjerner forskellige typer støj.

---

## 🎯 Læringsmål

✔️ Anvende mean-, median- og frekvensbaserede filtre på støjfyldte data  
✔️ Vurdere effekten af forskellige filtre  
✔️ Identificere, hvilken type støj der er bedst egnet til hvert filter  
✔️ Visualisere og dokumentere støjreduktion

---

## 🧪 Eksempel: Filtrering af støjfyldt datasæt

```python
import pandas as pd
import matplotlib.pyplot as plt

# Indlæs støjfyldt data
file = "data_noisy.csv"
df = pd.read_csv(file)

# Filtrér med rolling mean og median
df["mean"] = df["temp_noisy"].rolling(window=5).mean()
df["median"] = df["temp_noisy"].rolling(window=5).median()

# Visualisér
plt.plot(df["timestamp"], df["temp_noisy"], label="Støjfyldt")
plt.plot(df["timestamp"], df["mean"], label="Mean")
plt.plot(df["timestamp"], df["median"], label="Median")
plt.legend()
plt.title("Støjreduktion")
plt.show()
```

---

## 📊 Evaluering af filtrene

Overvej:
- Hvilket filter klarer sig bedst mod white noise?
- Hvilket filter fjerner outliers bedst?
- Er der trade-offs mellem hurtig reaktion og støjreduktion?

---

## 💡 Avanceret (valgfrit): Low-pass filter med FFT

```python
import numpy as np
from scipy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

signal = df["temp_noisy"].values
N = len(signal)
dt = (df["timestamp"].iloc[1] - df["timestamp"].iloc[0]) / 1000  # ms → sek

# FFT og frekvensakse
frekvenser = fftfreq(N, dt)
spektrum = fft(signal)

# Low-pass filter: behold kun frekvenser < 1 Hz
cutoff = 1  # Hz
filtered_spectrum = spektrum.copy()
filtered_spectrum[np.abs(frekvenser) > cutoff] = 0

# Invers FFT for at genskabe signal
filtered_signal = ifft(filtered_spectrum).real

# Visualisér resultat
plt.plot(df["timestamp"], df["temp_noisy"], label="Støjfyldt")
plt.plot(df["timestamp"], filtered_signal, label="Low-pass (FFT)")
plt.legend()
plt.title("FFT-baseret støjreduktion")
plt.show()
```

---

## 🔁 Din opgave

1. Indlæs dine støjfyldte data fra `data_noisy.csv`  
2. Brug mean og median til at filtrere støj  
3. Plot og sammenlign med den originale og støjfyldte kurve  
4. *(Valgfrit)* Brug FFT og vurder, hvad der virker bedst

---

✅ Tillykke! Du har nu gennemført hele forløbet og har lært at generere, analysere, visualisere og rense sensor-data i realtid. Del gerne dit projekt med dine medstuderende eller på GitHub!

