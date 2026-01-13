# 📂 Modul 3: Import og eksport af data i Pandas

## 📌 **Introduktion**
Dette modul viser, hvordan du **importerer og eksporterer data i forskellige formater**.  
Vi lærer at arbejde med **CSV, Excel, JSON og SQL-databaser** i Pandas.

🔗 **Forrige modul:** [02-pandas-basics.md](02-pandas-basics.md)  
🔜 **Næste modul:** [04-data-cleaning.md](04-data-cleaning.md)  

---

## ✅ **Trin 1: Importér data fra en CSV-fil**
Pandas gør det nemt at **læse data fra CSV-filer**.

```python
import pandas as pd

# Læs en CSV-fil
df = pd.read_csv("sensor_data.csv")

print(df.head())  # Vis de første 5 rækker
```

✅ **Nu har vi indlæst en CSV-fil i Pandas!**  

---

## 📤 **Trin 2: Eksportér data til CSV**
Når vi har behandlet vores data, kan vi **gemme det igen i en CSV-fil**.

```python
df.to_csv("output.csv", index=False)
print("Data gemt til output.csv")
```

✅ **Nu har vi eksporteret vores data til en CSV-fil!**  

---

## 📥 **Trin 3: Importér data fra Excel**
Pandas understøtter også **Excel-filer**, hvis `openpyxl` er installeret.

### 🔹 **Installer nødvendige biblioteker**
Før vi kan læse Excel-filer, skal vi sikre os, at **openpyxl** eller **xlrd** er installeret.

```bash
pip install openpyxl  # Installer openpyxl til .xlsx filer
pip install xlrd      # Installer xlrd til gamle .xls filer
```

✅ **Nu har vi installeret de nødvendige biblioteker!**  

---

## 🔄 **Generelt format for `pd.read_excel()`**
```python
df = pd.read_excel(filepath, sheet_name, usecols, nrows, skiprows, dtype, parse_dates, engine)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `filepath` | Filnavn eller sti til Excel-filen | **Påkrævet** |
| `sheet_name` | Hvilket ark der skal indlæses (fx `"Ark1"`, `0` for første ark) | `0` |
| `usecols` | Udvalgte kolonner, der skal indlæses | `None` (henter alle) |
| `nrows` | Antal rækker, der skal indlæses | `None` (henter alle) |
| `skiprows` | Antal rækker, der skal springes over i starten | `0` |
| `dtype` | Angiver datatyper for kolonner | `None` (auto-detekteres) |
| `parse_dates` | Konverterer kolonner til datetime-format | `False` |
| `engine` | Parser-engine: `"openpyxl"` for .xlsx eller `"xlrd"` for .xls | Automatisk valgt |

---

## 📄 **Eksempel: Indlæs en hel Excel-fil**
```python
df = pd.read_excel("sensor_data.xlsx")
print(df.head())  # Vis de første 5 rækker
```

✅ **Nu har vi åbnet en Excel-fil i Pandas!**  

---

## 📌 **Trin 3.1: Indlæs data fra et specifikt ark**
Hvis en Excel-fil indeholder flere ark (sheets), kan vi vælge ét bestemt ark.

```python
df = pd.read_excel("sensor_data.xlsx", sheet_name="Ark2")
print(df.head())
```

✅ **Nu har vi indlæst data fra et specifikt ark!**  

---

## 🛠 **Trin 3.2: Indlæs kun bestemte kolonner**
Hvis vi kun vil hente **nogle kolonner**, kan vi bruge `usecols`.

```python
df = pd.read_excel("sensor_data.xlsx", usecols=["Sensor", "Værdi"])
print(df.head())
```

✅ **Nu har vi hentet udvalgte kolonner fra Excel!**  

---

## ⏳ **Trin 3.3: Indlæs kun et begrænset antal rækker**
Vi kan også begrænse **hvor mange rækker vi henter**.

```python
df = pd.read_excel("sensor_data.xlsx", nrows=5)  # Hent kun de første 5 rækker
print(df)
```

✅ **Nu har vi hentet kun de første 5 rækker!**  

---

## ❌ **Trin 3.4: Spring bestemte rækker over**
Hvis den øverste del af Excel-arket indeholder unødvendige oplysninger, kan vi **springe dem over**.

```python
df = pd.read_excel("sensor_data.xlsx", skiprows=2)  # Spring de første 2 rækker over
print(df.head())
```

✅ **Nu har vi sprunget overflødige rækker over!**  

---

## 📆 **Trin 3.5: Konverter en kolonne til datetime**
Hvis Excel-arket indeholder tidsstempler, kan vi **automatisk konvertere dem til datetime**.

```python
df = pd.read_excel("sensor_data.xlsx", parse_dates=["Tidspunkt"])
print(df.dtypes)  # Se datatyper
```

✅ **Nu har vi konverteret en kolonne til datetime!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Indlæst en **Excel-fil** med Pandas  
✔️ Udvalgt **specifikke ark, kolonner og rækker**  
✔️ Sprunget over **rækker ved indlæsning**  
✔️ Konverteret **tidsstempler automatisk**  

🚀 **Nu kan du arbejde fleksibelt med Excel-data i Pandas!**  *  

---

## 📤 **Trin 4: Eksportér data til Excel**
Hvis vi vil **gemme vores DataFrame som en Excel-fil**, kan vi gøre det sådan:

```python
df.to_excel("output.xlsx", index=False)
print("Data gemt til output.xlsx")
```

✅ **Nu har vi gemt data i en Excel-fil!**  

---

## 📤 **Trin 4: Eksportér data til Excel**
Hvis vi vil **gemme vores DataFrame som en Excel-fil**, kan vi gøre det sådan:

### 🔹 **Generelt format for `to_excel()`**
```python
df.to_excel(filepath, sheet_name, index, header, encoding, engine)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `filepath` | Filnavn eller sti, hvor Excel-filen gemmes | **Påkrævet** |
| `sheet_name` | Navnet på arket i Excel-filen | `"Sheet1"` |
| `index` | Om DataFrame-indekset skal gemmes i filen | `True` |
| `header` | Om kolonnenavne skal inkluderes i filen | `True` |
| `encoding` | Tegnsæt for filen (fx `"utf-8"`, `"latin1"`) | `"utf-8"` |
| `engine` | `"openpyxl"` for .xlsx eller `"xlsxwriter"` | Automatisk valgt |

