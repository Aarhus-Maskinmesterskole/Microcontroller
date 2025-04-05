# 📄 Modul 04 – Lokal datalogning og CSV-eksport i Node-RED

## 🎯 Formål
I dette modul udvider vi dine færdigheder i Node-RED med et centralt aspekt af ethvert automatiseret system: datalogning. Ved hjælp af `file`-noden skal du implementere funktionalitet, der opsamler og gemmer målinger i et struktureret CSV-format. Dette modul introducerer vigtige principper omkring datasporbarhed, systematisk logning og eksport i formater, der kan bruges til både teknisk dokumentation, fejlsøgning og efterfølgende analyse i eksterne værktøjer som Excel eller Python. Du lærer også hvordan du med fordel kan inkludere timestamps, metadata og anvende en daglig rotering af logfiler.

---

## 🧰 Forudsætninger
Før du går i gang med dette modul, forudsættes det, at:
- Du har gennemført **Modul 02**, hvor du lærte at hente data via seriel kommunikation
- Du har gennemført **Modul 03**, hvor du har visualiseret realtidsdata med dashboard
- Du har kendskab til brugen af `function`- og `change`-noder
- Du har skriveadgang til et lokalt bibliotek på din IPC, f.eks. en specifik mappe til logfiler
- Du har testet, at data modtages kontinuerligt fra din mikrokontroller eller sensor

---

## 📦 CSV – Comma Separated Values
Et CSV-dokument er en simpel men kraftfuld måde at organisere data på. Det er en tekstbaseret fil, hvor hver linje repræsenterer en observation (en datapunkt), og værdierne adskilles af kommaer eller semikolon. I tekniske og industrielle miljøer er CSV en udbredt standard, der kan anvendes til:

- Import til Excel, Python (pandas), MATLAB eller SCADA-rapporter
- Udveksling af måledata mellem systemer
- Dokumentation og verificering af testresultater

### Eksempel på klassisk CSV-indhold:
```csv
timestamp,value
2024-04-06 10:00:01,1321
2024-04-06 10:00:02,1328
```

Du kan med fordel oprette CSV-filer der inkluderer flere sensorer, brugernavne, lokationsdata eller systemstatus.

---

## 📋 Trin-for-trin – Simpel logger

1. Tilføj en `function`-node før din `file`-node:
```javascript
msg.payload = new Date().toISOString() + "," + msg.payload + "\n";
return msg;
```
   - Her formatteres outputtet som én linje pr. måling med timestamp og sensorværdi

2. Tilføj en `file`-node
   - **Mode:** `append to file`
   - **Filnavn:** fx `/home/pi/log/sensorlog.csv` (Linux) eller `C:\logs\sensorlog.csv` (Windows)
   - **Encoding:** `utf8` anbefales for bred kompatibilitet

3. **Deploy** dit flow og se filen blive opdateret i takt med at data modtages

> 📝 Tip: Opret en separat mappe til logs, fx `~/node-red-logs/` og giv den fuld skriveadgang

---

## 🛠️ Udvidet CSV – Flersporet logning
Hvis du ønsker at logge flere parametre, fx fra flere sensorer eller med tilknyttede metadata:
```javascript
let t = new Date().toISOString();
let val = parseInt(msg.payload);
msg.payload = `${t},sensor1,${val}\n`;
return msg;
```
Du kan nemt udvide dette til:
```javascript
msg.payload = `${t},sensor1,ESP32-Lab1,${val},OK\n`;
```

---

## 🧪 Test og validering
Når loggeren er sat op, er det vigtigt at teste dens stabilitet og nøjagtighed:
- **Åbn CSV-filen** i en teksteditor eller i Excel/LibreOffice for visuel kontrol
- **Kontrollér formatering**: Har hver linje korrekt timestamp og separator?
- **Tjek datarækker**: Matcher de med debug-uddata i Node-RED?
- Brug kommandoen `tail -f <filnavn>` på Linux/macOS for at se live data
- Hvis du arbejder i et undervisningsmiljø: Sørg for at testflowet logger til en unik filnavn per gruppe eller dag

---

## 📁 Struktur og backupstrategi
Når loggeren kører kontinuerligt, bør du implementere:
- **Én logfil pr. dag** med dynamisk filnavn, fx: `/logs/${current_date}.csv`
- Automatisk **rotering** ved hjælp af `function`-node der tjekker datoen
- **Backup** af filer til eksternt drev eller versioneret mappe
- Advarselssystem i tilfælde af manglende skriveadgang eller diskplads

---

## 📝 Øvelser
1. Lav en logger der gemmer serielle data med ISO-formateret timestamp
2. Udvid til at inkludere sensornavn og systemstatus
3. Log kun værdier hvor `msg.payload > 1000` med en `switch`-node før `function`
4. Test flowet ved at stoppe/start Node-RED og observere om loggen fortsætter korrekt
5. Tilføj fejlhåndtering – fx en `catch`-node der aktiveres hvis filskrivning fejler
6. Eksportér logfilen og åbn den i Excel – lav en graf over udviklingen

---

## ✅ Læringsudbytte
Efter gennemførelsen af dette modul vil du:
- Have implementeret en robust CSV-logger i Node-RED
- Kunne tilføje tidsstempel, sensor-ID og værdier i korrekt struktureret tekstformat
- Forstå hvordan man validerer og åbner logdata i eksterne systemer
- Være i stand til at oprette flows, der både logger og visualiserer data samtidigt
- Forstå praktiske overvejelser omkring datasikkerhed, backup og fejlhåndtering

---

I næste modul bygger vi videre på dette, når vi lærer at bruge `exec`-noden i Node-RED til at afvikle Python-scripts. Du vil lære at oprette flows, der interagerer direkte med eksterne scripts, fx til databehandling, Snap7-kommunikation eller aktivering af testværktøjer.

