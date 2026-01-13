# 🧹 Modul 4: Rensning og filtrering af måledata

## 📌 **Introduktion**
Rensning af data er vigtigt, især i **industrielle systemer**, hvor vi ofte har **manglende værdier, dubletter eller fejlmålinger**.  
I dette modul lærer vi at **finde, rette og filtrere fejlbehæftede data** i Pandas.

🔗 **Forrige modul:** [03-import-export.md](03-import-export.md)  
🔜 **Næste modul:** [05-time-series.md](05-time-series.md)  

---

## ✅ **Trin 1: Find og håndtér manglende værdier**
Mange datasæt har **manglende værdier**. Vi kan identificere dem med:

### 🔹 **Generelt format for at identificere manglende værdier**
```python
df.isnull()  # Returnerer en boolsk DataFrame, hvor True betyder manglende værdi
df.notnull()  # Returnerer det modsatte af isnull()
df.isnull().sum()  # Optæller manglende værdier pr. kolonne
```

---

## 📄 **Eksempel: Find manglende værdier**
```python
import pandas as pd

# Opret et datasæt med manglende værdier
data = {
    "Sensor": ["Temp", "Tryk", "Fugt", "Luft"],
    "Værdi": [22.5, None, 45, 80],
    "Enhed": ["C", "hPa", "%", None]
}

df = pd.DataFrame(data)

print(df.isnull())  # Se hvor værdier mangler
```

🔹 **Output:**
```
   Sensor  Værdi  Enhed
0   False  False  False
1   False   True  False
2   False  False  False
3   False  False   True
```

✅ **Nu kan vi se, hvilke data der mangler!**  

---

## ❌ **Trin 1.1: Fjern rækker med manglende værdier**
Hvis vi vil **fjerne rækker med manglende værdier**, kan vi bruge `dropna()`.

```python
df_clean = df.dropna()
print(df_clean)
```

✅ **Nu har vi fjernet alle rækker med manglende værdier!**  

---

## 🛠 **Trin 1.2: Erstat manglende værdier med en standardværdi**
I stedet for at fjerne rækker, kan vi **udfylde de manglende værdier**.

```python
df_filled = df.fillna({"Værdi": df["Værdi"].mean(), "Enhed": "N/A"})
print(df_filled)
```

✅ **Nu har vi erstattet de manglende værdier!**  

---

## 🔄 **Trin 1.3: Erstat manglende værdier med forrige værdi**
Nogle gange ønsker vi at **udfylde manglende værdier med den forrige registrerede værdi**.

```python
df_ffill = df.fillna(method="ffill")
print(df_ffill)
```

✅ **Nu har vi udfyldt de manglende værdier med den forrige måling!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Identificeret **hvor data mangler**  
✔️ Fjernet **rækker med manglende værdier**  
✔️ Udfyldt **manglende data med standardværdier**  
✔️ Anvendt **forrige værdi til at udfylde huller**  

🚀 **Nu kan du håndtere manglende værdier fleksibelt i Pandas!**  

---

## 🛠 **Trin 2: Erstat manglende værdier**
Vi kan enten **slette** rækker med manglende værdier eller **udfylde dem** med en standardværdi.

### 🔹 **Generelt format for `fillna()`**
```python
df.fillna(value, method, axis, inplace)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `value` | En bestemt værdi eller dictionary med værdier til at udfylde manglende data | `None` |
| `method` | `"ffill"` for at udfylde med forrige værdi, `"bfill"` for næste værdi | `None` |
| `axis` | `0` for at udfylde rækker, `1` for at udfylde kolonner | `0` |
| `inplace` | Hvis `True`, opdaterer DataFrame direkte | `False` |

---

## 📄 **Eksempel: Erstat manglende værdier med en standardværdi**
```python
df_filled = df.fillna({"Værdi": df["Værdi"].mean(), "Enhed": "N/A"})
print(df_filled)
```

🔹 **Output:**
```
  Sensor  Værdi Enhed
0   Temp   22.5     C
1   Tryk   49.2   hPa
2   Fugt   45.0     %
3   Luft   80.0   N/A
```

✅ **Nu har vi erstattet de manglende værdier!**  

---

## 🔄 **Trin 2.1: Erstat manglende værdier med forrige værdi (`ffill`)**
Hvis vi vil **udfylde manglende værdier med den forrige registrerede værdi**, kan vi bruge `"ffill"`.

```python
df_ffill = df.fillna(method="ffill")
print(df_ffill)
```

✅ **Nu har vi udfyldt de manglende værdier med den forrige måling!**  

---

## 🔄 **Trin 2.2: Erstat manglende værdier med næste værdi (`bfill`)**
Hvis vi vil **udfylde manglende værdier med den næste registrerede værdi**, kan vi bruge `"bfill"`.

```python
df_bfill = df.fillna(method="bfill")
print(df_bfill)
```

✅ **Nu har vi udfyldt de manglende værdier med den næste tilgængelige måling!**  

---

## ❌ **Trin 2.3: Fjern rækker med manglende værdier**
Hvis vi i stedet for at udfylde vil **fjerne rækker med manglende værdier**, bruger vi `dropna()`.

```python
df_clean = df.dropna()
print(df_clean)
```

✅ **Nu har vi fjernet rækker med manglende værdier!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Erstattet **manglende værdier med en standardværdi**  
✔️ Udfyldt **manglende værdier med forrige eller næste måling**  
✔️ Fjernet **rækker med manglende værdier**  

🚀 **Nu kan du håndtere manglende værdier fleksibelt i Pandas!**  

---

## 🔍 **Trin 3: Fjern dubletter**
Nogle gange har vi **gentagne målinger**, som vi vil fjerne.

### 🔹 **Generelt format for `drop_duplicates()`**
```python
df.drop_duplicates(subset, keep, inplace)
```

| Argument | Beskrivelse | Standardværdi |
|----------|------------|---------------|
| `subset` | Vælg specifikke kolonner til at identificere dubletter | `None` (alle kolonner bruges) |
| `keep` | `"first"` beholder første, `"last"` beholder sidste, `False` fjerner alle dubletter | `"first"` |
| `inplace` | Hvis `True`, opdaterer DataFrame direkte | `False` |

---

## 📄 **Eksempel: Fjern dubletter i hele DataFrame**
```python
df = pd.DataFrame({
    "Sensor": ["Temp", "Tryk", "Fugt", "Temp"],
    "Værdi": [22.5, 1013, 45, 22.5]
})

