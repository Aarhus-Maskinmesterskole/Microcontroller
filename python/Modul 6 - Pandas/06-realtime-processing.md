# ⏱ Modul 6: Realtidsdataanalyse i Pandas

## 📌 **Introduktion**
I automationssystemer kan vi arbejde med **løbende opdateringer af sensordata**.  
Dette modul viser, hvordan vi **læser, behandler og analyserer data i realtid** i Pandas.

🔗 **Forrige modul:** [05-time-series.md](05-time-series.md)  
🔜 **Næste modul:** [07-visualization.md](07-visualization.md)  

---

## ✅ **Trin 1: Simulér en strøm af realtidsdata**
Når vi arbejder med sensordata eller streaming-data, kan vi simulere en **løbende strøm af måledata** i Pandas.  
Dette kan bruges til **test af realtidsanalyse, visualisering eller databehandling**.

### 🔹 **Generelt format for realtidsdata**
```python
for i in range(antal_målinger):
    ny_tid = pd.Timestamp.now()  # Generér tidsstempel
    ny_måling = np.random.uniform(min_værdi, max_værdi)  # Simuler måleværdi
    df = pd.concat([df, pd.DataFrame({"Tidspunkt": [ny_tid], "Måling": [ny_måling]})])
```

---

## 📄 **Eksempel: Simulér en strøm af realtidsdata**
```python
import pandas as pd
import numpy as np
import time

# Opret en tom DataFrame til at gemme data
df = pd.DataFrame(columns=["Tidspunkt", "Måling"])

# Simulér realtidsmålinger
for i in range(10):
    ny_tid = pd.Timestamp.now()
    ny_måling = np.random.uniform(20, 25)  # Simuleret temperatur
    ny_række = pd.DataFrame({"Tidspunkt": [ny_tid], "Måling": [ny_måling]})
    
    df = pd.concat([df, ny_række], ignore_index=True)  # Tilføj ny måling
    
    print(df.tail(1))  # Vis den nyeste måling
    time.sleep(1)  # Simulér realtidsforsinkelse
```

✅ **Nu genererer vi realtidsdata!**  

---

## ⏳ **Trin 1.1: Fortløbende opdatering af DataFrame**
Hvis vi vil **tilføje målinger løbende** og kun gemme de seneste værdier:

```python
for i in range(10):
    ny_tid = pd.Timestamp.now()
    ny_måling = np.random.uniform(20, 25)
    
    df.loc[len(df)] = [ny_tid, ny_måling]  # Tilføj direkte uden concat
    
    print(df.tail(1))
    time.sleep(1)
```

✅ **Nu gemmer vi målinger uden at lave kopier af DataFrame!**  

---

## 🎯 **Trin 1.2: Begræns størrelsen af DataFrame**
Hvis vi **kun vil gemme de seneste 100 målinger**, kan vi gøre følgende:

```python
df = df.iloc[-100:]  # Behold kun de sidste 100 rækker
```

✅ **Nu sikrer vi, at DataFrame ikke bliver for stor!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Simuleret en **løbende strøm af realtidsmålinger**  
✔️ Tilføjet nye data **uden at kopiere hele DataFrame**  
✔️ Begrænset **størrelsen af DataFrame for at spare hukommelse**  

🚀 **Nu kan du simulere og analysere realtidsdata i Pandas!**  

---
## 🔄 **Trin 2: Glidende gennemsnit af realtidsdata**
Når vi arbejder med realtidsmålinger, kan vi **udglatte data for at reducere støj**.  
Et **glidende gennemsnit** beregnes ved at tage gennemsnittet af de **n seneste målinger**.  

### 🔹 **Generelt format for `rolling().mean()`**
```python
df["ny_kolonne"] = df["målekolonne"].rolling(window=n).mean()
```

| Argument | Beskrivelse |
|----------|------------|
| `window=n` | Antal værdier til at beregne gennemsnittet over |
| `.mean()` | Beregner gennemsnit for hver rullevindue |
| `.rolling(window=n, min_periods=1)` | Starter gennemsnittet tidligere, selvom der er få målinger |

---

## 📄 **Eksempel: Beregn et glidende gennemsnit**
```python
df["Glidende Gennemsnit"] = df["Måling"].rolling(window=3).mean()
print(df.tail(5))  # Vis de seneste 5 målinger
```

