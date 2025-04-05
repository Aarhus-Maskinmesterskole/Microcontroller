# ➕ Workshop 4 – Beregninger med input i Python

## 🎯 Formål
Formålet med denne workshop er at give dig en dybere forståelse for, hvordan du kan bruge Python til at udføre simple og udvidelige beregninger baseret på input leveret fra Node-RED. I de tidligere workshops har du lært at sende en enkelt værdi som argument til Python eller via stdin. Nu udvider vi det til at omfatte **flere inputparametre** og kobler dem til matematiske funktioner i Python.

I denne workshop sender vi to tal fra Node-RED som argumenter til et Python-script, der beregner summen og returnerer resultatet. Du lærer, hvordan Python kan bruges til at udføre bagvedliggende logik og matematik, mens Node-RED fungerer som brugergrænseflade og datarouter.

Metoden du lærer her, kan udvides til mange formål, fx: temperaturudregninger, procentsatser, afstandsberegninger, spændingsmålinger, valutakonvertering, datasummering og meget mere.

---

## 🧰 Forudsætninger
Før du går i gang, bør du have:
- ✅ Gennemført **Workshop 1** og **Workshop 2**, så du er bekendt med `exec`-noden og brug af argumenter
- ✅ En fungerende installation af **Node-RED** og **Python 3.x**
- ✅ Grundlæggende forståelse for noderne `inject`, `function`, `exec` og `debug`
- ✅ En mappe, fx `scripts/`, hvor du opbevarer dine Python-filer

---

## 📝 Trin-for-trin guide

### 1. Opret Python-scriptet `adder.py`
Opret filen `adder.py` med følgende kode:
```python
import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = x + y
    print("Summen er:", result)
except IndexError:
    print("Fejl: Mangler inputværdier")
except ValueError:
    print("Fejl: Input skal være heltal")
```
Dette script forsøger at konvertere to argumenter til heltal, lægge dem sammen og returnere resultatet. Det håndterer også simple fejl som manglende input eller forkert datatype.

Gem det i `scripts/`-mappen på din maskine.

---

### 2. Opsæt flowet i Node-RED
Vi laver nu et flow der sender to værdier til Python og modtager et resultat:

1. **`inject`-node**
   - Payload-type: array
   - Indtast fx `[7, 15]`
   - Navngiv den evt. "Send 2 tal"

2. **`function`-node** (forbind `inject` → `function`):
```javascript
let x = msg.payload[0];
let y = msg.payload[1];
msg.payload = `python3 /fuld/sti/til/scripts/adder.py ${x} ${y}`;
return msg;
```
> Husk at bruge den **fulde sti** til scriptet. På Windows bruges `python` og dobbelte backslashes `\\` i stien.

3. **`exec`-node**:
   - Brug `msg.payload` som kommando
   - Output mode: `return code + stdout`
   - Sæt evt. timeout til 10 sekunder

4. **`debug`-node**:
   - Forbind til første output på `exec`-noden (stdout)
   - Navngiv den "Resultat fra Python"

---

### 3. Deploy og test
Tryk på `Deploy`, og klik derefter på `inject`-noden for at sende værdierne til Python. Du bør se i debug-panelet:
```
Summen er: 22
```

Hvis input mangler eller ikke er numeriske, vil du se en fejlbesked som:
```
Fejl: Input skal være heltal
```

---

## 🧪 Udvidelser og variationer
- 🔢 Brug `float()` i stedet for `int()` for at tillade decimaltal
- ➕ Udvid scriptet til også at kunne udføre multiplikation, subtraktion eller division
- 🧮 Udskift `inject`-node med `ui_numeric` fra Node-RED Dashboard for interaktiv brugerinput
- 🛡️ Tilføj mere fejlhåndtering: fx "division by zero"
- 📈 Brug `function`-node til at hente værdier fra forskellige steder i dit flow og samle dem

---

## ✅ Læringsudbytte
Efter denne workshop kan du:
- Sende **flere parametre** fra Node-RED til et Python-script via kommandolinjen
- Modtage og bruge argumenter i Python med `sys.argv[]`
- Udføre matematiske beregninger i Python og returnere resultatet til Node-RED
- Forbinde Node-RED frontend med Python backend i strukturerede flows
- Udvide dine scripts med fejlkontrol, floating point og brugervenlighed

---

🔁 Næste skridt? Fortsæt med [Workshop 5 – Snap7 læsning](../05-snap7-basic-read/README.md), hvor du lærer at bruge Python til at læse data fra en Siemens PLC og sende dem til Node-RED.

