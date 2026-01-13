# 📊 Modul 7: Visualisering af data med Pandas og Matplotlib

## 📌 **Introduktion**
For at forstå måledata bedre er det ofte en god idé at **visualisere dem**.  
I dette modul lærer vi at **plotte data med Pandas og Matplotlib**.

🔗 **Forrige modul:** [06-realtime-processing.md](06-realtime-processing.md)  
🔜 **Næste modul:** [08-next-steps.md](08-next-steps.md)  

---

## ✅ **Trin 1: Opret en simpel graf**
Vi kan bruge **Matplotlib** til at visualisere en Pandas DataFrame og vise målinger som en graf.  

### 🔹 **Generelt format for `plt.plot()`**
```python
plt.plot(x_data, y_data, marker, linestyle, color, label)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `x_data` | X-aksens værdier (fx tidspunkter) | **Påkrævet** |
| `y_data` | Y-aksens værdier (fx temperaturmålinger) | **Påkrævet** |
| `marker` | Markørtype for datapunkter (fx `"o"` for cirkler) | `None` |
| `linestyle` | Linjetype (fx `"-"` for fuld linje, `"--"` for stiplet) | `"-"` |
| `color` | Farve på linjen | Automatisk valgt |
| `label` | Navn til kurven (bruges med `plt.legend()`) | `None` |

---

## 📄 **Eksempel: Opret en simpel graf**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Simuler nogle måledata
data = {
    "Tidspunkt": pd.date_range(start="2024-03-01", periods=10, freq="D"),
    "Måling": [20, 21, 22, 21, 23, 24, 25, 26, 27, 28]
}

df = pd.DataFrame(data)

# Plot data
plt.plot(df["Tidspunkt"], df["Måling"], marker="o", linestyle="-")
plt.xlabel("Tid")
plt.ylabel("Temperatur ( C)")
plt.title("Temperaturmålinger over tid")
plt.grid(True)
plt.show()
```

✅ **Nu har vi plottet en simpel tidsserie!**  

---

## 📊 **Trin 1.1: Tilføj flere kurver til grafen**
Hvis vi har **flere sensorer**, kan vi plotte dem sammen.

```python
df["Måling2"] = df["Måling"] + 2  # Simuler en anden sensor

plt.plot(df["Tidspunkt"], df["Måling"], marker="o", label="Sensor 1")
plt.plot(df["Tidspunkt"], df["Måling2"], marker="s", linestyle="--", label="Sensor 2")
plt.xlabel("Tid")
plt.ylabel("Måling")
plt.title("Flere sensorer over tid")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi tilføjet flere kurver til grafen!**  

---

## 🎨 **Trin 1.2: Tilpas grafens udseende**
Vi kan **ændre farver, linjestile og layout**.

```python
plt.plot(df["Tidspunkt"], df["Måling"], color="red", linestyle="dashed", marker="x")
plt.xlabel("Tid")
plt.ylabel("Temperatur ( C)")
plt.title("Tilpasset graf")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
```

✅ **Nu har vi tilpasset grafens udseende!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Plottet **en simpel graf med Matplotlib**  
✔️ Tilføjet **flere kurver til samme graf**  
✔️ Tilpasset **grafens farver og layout**  

🚀 **Nu kan du visualisere data effektivt i Pandas!**  

---

## 🔄 **Trin 2: Glidende gennemsnit i et plot**
For at **udglatte data** kan vi tilføje en **glidende gennemsnitskurve**.  
Dette hjælper med at reducere støj i data og gøre tendenser mere tydelige.

### 🔹 **Generelt format for glidende gennemsnit**
```python
df["Glidende Gennemsnit"] = df["Måling"].rolling(window=n).mean()
```

| Argument | Beskrivelse |
|----------|------------|
| `window=n` | Antal målinger brugt til at beregne gennemsnittet |
| `.mean()` | Beregner gennemsnittet for hvert rullende vindue |

---

## 📄 **Eksempel: Plot rå data og glidende gennemsnit**
```python
df["Glidende Gennemsnit"] = df["Måling"].rolling(window=3).mean()

plt.plot(df["Tidspunkt"], df["Måling"], marker="o", linestyle="-", label="Rå data")
plt.plot(df["Tidspunkt"], df["Glidende Gennemsnit"], linestyle="--", label="Glidende gennemsnit")
plt.xlabel("Tid")
plt.ylabel("Temperatur ( C)")
plt.title("Temperatur med glidende gennemsnit")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu kan vi vise både rå data og en glidende gennemsnitskurve!**  

