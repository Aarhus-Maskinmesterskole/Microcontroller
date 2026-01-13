# 🐍 Modul 02 – CSV-filtrering med Python og pandas

I dette modul lærer du at læse og filtrere CSV-data i Python. Du vil bruge `pandas` til at indlæse filen, og derefter anvende forskellige filtre (mean og median) for at reducere støj i datasættet.

---

## 🎯 Læringsmål

✔️ Indlæse CSV-filer med `pandas`  
✔️ Forstå og anvende rullende ("rolling") gennemsnit og medianfiltre  
✔️ Visualisere rå og filtrerede data med `matplotlib`  
✔️ Eksperimentere med forskellige vinduesstørrelser og sammenligne resultater

---

## 📁 Trin 1 – Download eller gem dine data

Brug enten den data du har genereret fra ESP32, eller hent `data.csv` fra `01_materialer/`.

Eksempel på indhold i `data.csv`:

```csv
timestamp,temp,humidity
0,22.5,56.1
500,22.7,55.8
1000,22.8,56.2
```

---

## 🧪 Trin 2 – Indlæs og vis data i Python

Opret en Python-fil `filtrering.py` og indsæt:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Indlæs CSV-data
file = "data.csv"
df = pd.read_csv(file)

# Vis de første rækker
print(df.head())

# Plot rå data
plt.plot(df["timestamp"], df["temp"], label="Raw")
plt.xlabel("Tid (ms)")
plt.ylabel("Temperatur")
plt.title("Temperatur over tid")
plt.legend()
plt.show()
```

---

## 🔁 Trin 3 – Tilføj glidende gennemsnit

```python
# Tilføj kolonne med glidende gennemsnit (vindue = 5 rækker)
df["temp_mean"] = df["temp"].rolling(window=5).mean()

# Plot med filter
plt.plot(df["timestamp"], df["temp"], label="Raw")
plt.plot(df["timestamp"], df["temp_mean"], label="Mean Filter")
plt.legend()
plt.show()
```

---

## 📏 Trin 4 – Medianfiltrering

```python
# Tilføj kolonne med glidende median (vindue = 5)
df["temp_median"] = df["temp"].rolling(window=5).median()

# Plot sammenligning
plt.plot(df["timestamp"], df["temp"], label="Raw")
plt.plot(df["timestamp"], df["temp_mean"], label="Mean")
plt.plot(df["timestamp"], df["temp_median"], label="Median")
plt.legend()
plt.show()
```

---

## 🔁 Din opgave

1. Indlæs data fra ESP32 eller en CSV-fil  
2. Plot den rå temperatur- eller fugtighedskurve  
3. Anvend rolling mean og median, og visualisér begge  
4. Prøv forskellige vinduesstørrelser (`window=3`, `7`, `15`) og se forskellen  
5. *(Valgfrit)* Brug samme teknik på `humidity`

---

✅ Når du er klar, fortsæt til næste modul: [`03_realtime_plot`](../03_realtime_plot/) hvor du skal arbejde med realtidsdata fra ESP32 i Python!

