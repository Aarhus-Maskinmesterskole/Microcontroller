# 🔢 Modul 2: Grundlæggende Pandas operationer

## 📌 **Introduktion**
Dette modul introducerer de vigtigste Pandas-funktioner til **databehandling, filtrering og transformation**.  
Vi lærer at **åbne og gemme data**, **slicke**, **flytte kolonner/rækker**, **tilføje/fjerne data**, og **transponere DataFrames**.

🔗 **Forrige modul:** [01-installation.md](01-installation.md)  
🔜 **Næste modul:** [03-import-export.md](03-import-export.md)  

---
## ✅ **Trin 1: Opret og gem en Pandas DataFrame**
Lad os starte med at **oprette en DataFrame og gemme den**.

### 🔹 **Hvad er en Pandas DataFrame?**
En **DataFrame** er en tabel-lignende datastruktur i Pandas, der bruges til **at organisere og analysere data i rækker og kolonner**.

### 📄 **Generelt format for `pd.DataFrame()`**
```python
import pandas as pd

df = pd.DataFrame(data, index, dtype)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `data` | Dictionary, liste af lister eller en NumPy-array med data | **Påkrævet** |
| `index` | Rækkenavne (hvis ikke angivet, bruges 0,1,2,...) | `None` |
| `dtype` | Angiver datatypen for kolonnerne | Automatisk detekteret |

### 📄 **Eksempel: Opret en DataFrame**
```python
import pandas as pd

# Opret et datasæt
data = {
    "Sensor": ["Temp", "Tryk", "Fugt"],
    "Værdi": [22.5, 1013, 45],
    "Enhed": ["C", "hPa", "%"]
}

df = pd.DataFrame(data)

print(df)
```

🔹 **Output:**
```
  Sensor  Værdi Enhed
0   Temp   22.5     C
1   Tryk  1013  hPa
2   Fugt   45.0     %
```

✅ **Nu har vi oprettet en DataFrame!**  

---

## 📤 **Gem DataFrame til CSV**
Vi kan gemme vores DataFrame til en **CSV-fil** for senere brug.

### 🔹 **Generelt format for `to_csv()`**
```python
df.to_csv(filepath, sep, index, header, encoding, mode)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `filepath` | Filnavn eller sti, hvor CSV-filen gemmes | **Påkrævet** |
| `sep` | Separator (fx `","` for CSV, `";"` for semikolon-separeret) | `","` |
| `index` | Om DataFrame-indekset skal gemmes i filen | `True` |
| `header` | Om kolonnenavne skal inkluderes i filen | `True` |
| `encoding` | Tegnsæt til filen (fx `"utf-8"`, `"latin1"`) | `"utf-8"` |
| `mode` | `"w"` for at overskrive, `"a"` for at tilføje data | `"w"` |

### 📄 **Eksempel: Gem DataFrame som CSV**
```python
df.to_csv("sensor_data.csv", index=False)
print("Data gemt til 'sensor_data.csv'!")
```

✅ **Nu har vi gemt data i en CSV-fil uden index-kolonnen!**  

---

## 📥 **Trin 2: Åbn en CSV-fil i Pandas**
Vi kan nu **åbne CSV-filen** og arbejde videre med dataene.

### 🔹 **Generelt format for `pd.read_csv()`**
```python
df = pd.read_csv(filepath, sep, header, names, usecols, nrows, skiprows, dtype, parse_dates, encoding)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `filepath` | Filnavn eller sti til CSV-filen | **Påkrævet** |
| `sep` | Separator (fx `","` for CSV, `";"` for semikolon-separeret) | `","` |
| `header` | Hvilken række der skal bruges som kolonneoverskrifter (`None` hvis ingen) | `infer` |
| `names` | Angiv egne kolonnenavne som en liste | `None` |
| `usecols` | Vælg specifikke kolonner at indlæse | `None` (henter alle kolonner) |
| `nrows` | Antal rækker at indlæse | `None` (henter alle rækker) |
| `skiprows` | Antal rækker at springe over i starten | `0` |
| `dtype` | Tving en bestemt datatype for kolonner | `None` (auto-detekteres) |
| `parse_dates` | Konverter kolonner til datetime-format | `False` |
| `encoding` | Tegnsæt for filen (fx `"utf-8"`, `"latin1"`) | `"utf-8"` |

### 📄 **Eksempel: Indlæs en hel CSV-fil**
```python
df = pd.read_csv("sensor_data.csv")
print(df)
```

🔹 **Output:**
```
  Sensor  Værdi Enhed