---

## 📄 **Eksempel: Gem DataFrame som Excel**
```python
df.to_excel("output.xlsx", index=False)
print("Data gemt til output.xlsx")
```

✅ **Nu har vi gemt data i en Excel-fil!**  

---

## 📌 **Trin 4.1: Gem data til et specifikt ark**
Hvis vi vil **gemme data i et bestemt ark (sheet)** i Excel-filen:

```python
df.to_excel("output.xlsx", sheet_name="Målinger", index=False)
print("Data gemt til output.xlsx i 'Målinger'-arket!")
```

✅ **Nu har vi gemt data i et specifikt ark!**  

---

## ➕ **Trin 4.2: Tilføj flere ark til Excel-filen**
Vi kan også **gemme flere DataFrames i samme Excel-fil** ved hjælp af `ExcelWriter`.

```python
with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Målinger", index=False)
    df.describe().to_excel(writer, sheet_name="Statistik", index=True)
print("Data gemt med flere ark i output.xlsx!")
```

✅ **Nu har vi gemt flere ark i én Excel-fil!**  

---

## ❌ **Trin 4.3: Fjern indekset i Excel-filen**
Som standard gemmer `to_excel()` DataFrame-indekset i den første kolonne. Hvis vi **ikke ønsker dette**, kan vi fjerne det:

```python
df.to_excel("output.xlsx", index=False)
```

✅ **Nu har vi gemt data uden index!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Eksporteret en **DataFrame til en Excel-fil**  
✔️ Gemt **data i et bestemt ark**  
✔️ Oprettet **flere ark i samme Excel-fil**  
✔️ Fjernet **indeks fra Excel-output**  

🚀 **Nu kan du eksportere data til Excel på en fleksibel måde!**  

---

## 🌍 **Trin 5: Importér data fra JSON**
JSON er et **populært dataformat til webapplikationer og API'er**, som Pandas nemt kan håndtere.

