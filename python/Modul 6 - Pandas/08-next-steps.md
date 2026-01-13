# 🚀 Modul 8: Udvidelser og næste skridt

## 📌 **Introduktion**
Nu hvor du har lært de grundlæggende funktioner i Pandas, er du klar til **mere avancerede analyser og integrationer**.  
Her er nogle idéer til, hvordan du kan bygge videre på det, du har lært.

🔗 **Forrige modul:** [07-visualization.md](07-visualization.md)  

---

## 📡 **1. Realtime streaming af data**
Hvis du arbejder med **IoT eller industrielle systemer**, kan du **streame data direkte fra sensorer** og analysere dem i Pandas.

### 🛠 **Mulige løsninger**
- **Brug MQTT** til at modtage live-data.  
- **Læs serielle data fra en ESP32 eller Arduino** via USB.  
- **Integrér med en database** for live-dataanalyse.  

📄 **Eksempel: Læs live-data fra en seriel port**
```python
import serial
import pandas as pd

ser = serial.Serial("COM3", 115200, timeout=1)  # Erstat COM3 med din port

df = pd.DataFrame(columns=["Tid", "Sensorværdi"])

while True:
    line = ser.readline().decode("utf-8").strip()
    if line:
        df = df.append({"Tid": pd.Timestamp.now(), "Sensorværdi": float(line)}, ignore_index=True)
        print(df.tail(1))  # Vis de seneste målinger
```

✅ **Nu kan du hente live-data fra en sensor og analysere det i Pandas!**  

---

## 📊 **2. Avanceret dataanalyse med Pandas**
Pandas har mange **statistiske funktioner**, som kan hjælpe med at analysere data **mere detaljeret**.

📄 **Eksempel: Udregn statistikker for målinger**
```python
print(df.describe())  # Giver middelværdi, min, max, std-afvigelse osv.
```

✅ **Nu kan du lave dybere analyser af dine data!**  

---

## 📈 **3. Avanceret visualisering med Seaborn**
Matplotlib er kraftfuld, men **Seaborn giver mere avancerede plots**.

```bash
pip install seaborn  # Installer Seaborn først
```

📄 **Eksempel: Brug Seaborn til avancerede plots**
```python
import seaborn as sns
sns.boxplot(x=df["Sensorværdi"])
```

✅ **Nu kan du lave mere avancerede visualiseringer!**  

---

## ✅ **Opsummering: Hvad kan du gøre nu?**
| 🚀 **Mulighed** | 🛠 **Hvad du lærer** |
|---------------|----------------|
| 📡 Stream data fra en sensor | IoT, MQTT, real-time Pandas |
| 📊 Udvid dataanalyse | Statistik, datamodellering |
| 📈 Brug avanceret visualisering | Seaborn, interaktive plots |
| 🏛 Integrér med databaser | SQL, data management |

---

## ✅ **Næste skridt**
Vælg en **udvidelse**, og begynd at bygge videre på dine Pandas-færdigheder! 🚀  

📢 **Har du lavet et spændende projekt?**  
👉 Del det med os i en **GitHub-repository eller en blogpost!** 🎉  
