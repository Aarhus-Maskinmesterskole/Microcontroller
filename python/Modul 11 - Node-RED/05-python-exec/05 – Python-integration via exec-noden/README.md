# 🧹 Modul 05 – Python-integration via exec-noden

---

## 🌟 Workshop 5 – JSON-integration og CSV-logning

---

### 🌟 Formål

Formålet med denne workshop er at lære, hvordan du kan sende strukturerede JSON-data fra Node-RED til Python, og hvordan Python kan bruge pandas-biblioteket til at gemme data i dato-baserede CSV-filer.

Denne teknik bruges i mange virkelige systemer som f.eks. IoT-enheder, målerdata, batch-logs og produktionsdata.

---

### 🧰 Forudsætninger

- Gennemført Workshops 1–4
- Node-RED og Python 3.x installeret
- Pandas installeret: `pip install pandas`
- Scripts-mappe oprettet
- Grundlæggende kendskab til JSON, exec-, function- og debug-noder i Node-RED

---

### 📝 Trin-for-trin guide

#### 1. Opret Python-scriptet `log_to_csv.py`

Gem følgende script i din **scripts/**-mappe:

```python
#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime
import pandas as pd


try:
    json_input = sys.argv[1]
except IndexError:
    sys.exit("Fejl: Der blev ikke givet noget JSON-argument")

data_dict = json.loads(json_input)


df = pd.DataFrame([data_dict])              


dagens_dato   = datetime.now().strftime("%Y-%m-%d") 
filnavn = f"{dagens_dato}.csv"


skriv_header = not os.path.isfile(filnavn)

df.to_csv(filnavn,
          mode="a",
          index=False,
          header=skriv_header)

print(f"Data skrevet til {filnavn}")
```

---

#### 2. Byg flowet i Node-RED

##### a) Tilføj en Inject-node
- Sæt Payload-type til **JSON**.
- Indtast følgende JSON-data:

```json
{
  "temp": 23.4,
  "humid": 45.2,
  "gass": 123
}
```

Denne JSON bruges som input til Function-noden.

![Screenshot From 2025-04-27 18-34-07](https://github.com/user-attachments/assets/69e38646-2192-47e5-8329-7b53e2c2dc26)

##### b) Tilføj en Function-node
- Tilføj følgende kode i Function-noden:

Hvis du køre Linux:
```javascript
let now = new Date();
let ts = now.toISOString().replace('T',' ').split('.')[0];

// Her oprettes et JSON objekt med fire entries: timestamp, temperature, humidity, gass
let obj = {
    timestamp: ts,
    temperature: msg.payload.temp,
    humidity: msg.payload.humid,
    gass: msg.payload.gass
};

let payload = JSON.stringify(obj);

// Byg hele kommandoen korrekt
msg.payload = `python3 /scripts/log_to_csv.py '${payload}'`;
return msg;
```

Hvis du køre Windows:
```javascript
let now = new Date();
let ts = now.toISOString().replace('T',' ').split('.')[0];

// Lav JSON-objektet
let obj = {
    timestamp: ts,
    temperature: msg.payload.temp,
    humidity: msg.payload.humid,
    gass: msg.payload.gass
};

// Konverter objektet til en JSON-string
let payload = JSON.stringify(obj);

// Escape double quotes i payload (MEGET VIGTIGT til cmd / exec)
payload = payload.replace(/"/g, '\\"');

// Byg kommandoen
msg.payload = `python3 /scripts/log_to_csv.py "${payload}"`;

return msg;
```



**Forklaring step-for-step:**
- `now` opretter et timestamp.
- `toISOString().replace('T',' ').split('.')[0]` formaterer timestampet til "ÅÅÅÅ-MM-DD HH:MM:SS".
- Der oprettes et JSON-objekt med fire entries ud fra de modtagne værdier.
- Kommandoen til at køre Python-scriptet bygges.
- Kommandoen sendes videre i flowet.

![Screenshot From 2025-04-27 13-47-16](https://github.com/user-attachments/assets/e4612653-3792-4fc9-9848-cd31ba8ab5a9)

##### c) Tilføj en Exec-node
- Sæt Command til: `msg.payload`
- Slå **"Append msg.payload to command" fra**.
- Output mode: "when the command is complete - exec mode"
  
![Screenshot From 2025-04-27 13-47-25](https://github.com/user-attachments/assets/5fdd3bd5-a0a7-403e-9fdb-903b6dd7b8d8)

##### d) Tilføj tre Debug-noder
- Forbind stdout (1. output), stderr (2. output) og return code (3. output) til separate debug-noder.
- Ændr evt. navnene til `stdout`, `stderr`, og `returncode` for at holde overblik.

![Screenshot From 2025-04-27 13-47-25](https://github.com/user-attachments/assets/ab6e0630-8ffb-4674-bd32-2a3ab6768160)

##### e) Flow oversigt

![Screenshot From 2025-04-27 13-46-57](https://github.com/user-attachments/assets/bbf2b1bf-bc21-4877-bb42-857200e5b251)

---

#### 3. (Ekstra) Alternativ opsætning: Python via stdin

Hvis du i stedet vil sende JSON via stdin, skal du bruge dette Python-script:

```python
#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime
import pandas as pd

json_input = sys.stdin.read()
data_dict = json.loads(json_input)

df = pd.DataFrame([data_dict])
filnavn = f"{datetime.now():%Y-%m-%d}.csv"
skriv_header = not os.path.isfile(filnavn)

df.to_csv(filnavn, mode="a", index=False, header=skriv_header)
print(f"Data skrevet til {filnavn}")
```

Node-RED flowet tilpasses ved at fjerne kommandoen fra Function-noden og i stedet lade Exec-noden modtage data via stdin.

---

### 🛠️ Fejlsøgning og tips

- Brug **absolutte stier** til Python-scripts.
- Kontrollér at `pandas` er installeret korrekt.
- Kontrollér i stderr-debug hvis der sker fejl i exec.
- Tjek JSON-format hvis Python fejler med JSONDecodeError.

---

### ✅ Læringsudbytte

Efter denne workshop kan du:

- Sende struktureret JSON-data fra Node-RED til Python
- Parse JSON-data i Python
- Oprette daglige CSV-filer dynamisk
- Anvende `argv` eller `stdin` til datakommunikation
- Debugge flows ved hjælp af flere outputs i exec-noden

---

🔄 Klar til næste niveau? Fortsæt med **Workshop 6 – Snap7-læsning fra Siemens PLC**!