### 🔹 **Generelt format for `pd.read_json()`**
```python
df = pd.read_json(filepath, orient, typ, convert_dates, encoding, lines)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `filepath` | Filnavn eller sti til JSON-filen | **Påkrævet** |
| `orient` | Hvordan JSON-strukturen er opbygget (`"records"`, `"split"`, `"index"`, `"columns"`) | `"columns"` |
| `typ` | `"frame"` for DataFrame eller `"series"` for Series | `"frame"` |
| `convert_dates` | Om Pandas automatisk skal konvertere datoer | `True` |
| `encoding` | Tegnsæt for filen (fx `"utf-8"`, `"latin1"`) | `"utf-8"` |
| `lines` | Om JSON-filen indeholder én JSON-objekt pr. linje | `False` |

---

## 📄 **Eksempel: Indlæs en JSON-fil**
```python
df = pd.read_json("sensor_data.json")
print(df.head())
```

✅ **Nu har vi indlæst data fra en JSON-fil!**  

---

## 📌 **Trin 5.1: JSON med `orient="records"`**
Nogle JSON-filer bruger `"records"`-formatet, hvor hver række er en liste af dictionaries:

```json
[
  {"Sensor": "Temp", "Værdi": 22.5, "Enhed": "C"},
  {"Sensor": "Tryk", "Værdi": 1013, "Enhed": "hPa"},
  {"Sensor": "Fugt", "Værdi": 45, "Enhed": "%"}
]
```

Vi kan læse denne type JSON med:

```python
df = pd.read_json("sensor_data.json", orient="records")
print(df.head())
```

✅ **Nu har vi indlæst JSON med `orient="records"`!**  

---

## 🛠 **Trin 5.2: Indlæs JSON med én linje pr. objekt (`lines=True`)**
Nogle JSON-filer indeholder **én linje pr. objekt**. Vi kan læse dem med `lines=True`.

Eksempel på JSON-linjeformat:
```json
{"Sensor": "Temp", "Værdi": 22.5, "Enhed": "C"}
{"Sensor": "Tryk", "Værdi": 1013, "Enhed": "hPa"}
{"Sensor": "Fugt", "Værdi": 45, "Enhed": "%"}
```

```python
df = pd.read_json("sensor_data.json", lines=True)
print(df.head())
```

✅ **Nu har vi indlæst JSON med `lines=True`!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Indlæst en **JSON-fil i Pandas**  
✔️ Arbejdet med **forskellige JSON-strukturer**  
✔️ Læst JSON med **"records" format**  
✔️ Håndteret JSON-linjeformat med `lines=True`  

🚀 **Nu kan du importere JSON-data i Pandas fleksibelt!**  

---

## 🏛 **Trin 7: Importér data fra en SQL-database**
Pandas kan også læse data fra en **SQL-database**, hvilket gør det let at håndtere store datasæt.

### 🔹 **Generelt format for `pd.read_sql()`**
```python
df = pd.read_sql(query, con, index_col, parse_dates)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `query` | SQL-forespørgsel, fx `"SELECT * FROM tabelnavn"` | **Påkrævet** |
| `con` | Forbindelse til databasen | **Påkrævet** |
| `index_col` | Hvilken kolonne der skal bruges som index | `None` |
| `parse_dates` | Konverterer kolonner til datetime-format | `False` |

---

## 📄 **Eksempel: Læs data fra en SQLite-database**
```python
import sqlite3
import pandas as pd

# Opret forbindelse til databasen
conn = sqlite3.connect("database.db")

# Læs data fra en tabel
df = pd.read_sql("SELECT * FROM sensors", conn)

print(df.head())
```

✅ **Nu har vi hentet data fra en SQL-database!**  

---

## 📌 **Trin 7.1: Indlæs kun specifikke kolonner**
Vi kan hente **kun udvalgte kolonner** fra databasen.

```python
df = pd.read_sql("SELECT Sensor, Værdi FROM sensors", conn)
print(df.head())
```

✅ **Nu har vi kun hentet kolonnerne "Sensor" og "Værdi"!**  

---

## 🛠 **Trin 7.2: Filtrér data ved SQL-forespørgsel**
Vi kan filtrere data direkte med SQL.

```python
df = pd.read_sql("SELECT * FROM sensors WHERE Værdi > 50", conn)
print(df.head())
```

✅ **Nu har vi kun hentet målinger over 50!**  

---

## 📆 **Trin 7.3: Konverter datoer fra SQL til datetime**
Hvis databasen har en **dato-kolonne**, kan vi konvertere den automatisk.

```python
df = pd.read_sql("SELECT * FROM sensors", conn, parse_dates=["Tidspunkt"])
print(df.dtypes)  # Se datatyper
```

✅ **Nu har vi konverteret datoer automatisk!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Indlæst en **SQL-tabel i Pandas**  
✔️ Udvalgt **specifikke kolonner fra databasen**  
✔️ Filtreret data **direkte i SQL-forespørgslen**  
✔️ Konverteret **dato-kolonner automatisk**  

🚀 **Nu kan du hente og arbejde med SQL-data i Pandas!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Importeret data fra **CSV, Excel, JSON og SQL**  
✔️ Eksporteret data til **CSV, Excel og JSON**  
✔️ Lært at **arbejde med eksterne datakilder i Pandas**  

🔜 **Fortsæt til næste modul:** [04-data-cleaning.md](04-data-cleaning.md), hvor vi lærer **at rense og filtrere måledata**!  