---

## 📊 **Trin 2.1: Tilpas vinduet for glidende gennemsnit**
Hvis vi ændrer **window**-størrelsen, kan vi få **mere eller mindre udglatning**.

```python
df["Glidende Gennemsnit 5"] = df["Måling"].rolling(window=5).mean()

plt.plot(df["Tidspunkt"], df["Måling"], marker="o", linestyle="-", label="Rå data")
plt.plot(df["Tidspunkt"], df["Glidende Gennemsnit 5"], linestyle="--", label="Glidende gennemsnit (5)")
plt.xlabel("Tid")
plt.ylabel("Temperatur ( C)")
plt.title("Temperatur med glidende gennemsnit (5 målinger)")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi justeret vinduet for glidende gennemsnit!**  

---

## 🔄 **Trin 2.2: Brug eksponentiel glatning (`ewm()`)**
Eksponentiel glatning vægter **nyere målinger højere** end ældre.

```python
df["Eksponentiel Gennemsnit"] = df["Måling"].ewm(alpha=0.3).mean()

plt.plot(df["Tidspunkt"], df["Måling"], marker="o", linestyle="-", label="Rå data")
plt.plot(df["Tidspunkt"], df["Eksponentiel Gennemsnit"], linestyle="--", label="Eksponentiel glatning")
plt.xlabel("Tid")
plt.ylabel("Temperatur ( C)")
plt.title("Temperatur med eksponentiel glatning")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu har vi brugt en mere avanceret metode til udglatning!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Tilføjet **glidende gennemsnit til et plot**  
✔️ Justeret **vinduet for glidende gennemsnit**  
✔️ Anvendt **eksponentiel glatning** for en mere dynamisk filtrering  

🚀 **Nu kan du visualisere data med glidende gennemsnit i Pandas!**  

---

## 📊 **Trin 3: Histogram af måledata**
Et **histogram** bruges til at **se fordelingen af målinger** over et interval.  
Dette hjælper os med **at forstå, hvordan data er fordelt** og identificere tendenser.

### 🔹 **Generelt format for `plt.hist()`**
```python
plt.hist(data, bins=n, edgecolor="black", alpha=transparens, color="farve")
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `data` | Data der skal plottes | **Påkrævet** |
| `bins=n` | Antal intervaller (søjler) i histogrammet | Automatisk valgt |
| `edgecolor="black"` | Farve på kantlinjer mellem søjler | `None` |
| `alpha=0.75` | Gennemsigtighed af søjlerne (1 = ingen gennemsigtighed) | `1.0` |
| `color="blue"` | Farve på søjler | Automatisk valgt |

---

## 📄 **Eksempel: Plot et histogram af måledata**
```python
plt.hist(df["Måling"], bins=5, edgecolor="black")
plt.xlabel("Temperatur (°C)")
plt.ylabel("Antal målinger")
plt.title("Histogram over temperaturmålinger")
plt.grid(True)
plt.show()
```

✅ **Nu kan vi se fordelingen af måledata!**  

---

## 📈 **Trin 3.1: Justér antallet af bins**
Hvis vi ændrer **bins**, kan vi **få mere eller mindre detaljer i histogrammet**.

```python
plt.hist(df["Måling"], bins=10, edgecolor="black")
plt.title("Histogram med 10 bins")
plt.show()
```

✅ **Nu har vi en mere detaljeret visning af datafordelingen!**  

---

## 🎨 **Trin 3.2: Tilpas farver og gennemsigtighed**
Vi kan **ændre farver** og gøre søjlerne delvist gennemsigtige.

```python
plt.hist(df["Måling"], bins=7, edgecolor="black", color="red", alpha=0.6)
plt.title("Tilpasset histogram")
plt.show()
```

✅ **Nu har vi gjort histogrammet mere visuelt tiltalende!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Plottet **et histogram for at se fordelingen af måledata**  
✔️ Justeret **antallet af bins for mere eller mindre detaljer**  
✔️ Tilpasset **farver og gennemsigtighed for bedre visualisering**  

🚀 **Nu kan du lave informative histogrammer i Pandas!**  

---

# ✅ **Hvad har vi opnået?**
✔️ Plottet **måledata over tid**  
✔️ Tilføjet **glidende gennemsnit til et plot**  
✔️ Visualiseret **fordelingen af måledata med et histogram**  

🔜 **Fortsæt til næste modul:** [08-next-steps.md](08-next-steps.md), hvor vi udforsker **avancerede anvendelser og næste skridt**!  