df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)
```

✅ **Nu har vi fjernet dubletter!**  

---

## 🎯 **Trin 3.1: Fjern dubletter baseret på en bestemt kolonne**
Hvis vi vil **fjerne dubletter baseret på én specifik kolonne**, kan vi bruge `subset`.

```python
df_no_duplicates = df.drop_duplicates(subset=["Sensor"])
print(df_no_duplicates)
```

✅ **Nu har vi kun beholdt én række pr. unikke sensor!**  

---

## 🔄 **Trin 3.2: Behold kun den sidste forekomst af dubletter**
Som standard beholder Pandas **den første forekomst af en dublet**.  
Hvis vi i stedet vil beholde **den sidste forekomst**, kan vi ændre `keep="last"`.

```python
df_no_duplicates = df.drop_duplicates(keep="last")
print(df_no_duplicates)
```

✅ **Nu har vi fjernet dubletter, men beholdt den sidste forekomst!**  

---

## ❌ **Trin 3.3: Fjern alle forekomster af dubletter**
Hvis vi vil fjerne **alle rækker med dubletter**, kan vi sætte `keep=False`.

```python
df_no_duplicates = df.drop_duplicates(keep=False)
print(df_no_duplicates)
```

✅ **Nu har vi fjernet alle dubletter helt!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Fjernet **alle dubletter i hele DataFrame**  
✔️ Fjernet **dubletter baseret på en specifik kolonne**  
✔️ Beholdt **enten første eller sidste forekomst af en dublet**  
✔️ Fjernet **alle forekomster af dubletter**  

🚀 **Nu kan du håndtere dubletter fleksibelt i Pandas!**  

---

## ✂️ **Trin 4: Fjern ekstreme målinger**
Målefejl kan føre til **ekstremt høje eller lave værdier**. Vi kan filtrere dem fra.

### 🔹 **Generelt format for filtrering af ekstreme værdier**
```python
df[(df["kolonne"] > min_værdi) & (df["kolonne"] < max_værdi)]
```

| Metode | Beskrivelse |
|--------|------------|
| `df[df["Værdi"] > 10]` | Behold kun værdier over 10 |
| `df[df["Værdi"] < 1000]` | Behold kun værdier under 1000 |
| `df[(df["Værdi"] > 10) & (df["Værdi"] < 1000)]` | Behold værdier mellem 10 og 1000 |

---

## 📄 **Eksempel: Fjern ekstremt lave eller høje værdier**
```python
df_filtered = df[(df["Værdi"] > 10) & (df["Værdi"] < 1000)]
print(df_filtered)
```

✅ **Nu har vi filtreret ekstreme værdier væk!**  

---

## 🔄 **Trin 4.1: Identificér ekstreme værdier med statistiske metoder**
En anden metode er at bruge **standardafvigelse** eller **percentiler** til at identificere ekstreme værdier.

```python
mean = df["Værdi"].mean()
std_dev = df["Værdi"].std()

df_filtered = df[(df["Værdi"] > mean - 3 * std_dev) & (df["Værdi"] < mean + 3 * std_dev)]
print(df_filtered)
```

✅ **Nu har vi fjernet ekstreme værdier ved hjælp af statistik!**  

---

## 🎯 **Trin 4.2: Fjern ekstreme værdier baseret på percentiler**
Vi kan også bruge **percentiler** til at definere ekstremer.

```python
lower_bound = df["Værdi"].quantile(0.05)  # 5%-percentilen
upper_bound = df["Værdi"].quantile(0.95)  # 95%-percentilen

df_filtered = df[(df["Værdi"] > lower_bound) & (df["Værdi"] < upper_bound)]
print(df_filtered)
```

✅ **Nu har vi fjernet ekstreme værdier baseret på percentiler!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Filtreret **ekstreme værdier ud fra faste grænser**  
✔️ Identificeret **ekstreme værdier ved hjælp af standardafvigelse**  
✔️ Fjernet **ekstreme værdier ved hjælp af percentiler**  

🚀 **Nu kan du håndtere ekstreme værdier fleksibelt i Pandas!**  *  

---

# ✅ **Hvad har vi opnået?**
✔️ Fundet og håndteret **manglende værdier**  
✔️ Fjernet **dubletter** i data  
✔️ Filtreret **ekstreme målinger**  
✔️ Gjort data **klar til analyse**  

🔜 **Fortsæt til næste modul:** [05-time-series.md](05-time-series.md), hvor vi lærer **at håndtere tidsserier og log-data**!  
