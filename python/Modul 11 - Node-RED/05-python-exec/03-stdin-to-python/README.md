# 📥 Workshop 3 – Sende input via stdin til Python

## 🎯 Formål
Denne workshop udvider din forståelse for datakommunikation mellem Node-RED og Python ved at introducere dig til brugen af **standard input (stdin)** som kommunikationskanal. I modsætning til de tidligere workshops, hvor vi sendte argumenter direkte med kommandoen, giver `stdin` en mere fleksibel måde at sende data fra Node-RED til Python på. Det er især nyttigt, når man vil sende større datamængder, som fx tekst, JSON, flere parametre på én gang eller dynamiske strenge fra brugere.

Du lærer at opbygge et Node-RED-flow, der kan sende tekst til Python, og hvordan Python-scriptet modtager dette input via `sys.stdin`. Du kommer også til at se, hvordan denne teknik kan bruges til at sende strukturerede data som JSON, og hvordan Python kan reagere på dette input.

---

## 🧰 Forudsætninger
For at kunne gennemføre denne workshop, forventes det at du:
- ✅ Har gennemført Workshop 1 og Workshop 2
- ✅ Har Node-RED installeret og kørende lokalt på din computer
- ✅ Har Python 3.x installeret og kan tilgå det fra kommandolinjen
- ✅ Har adgang til en `scripts/` mappe, hvor du kan gemme dine Python-filer
- ✅ Forstår grundlæggende brug af `inject`, `exec` og `debug` noder i Node-RED

---

## 📝 Trin-for-trin guide

### 1. Opret Python-scriptet `stdin_read.py`
Lav et nyt Python-script med følgende indhold:

```python
import sys
for line in sys.stdin:
    print("Modtaget via stdin:", line.strip())
```

Dette script vil læse inputlinjer én ad gangen fra `stdin` og derefter skrive dem tilbage som output til `stdout`. Det er denne output, du vil se i Node-RED.

Gem scriptet som `stdin_read.py` i mappen `scripts/` på din computer.

---

### 2. Byg dit flow i Node-RED

#### 💻 For Linux/macOS
1. **Opret en `inject`-node**
   - Sæt payload-type til `string`
   - Indtast en værdi, fx: `Test fra Node-RED`

2. **Opret en `exec`-node**
   - Kommando: `python3 /fuld/sti/til/scripts/stdin_read.py`
   - Marker feltet: `Append msg.payload to stdin`
   - Fjern flueben i "append input to command"

3. **Tilføj en `debug`-node**
   - Forbind den til **første output** af `exec`-noden (stdout)

#### 🪟 For Windows
1. **`inject`-node**
   - Payload-type: string → fx: `Hello Windows!`

2. **`exec`-node**
   - Kommando: `python C:\sti\til\scripts\stdin_read.py`
   - Marker: `Append msg.payload to stdin`

3. **`debug`-node**
   - Forbind til første output af `exec`

---

### 3. Deploy og test flowet
- Tryk på `Deploy`
- Aktiver flowet med `inject`-knappen
- Du bør se output i debug-panelet, fx:
```
Modtaget via stdin: Test fra Node-RED
```

> Du kan nu sende alt fra almindelig tekst til JSON-strenge via denne metode.

---

## 🧪 Eksempel: Sende JSON til Python
For mere avancerede scenarier kan du sende JSON-objekter til Python og bearbejde dem med `json.loads()`:

### Eksempel på payload i `inject`:
```json
{
  "sensor": "temp",
  "value": 23.5
}
```

### Python-script (videreudvikling af `stdin_read.py`):
```python
import sys, json
for line in sys.stdin:
    try:
        data = json.loads(line)
        print(f"Sensor {data['sensor']} har målt {data['value']}°C")
    except Exception as e:
        print("Fejl i parsing:", e)
```

Med denne tilgang kan du bruge Node-RED som frontend og Python som backend til databehandling.

---

## 🛠️ Fejlsøgning og gode råd
- ✅ Sørg for at `Append msg.payload to stdin` er **markeret** i `exec`-noden
- 🔁 Brug en `debug`-node før `exec`-noden for at sikre at payload bliver korrekt sendt
- 📍 Tjek stien til Python-scriptet – brug altid **absolutte stier**
- 🔧 Tilføj en `debug`-node til **stderr-output** (output 2 på `exec`) for at se Python-fejl

> Husk, at hvis du bruger Windows, skal du bruge `python` og `C:\sti\til\...`, mens du på Linux/macOS bruger `python3` og Unix-stier (`/home/...`).

---

## ✅ Læringsudbytte
Når du har gennemført denne workshop, kan du:

- Udvide din Python-kommunikation med `stdin` som fleksibel inputkanal
- Skrive Python-scripts der dynamisk læser tekststrømme fra Node-RED
- Behandle både almindelig tekst og struktureret JSON direkte i Python
- Forstå forskellen på `sys.stdin` og `sys.argv` og hvornår de bruges
- Udvikle flows der kombinerer brugerinput, UI-komponenter og backend scripts

Dette giver dig redskaberne til at udvikle mere avancerede og brugertilpassede løsninger med Python og Node-RED i tæt samarbejde.

---

🔁 Klar til næste skridt? Gå videre til [Workshop 4 – beregninger med input](../04-python-math/README.md), hvor du lærer at sende flere inputværdier og lade Python beregne et resultat.

