# 📄 Modul 6 – Real-time visualisering og datalogning med Node-RED

## 🎯 Formål

Dette modul har til formål at introducere dig som universitetsstuderende til den tekniske og metodiske opsætning af realtidsvisualisering og vedvarende datalogning i Node-RED. Du skal arbejde med at kombinere visualiseringskomponenter og persistente lagringsmekanismer, så data fra ESP32 både kan observeres i realtid og gemmes til videre analyser. Det primære udgangspunkt er et eksisterende serielt dataflow opbygget i Modul 5, hvor ESP32 sender målinger i CSV-format over USB. 

Modulet fokuserer på, hvordan dette datasæt struktureres i Node-RED, og hvordan du kan bearbejde det til anvendelig visualisering og logging – vigtige komponenter i moderne industrielle IoT-løsninger og SCADA-systemer. Desuden introduceres du til god praksis for dataintegration, filformatvalg og præsentationsstrategier.

---

## 🧰 Forudsætninger og nødvendige komponenter

For at kunne gennemføre dette modul på hensigtsmæssig vis, skal du sikre følgende:

- Node-RED er korrekt installeret og kørende lokalt på IPC eller kompatibel arbejdsstation.
- Du har et fungerende flow fra Modul 5, hvor ESP32 kontinuerligt sender sensorværdier (temperatur, fugtighed, gas og lysniveau) i CSV-format.
- Node-RED-paletten inkluderer `node-red-dashboard` til brugergrænseflade.
- Du har adgang til `file`-node for filbaseret datalagring.
- Du har basal forståelse af JavaScript og JSON-strukturer til flowlogik og datamanipulation.

---

## 🎛️ Trin 1: Implementering af realtidsvisualisering

Visualiseringen opbygges vha. komponenter i `dashboard`-paletten, som tillader dynamisk præsentation af måleværdier direkte i webgrænsefladen.

1. Tilføj følgende elementer til dit flow:
   - `gauge`-komponenter for visning af temperatur- og fugtværdier.
   - `chart`-komponenter til løbende visning af gas og lys som tidsserier.

2. Konfiguration af komponenterne:
   - **Group**: Opret eller tilknyt til eksisterende visningsgruppe i dashboard.
   - **Label**: Brug tydelige og konsistente etiketter (f.eks. "Temperatur [°C]", "Gasniveau").
   - **Format**: `{{value}}` giver ren visning; overvej også at inkludere enhed-
   - **Min/Max**: Brug passende skala – fx 0–100 for temperatur, 0–1023 for analoge sensorer.

3. Strukturér dit flow på følgende måde:
```text
[serial in] → [CSV to JSON function] → [gauge/chart/debug]
```

4. Gå til dashboardvisning: `http://localhost:1880/ui`. Du bør se levende målinger ændre sig i takt med sensorinput.

> Dashboardet fungerer som en lokal HMI og giver mulighed for at simulere industriel visualisering af procesdata.

---

## 🗃️ Trin 2: Konfiguration af datalogning i CSV-format

Datalogning er essentiel for at kunne dokumentere systemadfærd, analysere trends og efterbehandle datasæt i fx Python eller Excel.

1. Tilføj en `file`-node og tilknyt den til flowet. Konfiguration:
   - **Filename**: Navngiv f.eks. `sensor_log.csv`.
   - **Action**: Append to file.
   - **Encoding**: UTF-8.
   - **Add newline**: ✅ aktiveres for at sikre korrekt formatering.

2. Tilføj en `function`-node forud for `file`-noden, der konverterer JSON til en korrekt struktureret CSV-række:
```javascript
let d = new Date();
let t = d.toISOString();
let row = `${t},${msg.payload.temperature},${msg.payload.humidity},${msg.payload.gas},${msg.payload.light}`;
msg.payload = row;
return msg;
```

3. Eksempel på logoutput:
```
2025-04-05T12:00:01.123Z,22.5,43.2,601,812
```

Du har nu skabt en logstruktur, der kan anvendes i regressionsanalyse, maskinlæring og sammenlignende studier.

---

## 📝 Øvelser og afprøvning

1. Opret visualisering af alle fire sensortyper (temperatur, fugt, gas, lys) via dashboard.
2. Konfigurer CSV-logging med timestamps og valider i debug og fysisk fil.
3. Udvid dit flow med logik, der reagerer på grænseværdier (f.eks. alarm hvis gas > 800).
4. Test robusthed: Hvad sker der hvis der mangler en værdi i datastrengen?
5. Dokumentér flowet med kommentarer og brug evt. `comment`-noder til læsbarhed.
6. Åbn `sensor_log.csv` i regneark og visualisér data herfra som kontrol.
7. Skriv et kort afsnit i din rapport, hvor du beskriver potentialet for integration med en cloud- eller databaseløsning.

---

## ✅ Læringsudbytte

Ved afslutningen af dette modul forventes det, at du er i stand til at:

- Opbygge og konfigurere realtidsdashboard i Node-RED til sensordata.
- Omdanne struktureret data til CSV-format med tidsstempling.
- Implementere betinget logik i flows (alarm, filtrering, dynamisk routing).
- Integrere persistente lagringsmetoder i flows.
- Vurdere og dokumentere datakvalitet og systemintegration.

Disse færdigheder er centrale i mange industrielle og akademiske projekter med fokus på datadrevet automatisering.

---

## 💡 Faglige noter og anbefalinger

- Inkludér `ui_alert`, `ui_text`, og `notification`-komponenter for forbedret brugerfeedback.
- Brug `file in`-node til at indlæse og vise loggedata retrospektivt.
- Sørg for versionskontrol af flows via Git – især hvis du arbejder i teams.
- Inkludér dine logningsmekanismer i din FAT-/SAT-teststrategi, så dokumentationen kan anvendes til validering.
- Overvej at udvide logging til databasesystem (MongoDB, InfluxDB) i projektforløbets senere faser.

Med dette modul har du opnået erfaring med både frontend-visualisering og backend-logning af tekniske målinger – en kompetence, der er yderst relevant i den moderne industrielle og akademiske kontekst.

