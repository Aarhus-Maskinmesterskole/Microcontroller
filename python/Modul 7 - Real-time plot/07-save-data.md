# 💾 **Modul 7: Gem og hent realtidsdata**

## 📌 **1️⃣ Hvorfor gemme realtidsdata?**
Når vi arbejder med realtidsmålinger fra **DHT22**, kan vi gemme data for at:  

✅ **Analysere historiske målinger**  
✅ **Fejlsøge unormale værdier**  
✅ **Træne maskinlæringsmodeller**  

Vi gemmer data i **CSV-format**, så vi kan **åbne og analysere dem senere**.  

---

## 📌 **2️⃣ Tilføj automatisk lagring af data**
Vi udvider vores Python-kode, så **hvert datapunkt gemmes i en CSV-fil**.

```python
import serial
import pandas as pd
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 115200)  # Udskift med din serielle port
df = pd.DataFrame(columns=["Tid", "Temperatur", "Fugtighed"])

plt.ion()  # Aktiver interaktiv tilstand

while True:
    try:
        linje = ser.readline().decode("utf-8").strip().split(",")
        df.loc[len(df)] = [int(linje[0]), float(linje[1]), float(linje[2])]

        # Gem data til CSV uden at overskrive gamle data
        df.to_csv("dht22_data.csv", mode="a", index=False, header=False)

        plt.clf()  # Rens grafen før vi tegner igen
        plt.plot(df["Tid"], df["Temperatur"], marker="o", linestyle="-", label="Temperatur")
        plt.plot(df["Tid"], df["Fugtighed"], marker="s", linestyle="-.", label="Fugtighed")

        plt.xlabel("Tid")
        plt.ylabel("Målinger")
        plt.title("Realtidsplot af temperatur og fugtighed")
        plt.legend()
        plt.pause(1)  # Opdater grafen hvert sekund

    except Exception as e:
        print("Fejl ved læsning af data:", e)
```

✅ **Nu bliver alle målinger gemt i `dht22_data.csv`!**  

---

## 📌 **3️⃣ Initialiser CSV-filen med overskrifter**
Når vi gemmer data, ønsker vi **kun én gang at skrive kolonnenavne**.  
Dette kan vi sikre ved at tjekke, om filen allerede eksisterer.  

```python
import os

filnavn = "dht22_data.csv"

# Hvis filen ikke findes, skriv kolonneoverskrifter
if not os.path.exists(filnavn):
    df.to_csv(filnavn, mode="w", index=False, header=True)
else:
    df.to_csv(filnavn, mode="a", index=False, header=False)
```

✅ **Nu har vi sikret, at CSV-filen altid starter korrekt!**  

---

## 📌 **4️⃣ Hent og analyser gemte data**
For at **åbne de gemte data senere**, kan vi bruge Pandas:

```python
df = pd.read_csv("dht22_data.csv")
print(df.head())  # Se de første rækker
```

✅ **Nu kan vi hente de gemte målinger til analyse!**  

---

## 📌 **5️⃣ Fejlfinding**
🔹 **"CSV-filen overskrives"**  
➡️ Brug `mode="a"` i stedet for `mode="w"`.  

🔹 **"Filen har ingen overskrifter"**  
➡️ Sørg for, at du **kun tilføjer overskrifter første gang**.  

🔹 **"Jeg kan ikke åbne filen"**  
➡️ Sørg for, at Python-programmet ikke kører, når du forsøger at åbne den i Excel.  

✅ **Nu kan vi gemme og hente realtidsmålinger korrekt!**  

🚀 **Fortsæt til næste modul: [08-advanced-plot.md](08-advanced-plot.md)**  
