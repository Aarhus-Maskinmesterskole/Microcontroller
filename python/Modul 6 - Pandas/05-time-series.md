# ⏳ Modul 5: Håndtering af tidsserier i Pandas

## 📌 **Introduktion**
Mange sensordata og logs indeholder **tidsstempler**, som kræver specielle teknikker til analyse.  
I dette modul lærer vi at **håndtere og analysere tidsserier** i Pandas.

🔗 **Forrige modul:** [04-data-cleaning.md](04-data-cleaning.md)  
🔜 **Næste modul:** [06-realtime-processing.md](06-realtime-processing.md)  

---

## ✅ **Trin 1: Konverter en kolonne til datetime**
Hvis vores data indeholder **tidsstempler som tekst**, kan vi konvertere dem til **datetime-format**.

### 🔹 **Generelt format for `pd.to_datetime()`**
```python
df["kolonne"] = pd.to_datetime(df["kolonne"], format, errors, utc)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `format` | Angiver datoformat, fx `"%Y-%m-%d %H:%M"` | Automatisk detekteret |
| `errors` | `"raise"` for fejl, `"coerce"` for at konvertere fejl til NaT, `"ignore"` for ingen ændring | `"raise"` |
| `utc` | Konverterer tid til UTC-format | `False` |

---

## 📄 **Eksempel: Konverter en kolonne til datetime**
```python
import pandas as pd

data = {
    "Tidspunkt": ["2024-03-01 12:00", "2024-03-01 12:05", "2024-03-01 12:10"],
    "Temperatur": [22.5, 22.7, 22.6]
}

df = pd.DataFrame(data)

# Konverter Tidspunkt-kolonnen til datetime
df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"])

print(df.dtypes)  # Bekræft, at kolonnen er konverteret
```

✅ **Nu har vi omdannet tidsdata til datetime-format!**  

---

## 📆 **Trin 1.1: Konverter datetime med et specifikt format**
Hvis tidsformatet ikke genkendes automatisk, kan vi angive det manuelt.

```python
df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"], format="%Y-%m-%d %H:%M")
```

✅ **Nu har vi konverteret datoformatet eksplicit!**  

---

## ❌ **Trin 1.2: Håndtér fejl i tidsdata**
Hvis vi har **forkerte datoer**, kan vi undgå fejl ved at bruge `errors="coerce"`.

```python
df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"], errors="coerce")
```

✅ **Nu bliver ugyldige datoer konverteret til NaT (Not a Time)!**  

---

## 🌍 **Trin 1.3: Konverter tid til UTC**
Hvis vi vil **arbejde med tidszoner**, kan vi konvertere til UTC.

```python
df["Tidspunkt"] = pd.to_datetime(df["Tidspunkt"], utc=True)
```

✅ **Nu er tiden omdannet til UTC!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Konverteret **tidsstempler fra tekst til datetime**  
✔️ Angivet **specifikt datoformat**  
✔️ Håndteret **ugyldige datoer uden fejl**  
✔️ Konverteret **tid til UTC-format**  

🚀 **Nu kan du arbejde effektivt med tidsdata i Pandas!**  

---

## ⏱ **Trin 2: Indstil en datetime-kolonne som index**
Når vi arbejder med tidsserier, er det en god idé at bruge **tidspunktet som index**.

### 🔹 **Generelt format for `set_index()`**
```python
df.set_index("kolonne", inplace=True)
```

| Metode | Beskrivelse |
|--------|------------|
| `df.set_index("Tidspunkt")` | Sætter en kolonne som index |
| `df.reset_index()` | Fjerner index og gør det til en kolonne igen |

---

## 📄 **Eksempel: Indstil en datetime-kolonne som index**
```python
df.set_index("Tidspunkt", inplace=True)
print(df)
```

✅ **Nu har vi et tidsserie-index!**  

---

## 📌 **Trin 2.1: Tjek om index er datetime**
For at sikre, at indexet er i datetime-format, kan vi kontrollere typen.

```python
print(type(df.index))
```

🔹 **Output:**  
```
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
```

✅ **Nu ved vi, at vores index er datetime!**  

---

## 🔄 **Trin 2.2: Nulstil index**
Hvis vi vil fjerne datetime som index og konvertere det tilbage til en kolonne, bruger vi `reset_index()`.

```python
df.reset_index(inplace=True)
```

✅ **Nu er datetime-kolonnen tilbage i DataFrame!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Sat **datetime-kolonnen som index**  
✔️ Kontrolleret **om index er datetime**  
✔️ Lært at **nulstille index til en kolonne igen**  

🚀 **Nu kan du arbejde med tidsserier i Pandas!**  

---

## 📆 **Trin 3: Resample data (ændr tidsinterval)**
Nogle gange vil vi **aggregere data over større tidsintervaller**, fx per minut, time eller dag.  
Dette hjælper med **at reducere støj i data og gøre analyser mere overskuelige**.

### 🔹 **Generelt format for `resample()`**
```python
df.resample("frekvens").agg(aggregationsmetode)
```

| Metode | Beskrivelse |
|--------|------------|
| `df.resample("10T").mean()` | Beregn gennemsnit i 10-minutters intervaller |
| `df.resample("H").sum()` | Summer værdier i hele timer |
| `df.resample("D").max()` | Find den højeste værdi per dag |
| `df.resample("W").min()` | Find den laveste værdi per uge |

🔹 **Almindelige tidsfrekvenser i `resample()`**:  
- `"S"` = Sekund  
- `"T"` = Minut  
- `"H"` = Time  
- `"D"` = Dag  
- `"W"` = Uge  
- `"M"` = Måned  

---

## 📄 **Eksempel: Aggregér data i 10-minutters intervaller**
```python
df_resampled = df.resample("10T").mean()  # Gruppér i 10-minutters intervaller
print(df_resampled)
```

✅ **Nu har vi ændret tidsopløsningen i vores data!**  

---

## 🔄 **Trin 3.1: Beregn flere aggregater samtidig**
Vi kan beregne **flere statistikværdier** på én gang.

```python
df_resampled = df.resample("H").agg(["mean", "max", "min"])
print(df_resampled)
```

✅ **Nu har vi beregnet gennemsnit, maksimum og minimum per time!**  

---

## 🔁 **Trin 3.2: Brug interpolering efter resampling**
Nogle gange kan resampling skabe **manglende værdier**. Vi kan udfylde dem med interpolering.

```python
df_resampled = df.resample("5T").mean().interpolate()
print(df_resampled)
```

✅ **Nu har vi udfyldt manglende værdier med interpolering!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Aggregér data til **større tidsintervaller**  
✔️ Beregnet **flere statistiske mål på én gang**  
✔️ Håndteret **manglende værdier med interpolering**  

🚀 **Nu kan du nemt ændre tidsopløsningen i Pandas!**  

---
## 🛠 **Trin 4: Hent data for en bestemt tidsperiode**
Når vi arbejder med tidsserier, er det ofte nødvendigt at **filtrere data for en specifik tidsperiode**.  
Dette gør det lettere at analysere en bestemt del af datasættet.

### 🔹 **Generelt format for at filtrere data efter tid**
```python
df.loc[start_tid:end_tid]
df[df.index >= start_tid]
df[df.index <= end_tid]
df[(df.index >= start_tid) & (df.index <= end_tid)]
```

| Metode | Beskrivelse |
|--------|------------|
| `df.loc[start:end]` | Henter data mellem to tidspunkter |
| `df[df.index >= start]` | Henter data fra et bestemt tidspunkt og frem |
| `df[df.index <= end]` | Henter data op til et bestemt tidspunkt |

---

## 📄 **Eksempel: Hent data mellem to tidspunkter**
```python
start = "2024-03-01 12:00"
end = "2024-03-01 12:05"

