# 🧹 Modul 05 – Python-integration via exec-noden

---

## 🌟 Workshop 5 – JSON-integration og CSV-logning

---

### 🌟 Formål

Formålet med denne workshop er at lære, hvordan du kan sende strukturerede JSON-data fra Node-RED til Python, og hvordan Python kan bruge pandas-biblioteket til at gemme data i dato-baserede CSV-filer.  
Du lærer både at sende data via **argumenter** og **stdin**, og du får indsigt i, hvordan man håndterer data robust, så der kun oprettes nye filer når nødvendigt, og hvordan data appender korrekt til eksisterende filer.

Denne teknik er grundstenen i datalogning og bruges i mange virkelige systemer som f.eks. IoT-enheder, målerdata, batch-logs og produktionsdata.

---

### 🧰 Forudsætninger

- Gennemført Workshops 1–4
- Node-RED og Python 3.x installeret
- Pandas installeret: `pip install pandas`
- Scripts-mappe oprettet
- Grundlæggende kendskab til JSON, exec-, function- og debug-noder i Node-RED

---

### 📝 Trin-for-trin guide


#### Node-RED setup oversigt
![Screenshot From 2025-04-27 13-46-57](https://github.com/user-attachments/assets/2504fe9c-ab05-480c-aa54-7e86cb6946a8)



#### 1. Opret Python-scriptet `log_to_csv.py` (via argument)

```python
#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime
import pandas as pd

json_input = sys.argv[1]
data_dict = json.loads(json_input)

df = pd.DataFrame([data_dict])
filnavn = f"{datetime.now():%Y-%m-%d}.csv"
skriv_header = not os.path.isfile(filnavn)

df.to_csv(filnavn, mode="a", index=False, header=skriv_header)
print(f"Data skrevet til {filnavn}")
```

Gem i **scripts/**-mappen.

---

#### 2. Byg flowet i Node-RED (via argument)

- **Inject-node**: JSON-payload (fx `{ "temp": 23.4, "humid": 45.2, "gass": 123 }`)
![Screenshot From 2025-04-27 18-34-07](https://github.com/user-attachments/assets/b1a46f83-5fd2-472e-88e5-df8848c3e42b)

- **Function-node**:
```javascript
let now = new Date();
let ts = now.toISOString().replace('T',' ').split('.')[0];

let obj = {
    timestamp: ts,
    temperature: msg.payload.temp,
    humidity: msg.payload.humid,
    gass: msg.payload.gass
};

msg.payload = `python3 /scripts/log_to_csv.py '${JSON.stringify(obj)}'`;
return msg;
```

![Screenshot From 2025-04-27 13-47-16](https://github.com/user-attachments/assets/60b2536c-1061-41d7-b269-00b08893e3bf)

- **Exec-node**:
  - Command: `msg.payload`
  - Slå "Append msg.payload to command" FRA

![Screenshot From 2025-04-27 13-47-25](https://github.com/user-attachments/assets/7039dfbc-afbb-4026-921f-2f978c071537)

- **Debug-node**: Forbind stdout

![Screenshot From 2025-04-27 13-47-34](https://github.com/user-attachments/assets/aa481524-0d30-465a-b68e-db5e7adcb49b)

---

#### 3. Alternativ: Python via stdin

**Python-script `log_to_csv_stdin.py`:**

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

Node-RED flow ændres:
- **Function-node**: Samme JSON-struktur men åbn payload direkte som JSON-string.
- **Exec-node**: Kommando `python3 /scripts/log_to_csv_stdin.py`, og hak i "Append payload to stdin".

---

### 🛠️ Fejlsøgning og tips

- Brug **absolutte stier** til Python-scripts.
- Debug JSON-string før exec-node.
- Kontrollér at `pandas` er installeret korrekt.
- Husk korrekt formattering af JSON (`{"key": value}`).

---

### ✅ Læringsudbytte

Når du har gennemført denne workshop, kan du:

- Sende struktureret JSON-data fra Node-RED til Python
- Parse JSON-data i Python
- Oprette daglige CSV-filer med pandas
- Anvende enten `argv` eller `stdin` til datakommunikation
- Opbygge robuste flows til datalogning

---

🔄 Klar til næste niveau? Fortsæt med **Workshop 6 – Snap7-læsning fra Siemens PLC**!

