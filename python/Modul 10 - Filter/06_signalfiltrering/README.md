# ⚡️ Modul 06 – Signalfiltrering: Mean, Median og Fourier

I dette modul dykker vi dybere ned i signalfiltrering. Du lærer, hvordan forskellige filtre fungerer, og hvornår du bør anvende dem. Vi arbejder både med rullende gennemsnit, medianfiltrering og Fourier-transform til frekvensanalyse.

---

## 🎯 Læringsmål

✔️ Forstå forskellen mellem mean, median og frekvensbaserede filtre  
✔️ Anvende signalfiltrering i Python med `pandas`, `numpy` og `scipy`  
✔️ Filtrere data for at fjerne støj og finde trends  
✔️ Bruge FFT til at analysere frekvensindhold i signaler

---

## 🧪 Mean og Median filtrering

Start med at læse din CSV-data (fra ESP32 eller testfil) og anvend rolling mean og median:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df["mean"] = df["temp"].rolling(window=5).mean()
df["median"] = df["temp"].rolling(window=5).median()

plt.plot(df["timestamp"], df["temp"], label="Raw")
plt.plot(df["timestamp"], df["mean"], label="Mean")
plt.plot(df["timestamp"], df["median"], label="Median")
plt.legend()
plt.show()
```

---

## 📊 Fourier-analyse med FFT

Fourier-transform bruges til at identificere frekvenser (f.eks. periodisk støj):

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.interpolate import interp1d

# === 1. Indlæs data og parse timestamp ===
df = pd.read_csv("data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

# === 2. Konverter tid til sekunder fra start ===
df["time_sec"] = (df["timestamp"] - df["timestamp"].iloc[0]).dt.total_seconds()

# === 3. Interpolér temperatur til faste tidspunkter ===
dt = 1.0  # 1 sekund mellem samples (du kan ændre dette)
t_uniform = np.arange(0, df["time_sec"].iloc[-1], dt)
interp_func = interp1d(df["time_sec"], df["temperature"], kind="linear", fill_value="extrapolate")
signal_uniform = interp_func(t_uniform)

# === 4. FFT ===
N = len(signal_uniform)
frequencies = fftfreq(N, dt)
spectrum = np.abs(fft(signal_uniform))

# === 5. Plot ===
plt.figure(figsize=(10, 5))
plt.plot(frequencies[:N//2], spectrum[:N//2])
plt.title("FFT af interpoleret temperatur")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

## 💡 Hvad kan du bruge det til?

- Mean: Reducerer tilfældig støj men sløver hurtige ændringer
- Median: God mod outliers eller spikes i data
- FFT: Finder periodisk støj og svingninger i signalet

---

## 🔁 Din opgave

1. Anvend mean og median-filtrering på dine data  
2. Brug FFT til at analysere frekvensindhold  
3. Eksperimentér med forskellige vinduer og tolk resultaterne  
4. *(Avanceret)* Filtrer signalet i frekvensdomænet og genskab det med invers FFT

---

✅ Når du har forstået filtrene, kan du gå videre til næste trin: [`07_støjgenerering`](../07_støjgenerering/) hvor du lærer at simulere støj og teste dine filtre!