filtered_df = df.loc[start:end]
print(filtered_df)
```

✅ **Nu kan vi hente data for en given periode!**  

---

## ⏳ **Trin 4.1: Hent data for en bestemt dag**
Hvis vi vil **filtrere data for en specifik dag**, kan vi gøre dette:

```python
filtered_df = df.loc["2024-03-01"]
print(filtered_df)
```

✅ **Nu har vi hentet alle målinger for den valgte dag!**  

---

## 🔄 **Trin 4.2: Hent data inden for en tidsperiode**
Vi kan også bruge **betingelser** i stedet for `loc[]`.

```python
filtered_df = df[(df.index >= "2024-03-01 12:00") & (df.index <= "2024-03-01 12:05")]
print(filtered_df)
```

✅ **Nu har vi hentet data for et specifikt tidsinterval!**  

---

## 🎯 **Trin 4.3: Hent de seneste observationer**
Vi kan hurtigt hente **de seneste observationer** i tidsserien med `.last()`.

```python
df_last = df.last("5T")  # Henter de seneste 5 minutters data
print(df_last)
```

✅ **Nu har vi hentet de seneste målinger!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Filtreret data **mellem to tidspunkter**  
✔️ Hentet data **for en bestemt dag**  
✔️ Brug af **betingelser til filtrering**  
✔️ Hentet **de seneste målinger**  

🚀 **Nu kan du filtrere tidsdata fleksibelt i Pandas!**  

---

# ✅ **Hvad har vi opnået?**
✔️ Konverteret **tekst-tidstempler til datetime**  
✔️ Brugt **tidspunkt som index**  
✔️ Aggregere data ved **ændring af tidsopløsning**  
✔️ Filtreret data **baseret på tid**  

🔜 **Fortsæt til næste modul:** [06-realtime-processing.md](06-realtime-processing.md), hvor vi arbejder med **realtidsdataanalyse**!  
