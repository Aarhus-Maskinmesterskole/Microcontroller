# 📄 Modul 7 – PLC-kommunikation via Snap7

## 🎯 Formål

Dette modul introducerer dig til kommunikation mellem Node-RED og en Siemens PLC (S7-1200 eller S7-1500) ved brug af Snap7-biblioteket i Python. Du lærer at læse og skrive data til en datablock (DB) i PLC’en, hvilket skaber en bro mellem softwarens brugerflade (Node-RED) og hardwarestyringen (PLC).

Målet er at gøre dig i stand til at:
- Konfigurere en Siemens PLC med en DB til dataudveksling.
- Forbinde til PLC’en via Snap7 i Python.
- Integrere Python-scripts i Node-RED via exec- eller websocket-noder.
- Validere kommunikationen gennem realtidsvisualisering og respons.

---

## 🧰 Krav og forudsætninger

- Siemens PLC (fysisk eller via PLCSIM Advanced).
- Opsat datablock med de ønskede variabler.
- Kendskab til IP-konfiguration af PLC.
- Python 3.x installeret med Snap7:
```bash
pip install python-snap7
```
- Kendskab til adressestruktur i Siemens TIA Portal

---

## ⚙️ Eksempel på Python-kode med Snap7

```python
import snap7
from snap7.util import *
from snap7.snap7types import *

client = snap7.client.Client()
client.connect("192.168.0.10", 0, 1)  # IP, rack, slot

data = client.db_read(1, 0, 4)  # Læs 4 byte fra DB1
value = get_real(data, 0)
print("Temperatur i PLC:", value)

client.disconnect()
```

> Udskift `192.168.0.10` med IP-adressen på din PLC. Husk at DB1 skal være "non-optimized" for Snap7-adgang.

---

## 🧪 Trin-for-trin

1. Opret datablock i TIA Portal (non-optimized).
2. Indsæt en Real-variabel (fx `temperatur`) i DB1.
3. Tilføj netværkskonfiguration og IP-adresse.
4. Upload DB til PLC og test at den er tilgængelig.
5. Brug testscript i Python til at læse værdien.
6. Udvid script til også at kunne skrive data:
```python
from snap7.util import set_real
buffer = bytearray(4)
set_real(buffer, 0, 37.5)
client.db_write(1, 0, buffer)
```

---

## 📝 Opgaver

1. Installer Snap7 og test forbindelsen til din PLC.
2. Læs værdien af mindst én variabel i en datablock.
3. Vis den i Node-RED via `exec`- eller websocket node.
4. Skriv en værdi tilbage til PLC og bekræft ændring i TIA Portal.
5. Undersøg hvordan datatyper som Bool, Int og Real håndteres forskelligt i Snap7.
6. Dokumentér hele kommunikationsforløbet og eventuelle fejl.

---

## ✅ Læringsudbytte

- Du har opnået praktisk erfaring med Snap7 og Siemens PLC.
- Du kan udveksle data mellem Python og PLC.
- Du har etableret grundlaget for mere kompleks automatisering og procesovervågning.

---

## 💡 Tips

- Snap7 fungerer kun med "non-optimized" datablocks.
- Sørg for at PLC’en ikke er i "stop mode".
- Brug `try/except` i din Python-kode til robust fejlhåndtering.
- Du kan udvide med MQTT eller REST API senere hvis ønsket.

Dette modul sætter dig i stand til at bygge bro mellem embedded software og industriel PLC-teknologi – en afgørende kompetence i moderne automatisering.