0   Temp   22.5     C
1   Tryk  1013  hPa
2   Fugt   45.0     %
```

✅ **Nu har vi indlæst data fra en CSV-fil!**  

---

## 🛠 **Trin 2.1: Indlæs kun bestemte kolonner**
Hvis vi kun vil **indlæse nogle af kolonnerne**, kan vi bruge `usecols`.

```python
df = pd.read_csv("sensor_data.csv", usecols=["Sensor", "Værdi"])
print(df)
```

✅ **Nu har vi kun hentet de ønskede kolonner!**  

---

## ⏳ **Trin 2.2: Indlæs kun et begrænset antal rækker**
Hvis vi kun vil **indlæse de første 2 rækker**, kan vi bruge `nrows`.

```python
df = pd.read_csv("sensor_data.csv", nrows=2)
print(df)
```

✅ **Nu har vi kun hentet de første 2 rækker!**  

---

## 🗃 **Trin 2.3: Spring bestemte rækker over**
Hvis vi vil **springe de første rækker over**, kan vi bruge `skiprows`.

```python
df = pd.read_csv("sensor_data.csv", skiprows=1)  # Spring første række over
print(df)
```

✅ **Nu har vi sprunget den første række over!**  

---

## 📆 **Trin 2.4: Konverter en kolonne til datetime**
Hvis vores data indeholder tidsstempler, kan vi **automatisk konvertere dem til datetime**.

```python
df = pd.read_csv("sensor_data.csv", parse_dates=["Tidspunkt"])
print(df.dtypes)  # Se datatyper
```

✅ **Nu er Tidspunkt-kolonnen konverteret til datetime!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Indlæst en **CSV-fil** med Pandas  
✔️ Udvalgt **specifikke kolonner og rækker**  
✔️ Sprunget over **rækker ved indlæsning**  
✔️ Konverteret **tidsstempler automatisk**  

🚀 **Nu kan du arbejde fleksibelt med CSV-data i Pandas!**   

---

## 🔍 **Trin 3: Filtrér data**
Vi kan **filtrere rækker**, fx hvis vi kun vil have sensorer med værdier over 100.

### 🔹 **Generelt format for filtrering i Pandas**
```python
df[condition]
df.loc[condition, selected_columns]
df.query("condition")
```

| Metode | Beskrivelse |
|--------|------------|
| `df[condition]` | Filtrerer rækker baseret på en betingelse |
| `df.loc[condition, columns]` | Filtrerer rækker og vælger specifikke kolonner |
| `df.query("condition")` | Bruger en SQL-lignende syntaks til at filtrere data |

### 📄 **Eksempel: Filtrér rækker med en betingelse**
```python
filtered_df = df[df["Værdi"] > 100]
print(filtered_df)
```

🔹 **Output:**
```
  Sensor  Værdi Enhed
