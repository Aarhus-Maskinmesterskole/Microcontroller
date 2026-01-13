# 🚀 Modul 08: Avanceret Real-Tids Plotning med FuncAnimation

## 📌 1️⃣ Hvorfor bruge FuncAnimation?
Normalt bruger vi `plt.pause(1)` til at opdatere grafer i realtid.  
Men dette kan føre til **flickering (blinking)** og mindre effektiv opdatering.

✅ **Løsningen er FuncAnimation**, som opdaterer grafen jævnt uden flickering.

---

## 📌 2️⃣ Installation af nødvendige pakker
Hvis du ikke allerede har gjort det, installér Matplotlib og Pandas:

```bash
pip install matplotlib pandas
```
✅ Nu har vi alt klar til avanceret plotning!

---

## 📌 3️⃣ Python-kode til interaktiv realtidsgraf
Denne kode bruger FuncAnimation til at **opdatere grafen uden flickering**.

```python
import serial
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial("COM3", 115200)  # Udskift med din serielle port

df = pd.DataFrame(columns=["Tid", "Temperatur", "Fugtighed"])

fig, ax = plt.subplots()

def update(frame):
    global df

    # Læs serielle data
    linje = ser.readline().decode("utf-8").strip().split(",")
    df.loc[len(df)] = [int(linje[0]), float(linje[1]), float(linje[2])]

    # Behold kun de seneste 50 målinger
    df = df.iloc[-50:]

    ax.clear()  # Rens grafen før vi tegner igen
    ax.plot(df["Tid"], df["Temperatur"], marker="o", linestyle="-", label="Temperatur")
    ax.plot(df["Tid"], df["Fugtighed"], marker="s", linestyle="-.", label="Fugtighed")

    ax.set_xlabel("Tid")
    ax.set_ylabel("Målinger")
    ax.set_title("Interaktiv Realtidsplot af DHT22-data")
    ax.legend()
    plt.xticks(rotation=45)

# Start animationen
ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()
```
✅ Nu har vi en flicker-fri interaktiv realtidsgraf!

---

## 📌 4️⃣ Hvad gør FuncAnimation?
FuncAnimation **opdaterer grafen uden at blokere koden**, hvilket gør den mere jævn og responsiv.  
Den kører en funktion automatisk med faste intervaller for at holde grafen opdateret.

### 🔹 Hvordan fungerer FuncAnimation?
1️⃣ **Definér en opdateringsfunktion (`update()`)** der henter nye målinger og opdaterer grafen.  
2️⃣ **Opret en animation**, der kører `update()` med jævne intervaller.  
3️⃣ **Grafen opdateres uden flickering**, da `ax.clear()` rydder kun det nødvendige område.

### 🔹 Komponenter i FuncAnimation
| Funktion | Beskrivelse |
|----------|------------|
| `animation.FuncAnimation(fig, update, interval=1000)` | Kører `update()` hvert sekund |
| `update(frame)` | Henter nye data og opdaterer grafen |
| `ax.clear()` | Rydder kun den nuværende figur i stedet for hele plotten |
| `df.iloc[-50:]` | Beholder kun de sidste 50 målinger for bedre performance |
| `plt.xticks(rotation=45)` | Roterer x-aksens labels, så de er lettere at læse |
| `fig, ax = plt.subplots()` | Opretter en ny figur og akse for plottet |

---

## 📌 5️⃣ Forstå `update(frame)` og hvordan man tilføjer data til grafen
Funktionen `update(frame)` er **kernen i FuncAnimation**.  
Den henter nye data, opdaterer DataFrame, og tegner grafen igen.

### 🔹 Hvordan fungerer `update(frame)`?
1️⃣ **Læs nye data fra ESP32 via seriel port**.  
2️⃣ **Tilføj data til DataFrame med `df.loc[len(df)]`**.  
3️⃣ **Begræns DataFrame til de seneste `n` målinger** for bedre ydeevne.  
4️⃣ **Opdater grafen ved at tegne data på ny**.

```python
def update(frame):
    global df

    # Læs serielle data
    linje = ser.readline().decode("utf-8").strip().split(",")
    df.loc[len(df)] = [int(linje[0]), float(linje[1]), float(linje[2])]

    # Behold kun de seneste 50 målinger
    df = df.iloc[-50:]

    ax.clear()  # Rens grafen før vi tegner igen
    ax.plot(df["Tid"], df["Temperatur"], marker="o", linestyle="-", label="Temperatur")
    ax.plot(df["Tid"], df["Fugtighed"], marker="s", linestyle="-.", label="Fugtighed")

    ax.set_xlabel("Tid")
    ax.set_ylabel("Målinger")
    ax.set_title("Interaktiv Realtidsplot af DHT22-data")
    ax.legend()
    plt.xticks(rotation=45)
```

### 🔹 Hvorfor bruger vi `df.loc[len(df)]`?
`df.loc[len(df)]` tilføjer en ny række til DataFrame med de nyeste målinger.

| Metode | Beskrivelse |
|--------|------------|
| `df.loc[len(df)] = [tid, temp, fugt]` | Tilføjer en ny række med ny data |
| `df = df.iloc[-50:]` | Beholder kun de seneste 50 målinger |

✅ **Denne tilgang sikrer, at vi kun har de nyeste data uden at bruge for meget hukommelse!**

---

## 📌 6️⃣ Hvorfor bruge FuncAnimation i stedet for `plt.pause()`?
| Metode | Fordele | Ulemper |
|--------|---------|---------|
| `plt.pause()` | Let at bruge, fungerer til simple grafer | Kan forårsage flickering, blokering af koden |
| `FuncAnimation` | Glidende opdatering, ingen flickering, kan bruges med flere plots | Lidt mere kompleks opsætning |

✅ **FuncAnimation er den bedste metode til realtidsplotning!**

---

## 📌 7️⃣ Fejlfinding

### 🔹 "Grafen fryser"
➡️ Sørg for, at din **serielle port er korrekt**, og at ESP32 sender data.

### 🔹 "Grafen viser kun én måling"
➡️ Tilføj flere datapunkter med `df = df.iloc[-50:]`.

### 🔹 "Fejl: `ValueError: could not convert string to float`"
➡️ Sørg for, at ESP32 **sender kun numeriske værdier** (ikke `None` eller `" "`).

✅ Nu har vi optimeret vores realtidsgraf!

---

## 🚀 **Tillykke! Du har gennemført kurset!** 🎉
Du har nu lært at bruge FuncAnimation til **avanceret realtidsplotning**.  
✅ **Real-time opdatering af data uden flickering**  
✅ **Forståelse af FuncAnimation**  
✅ **Seriel kommunikation med ESP32**  

🔹 **Hvad kan du gøre som næste skridt?**
- Tilføj **et ekstra subplot** for at vise flere målinger.  
- Brug **Low-pass filtering** for at udglatte støj.  
- Send **data fra en anden sensor** som lufttryk.  

Tak for din deltagelse – og held og lykke med dine projekter! 🚀😊
