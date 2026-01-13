# 📊 **Real-time visualisering af PLC-data**

## 📌 **Formål**
I dette modul lærer du, hvordan du **læser PLC-data i real-time** og visualiserer det med **Matplotlib**.

---

## 🔗 **Trin 1: Installer nødvendige biblioteker**
Hvis du ikke allerede har Matplotlib installeret, kan du installere det med:

```sh
pip install matplotlib
```

---

## 🖥️ **Trin 2: Læs data fra PLC og plot real-time**
Vi bruger **Matplotlib’s FuncAnimation** til at opdatere grafen i real-time.

```python
import snap7
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from snap7.util import get_real

# PLC-indstillinger
PLC_IP = "192.168.0.1"
DB_NUMBER = 1
START_BYTE = 0

# Opret forbindelse til PLC
plc = snap7.client.Client()
plc.connect(PLC_IP, 0, 1)

# Liste til lagring af data
values = []

def read_plc_value():
    """ Læser en REAL-værdi fra PLC'en. """
    db_data = plc.db_read(DB_NUMBER, START_BYTE, 4)
    return get_real(db_data, 0)

def update(frame):
    """ Opdaterer plottet i real-time. """
    values.append(read_plc_value())
    if len(values) > 50:  # Begræns længden af dataserien
        values.pop(0)
    
    ax.clear()
    ax.plot(values, label="PLC Sensor Data")
    ax.set_xlabel("Tid (opdateringer)")
    ax.set_ylabel("Måleværdi")
    ax.legend()
    ax.grid()

# Opsæt Matplotlib
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=500)

plt.show()

plc.disconnect()
```

---

## ✅ **Test din kode**
Når du kører scriptet, vil du se en graf, der **opdateres i real-time** med værdier fra PLC’en.

---

## ⚠ **Fejlhåndtering**
Hvis du oplever problemer:
- **Sørg for, at din PLC er tændt** og tilsluttet netværket.  
- **Tjek PLC’s IP-adresse og datablock** i TIA Portal.  
- **Prøv at pinge PLC’en** for at sikre, at den svarer:

```sh
ping 192.168.0.1
```

---

## 🚀 **Næste trin**
✅ Du har nu real-time visualisering af PLC-data!  
Gå videre til næste modul: [📄 07-error-handling.md](07-error-handling.md) ⚠️
