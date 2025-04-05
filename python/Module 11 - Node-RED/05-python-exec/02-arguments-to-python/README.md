# 📤 Workshop 2 – Sende argumenter til Python

## 🎯 Formål
Formålet med denne workshop er at give dig en grundlæggende og solid forståelse for, hvordan du kan sende inputdata fra Node-RED til et Python-script via kommandolinjeargumenter. I stedet for blot at afvikle et script med fast output, som i Workshop 1, lærer du nu at sende værdier aktivt fra dit flow til Python. Python-scriptet modtager argumentet som en værdi, bearbejder det og sender det tilbage som output.

Dette giver dig mulighed for at integrere brugerinput, målinger, grænseværdier eller andre variabler i Python-scripts i realtid. Det er fundamentet for mere komplekse applikationer som beregninger, logikstyring og integration med eksterne enheder og systemer.

---

## 🧰 Forudsætninger
Før du går i gang, skal du have:

- ✅ Gennemført **Workshop 1**, så du ved hvordan `exec`-noden fungerer
- ✅ Python 3 installeret og tilgængelig fra terminal/kommandoprompt
- ✅ Node-RED oppe at køre på din lokale maskine
- ✅ Grundlæggende forståelse af `msg.payload` i Node-RED (den del af beskeden, hvor data lagres)
- ✅ Et simpelt Python-script liggende i en scripts-mappe

---

## 📝 Trin-for-trin guide

### 1. Opret Python-scriptet `echo.py`
Dette Python-script skal modtage et argument fra kommandolinjen og returnere det som output:

```python
import sys
if len(sys.argv) > 1:
    print("Modtaget fra Node-RED:", sys.argv[1])
else:
    print("Ingen argumenter modtaget")
```

- Gem filen som `echo.py` i din `scripts/` mappe
- Sørg for at placeringen af `echo.py` matcher din platform (Linux/macOS vs Windows)

---

### 2. Byg flowet i Node-RED

#### 💻 Linux/macOS

1. **`inject`-node**
   - Payload-type: string
   - Indtast en vilkårlig værdi (f.eks. `42` eller `TemperaturTest`)

2. **`function`-node** (opret forbindelse fra `inject`)
```javascript
msg.payload = `python3 /fuld/sti/til/scripts/echo.py ${msg.payload}`;
return msg;
```
   - Eksempel på sti: `python3 /home/pi/workshops/scripts/echo.py`

3. **`exec`-node**
   - Brug `msg.payload` som kommando
   - Output mode: `return code + stdout`
   - Fjern hak i "append input to command"

4. **`debug`-node**
   - Forbind den til første output af `exec`-noden (stdout)

#### 🪟 Windows

1. **`inject`-node**
   - Payload-type: string (f.eks. `NodeRED123`)

2. **`function`-node**
```javascript
msg.payload = `python C:\sti\til\scripts\echo.py ${msg.payload}`;
return msg;
```
   - Eksempel: `python C:\Users\Bruger\Documents\Modul_05\scripts\echo.py`

3. **`exec`-node**
   - Brug `msg.payload` som kommando
   - Output: `return code + stdout`

4. **`debug`-node** til stdout (første output)

---

### 3. Deploy og test flowet

- Tryk på knappen i `inject`-noden for at aktivere flowet
- Se resultatet i højre side under `debug`
- Outputtet burde ligne:
```
Modtaget fra Node-RED: 42
```

---

## 🔄 Ekstra: Dynamisk input fra brugergrænseflade
Du kan også bruge et **dashboard UI-element** som fx `ui_text_input`:

- Tilføj `ui_text_input` med label: "Indtast værdi til Python"
- Forbind den til `function`-noden ovenfor
- Brugeren indtaster en værdi → denne sendes videre som argument til Python

> Dette gør din løsning interaktiv og operatørstyret

---

## 🛠️ Fejlsøgning og tips

- Sørg for, at `msg.payload` i `function`-noden bliver til en **gyldig kommando**
- Hvis der ikke sker noget:
  - Tjek om stien til scriptet er korrekt (absolut sti)
  - Brug `debug`-node før `exec` til at kontrollere indholdet af `msg.payload`
  - Tilføj `debug`-node til `exec`'s **andet output** (stderr) for at fange fejl

- Kør scriptet manuelt i terminal for at teste:
```bash
python3 /sti/til/scripts/echo.py testværdi
```

---

## ✅ Læringsudbytte
Når du har gennemført denne workshop, vil du have lært at:

- Forstå hvordan argumenter overføres til Python via kommandolinjen
- Oprette Python-scripts der bruger `sys.argv[]` til at læse input
- Dynamisk generere og afvikle kommandoer i Node-RED
- Bruge både manuelle og UI-baserede inputs til at styre Python-kørsel

Dette er et centralt skridt i at gøre dine Python-programmer mere fleksible og responsive overfor brugersignaler, realtidsdata og flowlogik.

---

🔁 Klar til næste skridt? Fortsæt med [Workshop 3 – sende input via stdin](../03-stdin-to-python/README.md), hvor du lærer at sende tekst direkte ind i Python via standard input (stdin) – et alternativ til kommandolinjeargumenter.

