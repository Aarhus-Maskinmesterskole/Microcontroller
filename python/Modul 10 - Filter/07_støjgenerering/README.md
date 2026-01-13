# 🎛️ Modul 07 – Støjgenerering: Simulér og forstå støj

I dette modul lærer du at simulere forskellige typer støj i dine datasæt. Det gør det muligt at teste dine filtre og forstå, hvordan støj påvirker målinger og visualisering.

---

## 🎯 Læringsmål

✔️ Forstå forskellen på tilfældig og periodisk støj  
✔️ Tilføje støj til eksisterende CSV-data i Python  
✔️ Visualisere effekten af støj  
✔️ Forberede datasæt til test af filtreringsteknikker

---

## 📦 Typer af støj vi simulerer

- **Additiv hvid støj (AWGN)** – tilfældig og jævn fordeling
- **Periodisk støj** – f.eks. sinusformede udsving (støj på 50Hz)
- **Outliers** – pludselige spikes i data

---

## 🧪 Eksempel: Tilføj hvid støj til temperaturmålinger

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Indlæs data
file = "data.csv"
df = pd.read_csv(file)

# Tilføj støj
np.random.seed(42)
df["temp_noisy"] = df["temp"] + np.random.normal(0, 0.5, size=len(df))

# Plot
plt.plot(df["timestamp"], df["temp"], label="Original")
plt.plot(df["timestamp"], df["temp_noisy"], label="Med støj")
plt.legend()
plt.show()
```

---

## 💡 Andre støjtyper

```python
# Tilføj periodisk støj (f.eks. 50 Hz)
f = 50  # Hz
fs = 1000 / (df["timestamp"].iloc[1] - df["timestamp"].iloc[0])
t = df["timestamp"] / 1000  # ms → sek
sin_noise = 0.4 * np.sin(2 * np.pi * f * t)
df["temp_periodic"] = df["temp"] + sin_noise
```

```python
# Tilføj spikes (outliers)
outlier_idx = np.random.choice(len(df), size=5)
df.loc[outlier_idx, "temp"] += np.random.uniform(5, 10, size=5)
```

---

## 🔁 Din opgave

1. Tilføj forskellige typer støj til dine målinger (AWGN, sinus, outliers)  
2. Visualisér resultaterne og sammenlign med originalen  
3. Gem dine støjfyldte data som ny CSV-fil (f.eks. `data_noisy.csv`)  
4. Brug de filtreringsmetoder fra tidligere moduler på det støjfyldte datasæt

---

✅ Klar til næste modul? Gå videre til [`08_støjreduktion`](../08_støjreduktion/) og brug dine filtre til at rense data igen!

