# 🔧 Workshop 1 – Simpelt Python-output

## 🎯 Formål
Formålet med denne første workshop er at give dig en tryg og grundig introduktion til, hvordan du etablerer den mest basale form for integration mellem Node-RED og Python. Du vil lære, hvordan du ved hjælp af `exec`-noden i Node-RED kan afvikle et eksternt Python-script og hente dets tekstbaserede output direkte ind i dit flow. Dette danner grundlaget for al videre kommunikation mellem Node-RED og Python, herunder udveksling af målinger, styringssignaler, databehandling og meget mere.

Denne workshop er vigtig, fordi den introducerer begrebet **`stdout`** – altså standard output – som den primære kanal, hvorigennem Python kan sende data tilbage til Node-RED. Du vil desuden lære at arbejde platformsspecifikt, både i Linux/macOS- og Windows-miljøer.

---

## 🧰 Forudsætninger
Før du går i gang, skal du sikre dig følgende:

- ✅ Du har installeret Python 3.x:
  - På Linux/macOS: kør `python3 --version`
  - På Windows: kør `python --version` i kommandoprompten
- ✅ Du har installeret og kan tilgå Node-RED lokalt via `http://localhost:1880`
- ✅ Du er bekendt med følgende Node-RED noder:
  - `inject` (bruges til at trigge flows)
  - `exec` (bruges til at køre kommandoer på systemniveau)
  - `debug` (bruges til at vise output i højre side af editoren)

Du behøver ikke at kunne skrive Python i forvejen – denne workshop er netop skabt til begyndere.

---

## 📝 Trin-for-trin guide

### 1. Opret Python-scriptet `hello.py`

Først skal du oprette en lille Python-fil, som bare skriver en tekst til skærmen:

```python
print("Hej fra Python!")
```

Gem filen som `hello.py` i den medfølgende `scripts/` mappe, som du finder i din workshop-mappe.


### 2. Byg dit første Node-RED flow

#### 💻 Linux/macOS

1. Træk en `inject`-node ind på flowet
   - Konfigurer den til at sende et simpelt signal (fx "timestamp")

2. Træk en `exec`-node ind
   - Indstil feltet **Command** til:
     ```bash
     python3 /fuld/sti/til/scripts/hello.py
     ```
   - Eksempel: `python3 /home/pi/python_exec/scripts/hello.py`
   - Sørg for at du bruger den **fulde sti** – relative stier virker ikke altid

3. Træk en `debug`-node ind og forbind den til **første output** på `exec`-noden (stdout)

4. Klik på **Deploy**, og tryk derefter på knappen på `inject`-noden.

> I debug-panelet i højre side bør du nu se: `Hej fra Python!`

#### 🪟 Windows

1. Træk en `inject`-node ind som beskrevet ovenfor

2. Tilføj en `exec`-node og indtast følgende kommando:
   ```cmd
   python C:\sti\til\scripts\hello.py
   ```
   - Eksempel: `python C:\Users\Bruger\Documents\Modul_05\scripts\hello.py`
   - Husk at dobbelte backslashes (`\`) i stien er nødvendigt i Windows

3. Forbind `exec`-nodens første output til en `debug`-node, og deploy flowet

> Output i debug-panelet skal vise: `Hej fra Python!`

---

## 🛠️ Fejlsøgning og tips

Hvis noget går galt, kan du bruge nedenstående tjekliste:

- ❌ Intet output?
  - Tjek at filen `hello.py` eksisterer på den angivne sti
  - Kontrollér, at Node-RED har adgang til mappen

- ⚠️ Fejl i stderr?
  - Tilføj en `debug`-node til **andet output** på `exec`-noden (stderr)
  - Dette viser Python-fejlmeddelelser (fx syntaksfejl)

- 🧪 Test Python manuelt:
  - Åbn terminal eller kommandoprompt og skriv:
    ```bash
    python3 /sti/til/hello.py  # Linux/macOS
    python C:\sti\til\hello.py  # Windows
    ```

- 🗂️ Brug absolut sti – undgå relative stier som `./scripts/hello.py`

- 💾 Hvis du flytter flowet til en anden maskine, skal du tilpasse stien til Python-scriptet.

---

## ✅ Læringsudbytte
Når du har gennemført denne første workshop, vil du have lært at:

- Skrive og gemme et simpelt Python-script, som genererer `stdout`
- Udføre et Python-script fra Node-RED via `exec`-noden
- Opfange og vise output fra Python direkte i Node-RED via `debug`
- Fejlsøge og diagnosticere de mest almindelige problemer med sti og rettigheder

Dette er et vigtigt fundament for resten af modul 05, hvor vi gradvist udvider kompleksiteten.

---

🔁 Når du er klar, så fortsæt med [Workshop 2 – sende argumenter til Python](../02-arguments-to-python/README.md), hvor du lærer at sende data *ind* i Python-scriptet via argumenter på kommandolinjen.