1   Tryk  1013  hPa
```

✅ **Nu kan vi filtrere data baseret på værdier!**  

---

## 🛠 **Trin 3.1: Filtrér flere betingelser**
Hvis vi vil **kombinere flere betingelser**, kan vi bruge `&` (og) eller `|` (eller).

```python
filtered_df = df[(df["Værdi"] > 100) & (df["Sensor"] == "Tryk")]
print(filtered_df)
```

✅ **Nu filtrerer vi kun data, hvor "Værdi" er over 100 og "Sensor" er "Tryk"!**  

---

## 📌 **Trin 3.2: Vælg specifikke kolonner efter filtrering**
Vi kan **filtrere rækker og samtidig vælge bestemte kolonner**.

```python
filtered_df = df.loc[df["Værdi"] > 100, ["Sensor", "Værdi"]]
print(filtered_df)
```

✅ **Nu har vi filtreret data og beholdt kun de relevante kolonner!**  

---

## 🏷 **Trin 3.3: Filtrér ved hjælp af `query()`**
En anden måde at filtrere data på er **`query()`**, som minder om SQL.

```python
filtered_df = df.query("Værdi > 100 and Sensor == 'Tryk'")
print(filtered_df)
```

✅ **Nu har vi filtreret data ved hjælp af en SQL-lignende forespørgsel!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Filtreret rækker **baseret på én betingelse**  
✔️ Kombineret **flere betingelser**  
✔️ Udvalgt **specifikke kolonner efter filtrering**  
✔️ Brugt **SQL-lignende forespørgsel med `query()`**  

🚀 **Nu kan du filtrere data fleksibelt i Pandas!**   

---

## ✂️ **Trin 4: Slice data**
Slicing bruges til **at vælge en del af DataFrame'en**, enten **rækker, kolonner eller begge dele**.

### 🔹 **Generelt format for slicing i Pandas**
```python
df.loc[row_selection, column_selection]
df.iloc[row_index_selection, column_index_selection]
df[column_selection]  # Hurtig kolonnevalg
```

| Metode | Beskrivelse |
|--------|------------|
| `df.loc[rows, columns]` | Slicing baseret på rækker og kolonnenavne |
| `df.iloc[row_index, column_index]` | Slicing baseret på numeriske indeks |
| `df[["Kol1", "Kol2"]]` | Hurtig måde at vælge specifikke kolonner |

### 📄 **Eksempel: Vælg specifikke kolonner**
```python
subset = df.loc[:, ["Sensor", "Værdi"]]  # Vælg kun Sensor og Værdi-kolonner
print(subset)
```

✅ **Nu har vi udvalgt specifikke kolonner!**  

---

## 📌 **Trin 4.1: Slice bestemte rækker**
Vi kan **vælge specifikke rækker** baseret på indeks.

```python
subset = df.loc[0:1, :]  # Vælg de første to rækker
print(subset)
```

✅ **Nu har vi udvalgt de første to rækker!**  

---

## 🔢 **Trin 4.2: Slice data baseret på indeksnumre**
Vi kan også bruge `iloc` til **numerisk slicing**.

```python
subset = df.iloc[0:2, 1:3]  # Vælg rækker 0-1 og kolonner 1-2
print(subset)
```

✅ **Nu har vi valgt rækker og kolonner baseret på numeriske indeks!**  

---

## 🏷 **Trin 4.3: Slice hver anden række**
Hvis vi vil vælge **hver anden række**, kan vi bruge `step`.

```python
subset = df.iloc[::2, :]  # Vælg hver anden række
print(subset)
```

✅ **Nu har vi udvalgt hver anden række i datasættet!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Udvalgt **specifikke kolonner**  
✔️ Udvalgt **specifikke rækker**  
✔️ Brugt **numerisk slicing med `iloc`**  
✔️ Udvalgt **hver anden række**  

🚀 **Nu kan du bruge slicing til at vælge præcis de data, du har brug for!**  

---

## 🔄 **Trin 5: Flyt kolonner og rækker**
Nogle gange vil vi **ændre rækkefølgen af kolonner eller rækker** for at få en bedre struktur.

### 🔹 **Generelt format for omarrangering af kolonner**
```python
df = df[["Kol1", "Kol2", "Kol3"]]  # Angiv den ønskede rækkefølge
```

### 📄 **Eksempel: Omarranger kolonner**
```python
# Omarranger kolonner
df = df[["Værdi", "Sensor", "Enhed"]]
print(df)
```

✅ **Nu har vi ændret kolonnernes rækkefølge!**  

---

## 🔄 **Trin 5.1: Omarranger rækker**
Vi kan også ændre rækkefølgen af **rækker**.

```python
df = df.sort_values(by="Værdi", ascending=False)  # Sortér rækker baseret på værdier
print(df)
```

✅ **Nu har vi sorteret rækkerne baseret på en kolonne!**  

---

## ➕ **Trin 6: Tilføj og fjern kolonner og rækker**
Vi kan **tilføje eller fjerne data** dynamisk i en DataFrame.

### 📌 **Tilføj en ny kolonne**
```python
df["Kalibreret"] = df["Værdi"] * 1.05  # Opret en ny kolonne baseret på en beregning
print(df)
```

✅ **Nu har vi tilføjet en ny kolonne!**  

---

## ❌ **Trin 6.1: Fjern en kolonne**
Vi kan **fjerne en kolonne** fra DataFrame.

```python
df = df.drop(columns=["Enhed"])
print(df)
```

✅ **Nu har vi fjernet en kolonne!**  

---

## ➕ **Trin 6.2: Tilføj en ny række**
Vi kan også tilføje **en ny række** til vores DataFrame.

```python
ny_række = pd.DataFrame({"Sensor": ["Luft"], "Værdi": [80], "Enhed": ["%"]}, index=[len(df)])
df = pd.concat([df, ny_række])
print(df)
```

✅ **Nu har vi tilføjet en ny række!**  

---

## ❌ **Trin 6.3: Fjern en række**
For at **slette en række**, kan vi bruge `drop()`.

```python
df = df.drop(index=[0])  # Fjern række med indeks 0
print(df)
```

✅ **Nu har vi fjernet en række!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Flyttet **kolonner og rækker**  
✔️ Tilføjet en **ny kolonne** baseret på beregning  
✔️ Fjernet **kolonner og rækker** dynamisk  
✔️ Tilføjet **en ny række til DataFrame**  

🚀 **Nu kan du arbejde fleksibelt med kolonner og rækker i Pandas!**  

---

## 🔄 **Trin 7: Transponér en DataFrame**
Vi kan **bytte rækker og kolonner** i en DataFrame ved at bruge `.T`, som transponerer data.

### 🔹 **Generelt format for transponering**
```python
df.T
```

| Metode | Beskrivelse |
|--------|------------|
| `df.T` | Bytter rækker og kolonner i en DataFrame |

### 📄 **Eksempel: Transponér en DataFrame**
```python
df_T = df.T
print(df_T)
```

🔹 **Output:**
```
              0     1     2