✅ **Nu kan vi analysere realtidsdata med et glidende gennemsnit!**  

---

## 📊 **Trin 2.1: Visualiser glidende gennemsnit**
Vi kan **plotte rå data og det glidende gennemsnit** for at se udglatningen.

```python
import matplotlib.pyplot as plt

plt.plot(df["Tidspunkt"], df["Måling"], label="Rå data", linestyle="dotted")
plt.plot(df["Tidspunkt"], df["Glidende Gennemsnit"], label="Glidende gennemsnit", color="red")
plt.xlabel("Tid")
plt.ylabel("Måling")
plt.title("Glidende gennemsnit af realtidsdata")
plt.legend()
plt.show()
```

✅ **Nu kan vi se effekten af udglatningen grafisk!**  

---

## 🔄 **Trin 2.2: Brug eksponentiel glatning**
I stedet for et simpelt glidende gennemsnit kan vi bruge **eksponentiel glatning** (`ewm()`), hvor nyere målinger vægtes højere.

```python
df["Eksponentiel Gennemsnit"] = df["Måling"].ewm(alpha=0.3).mean()
print(df.tail(5))
```

✅ **Nu har vi brugt en mere dynamisk filtrering!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Beregnet **glidende gennemsnit** af realtidsdata  
✔️ Visualiseret **glidende gennemsnit sammen med rå data**  
✔️ Brugt **eksponentiel glatning for dynamisk filtrering**  

🚀 **Nu kan du udglatte realtidsmålinger i Pandas!**  

---

## 📤 **Trin 3: Gem realtidsdata løbende**
Når vi arbejder med realtidsdata, kan vi **løbende gemme data** i en CSV-fil, så vi ikke mister målinger.  

### 🔹 **Generelt format for `to_csv()` med løbende lagring**
```python
df.to_csv("filnavn.csv", mode="a", index=False, header=False)
```

| Argument | Beskrivelse |
|----------|------------|
| `mode="a"` | Tilføjer nye data til filen (append mode) |
| `index=False` | Gemmer data uden Pandas-indekset |
| `header=False` | Undgår at skrive kolonnenavne igen |

---

## 📄 **Eksempel: Gem realtidsdata løbende**
```python
df.to_csv("realtids_data.csv", index=False, mode="a", header=False)
print("Data gemt til realtids_data.csv!")
```

✅ **Nu gemmer vi realtidsmålinger i en CSV-fil!**  

---

## 🔄 **Trin 3.1: Initialiser CSV-filen med header**
Den første gang vi gemmer data, bør vi inkludere **kolonnenavne**.  
Derefter kan vi gemme nye data **uden header**.

```python
df.to_csv("realtids_data.csv", index=False, mode="w")  # Første gang (med header)
```

✅ **Nu har vi oprettet CSV-filen med kolonnenavne!**  

---

## 🔁 **Trin 3.2: Løbende opdatering af CSV-fil**
Hvis vi **henter nye målinger i en løkke**, kan vi gemme data efter hver iteration:

```python
import pandas as pd
import numpy as np
import time

# Simuler løbende dataopsamling
for _ in range(10):
    ny_tid = pd.Timestamp.now()
    ny_måling = np.random.uniform(20, 25)  # Simuleret temperatur
    ny_række = pd.DataFrame({"Tidspunkt": [ny_tid], "Måling": [ny_måling]})

    ny_række.to_csv("realtids_data.csv", index=False, mode="a", header=False)
    time.sleep(1)
```

✅ **Nu gemmer vi realtidsmålinger løbende!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Lært at **gemme realtidsmålinger løbende**  
✔️ Initialiseret CSV-filen **med header**  
✔️ Implementeret **automatisk lagring af nye målinger**  

🚀 **Nu kan du håndtere og gemme realtidsdata effektivt i Pandas!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Simuleret en **løbende strøm af realtidsmålinger**  
✔️ Anvendt **glidende gennemsnit** på realtidsdata  
✔️ Lært at **gemme realtidsmålinger løbende**  

🔜 **Fortsæt til næste modul:** [07-visualization.md](07-visualization.md), hvor vi lærer **at visualisere data med Pandas og Matplotlib**!  
