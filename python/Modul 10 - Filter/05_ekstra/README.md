# ➕ Modul 05 – Ekstra og Udvidelser (valgfrit)

Dette modul giver dig mulighed for at udforske mere avancerede eller alternative måder at arbejde med dine ESP32-data. Du vælger selv, hvilke dele du vil arbejde videre med – perfekt til nysgerrige og dem, der vil tage det et skridt videre.

---

## 🎯 Formål

✔️ Udforske muligheder for webvisualisering  
✔️ Lære at logge data i realtid til CSV eller database  
✔️ Eksperimentere med widgets og brugerinteraktion i plot  
✔️ Gøre dine løsninger mere robuste og fleksible

---

## 🌐 Webbaseret visualisering

Brug f.eks. `Plotly Dash`, `Streamlit` eller `Flask` til at opbygge en web-GUI, hvor du kan vise sensordata i realtid.

```bash
pip install streamlit
```

Eksempel:
```python
# streamlit_app.py
import streamlit as st
import pandas as pd

st.title("Live Data fra ESP32")
data = pd.read_csv("data.csv")
st.line_chart(data["temp"])
```

Kør appen:
```bash
streamlit run streamlit_app.py
```

---

## 💾 Realtids datalogning

Udvid dit realtidsplot-script til også at skrive til en `.csv`-fil:
```python
with open("log.csv", "a") as f:
    f.write(f"{timestamp},{temp},{humidity}\n")
```

Du kan også eksperimentere med databaser som SQLite eller InfluxDB.

---

## 🎛️ Interaktive plots

Brug widgets fra `matplotlib.widgets` til at lave sliders og knapper:
- Skift vinduesstørrelse på glidende gennemsnit live
- Tænd/sluk for visning af rå data vs. filtreret

---

## 🧠 Forslag til fordybelse

- Undersøg hvordan du kunne vise data via et dashboard i browseren
- Tilføj konfigurationsfil (JSON eller TOML) så parametre kan ændres uden at ændre kode
- Brug `argparse` til at gøre din Python-applikation mere fleksibel
- Skriv en README til dit mini-projekt og del det på GitHub

---

✅ Når du har udforsket nogle af disse udvidelser, og har lyst til at gå i dybden med signalfiltrering, så fortsæt til næste modul: [`06_signalfiltrering`](../06_signalfiltrering/)