Værdi      22.5  1013  45.0
Sensor    Temp  Tryk  Fugt
Kalibreret  23.6  1063.65  47.25
```

✅ **Nu har vi transponeret en DataFrame!**  

---

## 🏷 **Trin 7.1: Transponér og beholde et pænt format**
Når vi transponerer, kan vi bruge `.reset_index()` for at **gøre DataFrame mere læsbar**.

```python
df_T = df.T.reset_index()
print(df_T)
```

✅ **Nu er transponeringen mere struktureret!**  

---

## 🛠 **Trin 7.2: Transponér en del af DataFrame**
Hvis vi kun vil transponere **udvalgte kolonner**, kan vi gøre det sådan:

```python
df_T = df[["Sensor", "Værdi"]].T
print(df_T)
```

✅ **Nu har vi transponeret kun en del af DataFrame!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Transponeret en **hel DataFrame**  
✔️ Brug af **reset_index()** for at bevare strukturen  
✔️ Udvalgt **specifikke kolonner til transponering**  

🚀 **Nu kan du fleksibelt transponere data i Pandas!**  
---

## ✅ **Hvad har vi opnået?**
✔️ Åbnet og gemt data i Pandas  
✔️ Filtreret og slicet data  
✔️ Flyttet rækker og kolonner  
✔️ Tilføjet og fjernet kolonner/rækker  
✔️ Transponeret en DataFrame  

🔜 **Fortsæt til næste modul:** [03-import-export.md](03-import-export.md), hvor vi lærer at **arbejde med eksterne datakilder**!  
