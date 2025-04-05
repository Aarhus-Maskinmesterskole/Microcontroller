# 🏭 Workshop 5 – Snap7 læsning fra Siemens PLC med Python

## 🎯 Formål
I denne afsluttende workshop i modul 05 lærer du at forbinde Node-RED med en Siemens PLC via et Python-script, der benytter Snap7-biblioteket. Målet er at hente en værdi fra PLC’ens datablock og vise den i Node-RED. Dette er et klassisk eksempel på **IT/OT-integration**, hvor du trækker data fra en kontroller (OT) og gør den tilgængelig i visualisering eller videre behandling (IT).

Denne form for dataudveksling bruges i industriel automation, overvågning, datalogging og edge computing – og forståelsen herfor er central for både automationsteknologer og softwareingeniører, der arbejder med produktionssystemer.

Du lærer at:
- Bruge Snap7 til at læse en værdi fra PLC’ens datablock
- Forbinde Python med Node-RED via `exec`-noden
- Integrere realtidsmålinger fra PLC direkte i dit Node-RED-flow
- Fejlsøge typiske forbindelses- og kommunikationsfejl

---

## 🧰 Forudsætninger
For at kunne gennemføre denne workshop skal du have:
- ✅ Gennemført Workshops 1–4 og være fortrolig med `exec`-noden
- ✅ En Siemens PLC (fysisk, PLCSIM Advanced eller tilsvarende simulator)
- ✅ Adgang til netværket hvor PLC’en er tilgængelig
- ✅ Python 3.x installeret og fungerende
- ✅ Snap7 installeret med `pip install python-snap7`
- ✅ Kendskab til datablocks i TIA Portal

> 📌 Hvis du ikke har adgang til en fysisk PLC, kan Snap7 også bruges med simulering – fx PLCSIM Advanced. Det kræver dog korrekt netværksopsætning.

---

## ⚙️ Installation af Snap7
Første skridt er at sikre, at du har Snap7-biblioteket installeret. Kør følgende i terminalen (Linux/macOS) eller i kommandoprompt (Windows):

```bash
pip install python-snap7
```

### 🛠️ Fejlspecifik opsætning
- **Linux:** Det kan være nødvendigt at installere afhængigheder:
  ```bash
  sudo apt install build-essential
  ```
- **Windows:** Kræver muligvis Microsoft Visual C++ Redistributable (x64)
- Kontrollér installationen med:
  ```bash
  python -c "import snap7"
  ```
  Hvis der ikke kommer fejl, er du klar.

---

## 📝 Python-script: `snap7_read.py`
Gem følgende script i `scripts/`-mappen:
```python
import snap7
from snap7.util import get_real
from snap7.snap7types import S7WLByte

PLC_IP = "192.168.0.1"  # <- Opdater med din PLC's IP-adresse
DB_NUMBER = 1            # <- Dit datablock-nummer
START_ADDRESS = 0        # <- Offset i datablocken
LENGTH = 4               # <- 4 bytes til REAL (float)

client = snap7.client.Client()
client.connect(PLC_IP, 0, 1)

if client.get_connected():
    data = client.db_read(DB_NUMBER, START_ADDRESS, LENGTH)
    value = get_real(data, 0)
    print(value)
    client.disconnect()
else:
    print("Forbindelse til PLC mislykkedes")
```

📌 **OBS:**
- Brug `get_real()` til at aflæse en `REAL` (flydende tal) fra datablocken
- Alternativer: `get_int`, `get_bool`, `get_dword` til andre typer

---

## 🔧 Node-RED Flow

1. **`inject`-node**
   - Label: "Læs PLC-værdi"
   - Payload: tom, "timestamp" eller tekst (ignoreres)

2. **`exec`-node**
   - Kommando:
     ```bash
     python3 /fuld/sti/til/scripts/snap7_read.py
     ```
     _(eller på Windows: `python C:\sti\til\scripts\snap7_read.py`)_
   - Output: `return code + stdout`
   - Tilføj også `debug`-node til **stderr** (output 2)

3. **`debug`-node**
   - Tilslut til stdout (første output) på `exec`-noden
   - Navngiv den fx "PLC værdi fra Python"

> 💡 Du kan også sende resultatet videre til `ui_gauge`, CSV-logning eller MQTT

---

## 🧪 Test og validering
1. Opret et datablock i TIA Portal med fx `DB1.DBD0` som `REAL`
2. Initialiser værdien til fx `23.7`
3. Deploy dit flow og klik `inject`
4. Forventet output i debug-panelet:
```
23.7
```
5. Test også med ændrede værdier fra PLC’en – flowet bør returnere de opdaterede værdier

---

## 🛠️ Fejlfinding og diagnose
Hvis forbindelsen fejler, så tjek følgende:
- 📡 IP-adressen i scriptet matcher PLC’en
- 🔁 Du bruger rack `0`, slot `1` (gælder for S7-1200/1500)
- 🔐 PLC tillader kommunikation via Snap7 (Tjek "Protection settings")
- 🧱 Firewall og netværksforbindelse blokerer ikke port 102
- 📥 Datablock er downloadet til PLC og ikke i "optimized access only"-mode

---

## ✅ Læringsudbytte
Når du har gennemført denne workshop, kan du:
- Forstå og anvende Snap7 som kommunikationsbibliotek til Siemens PLC’er
- Læse en realtidsværdi fra en PLC’s datablock og bruge den i Node-RED
- Integrere industrielle data i dashboards, logfiler og visualiseringer
- Fejlsøge og tilpasse Python-scriptet til forskellige PLC-datatyper
- Bygge bro mellem PLC-baseret automation og dataanalyse/systemintegration

---

🔁 Tillykke! Du har nu gennemført hele Modul 05 – næste skridt kan være at lave et **mini-projekt**, hvor du kombinerer:
- Sensor- og seriel data fra ESP32 (Modul 01–04)
- PLC-data via Snap7
- Visualisering og logging i Node-RED
- Analyse og styring med Python

