# 📄 Modul 01 – Introduktion til Node-RED og flow-struktur

## 🎯 Formål
Dette første modul har til formål at give dig en grundlæggende, men samtidig detaljeret forståelse for, hvordan Node-RED fungerer som visuelt programmeringsmiljø og dataintegrationsværktøj i industrielle og tekniske kontekster. Du vil blive introduceret til det centrale begrebsapparat i Node-RED, herunder noder, flows, `msg.payload`, runtime og deploy-strukturen. Formålet er desuden at skabe et solidt fundament for de kommende moduler, hvor Node-RED anvendes som kommunikations- og visualiseringsplatform mellem fysiske enheder såsom mikrokontrollere og PLC’er.

---

## 🖥️ Installation og opsætning

### 🔧 Krav:
For at kunne arbejde med Node-RED skal følgende være tilgængeligt og korrekt installeret på din lokale maskine (IPC eller almindelig PC):

- **Node.js** (anbefalet LTS-version, fx v18.x eller nyere)
- **NPM** – Node Package Manager (følger typisk med Node.js)
- **Terminal** eller **kommandoprompt** med administratorrettigheder
- **Browser** til lokal adgang til Node-RED editoren

### 🧰 Installationstrin:

1. **Download og installer Node.js**:
   - Gå til [https://nodejs.org](https://nodejs.org) og vælg LTS-versionen
   - Under installationen accepteres standardindstillinger

2. **Verificér installation i terminal**:
```bash
node -v
npm -v
```
   - Disse kommandoer skal returnere versionsnumre

3. **Installer Node-RED globalt**:
```bash
npm install -g --unsafe-perm node-red
```

4. **Start Node-RED**:
```bash
node-red
```
   - Du bør nu se output i terminalen, som slutter med:
     > Server now running at http://127.0.0.1:1880/

5. **Åbn Node-RED editor i din browser**:
```text
http://localhost:1880
```

6. **Installer nødvendige udvidelser (fra ~/.node-red)**:
```bash
cd ~/.node-red
npm install node-red-dashboard
npm install node-red-node-serialport
```
   - Dashboardet bruges til UI-visualisering, og Serial-noden anvendes i næste modul

> 💡 Har du problemer med `serialport`-noden på Windows, skal du evt. installere drivere som **CH340** eller **CP210x**, afhængigt af dit USB-til-seriel interface.

---

## 🧰 Forudsætninger
- Node.js og Node-RED er installeret på dit system
- Du har adgang til en moderne browser (Chrome, Firefox eller Edge)
- Du er klar til at udforske visuel programmering med fokus på databehandling, kommunikation og automation
- Det er en fordel, men ikke et krav, at have grundlæggende forståelse for logiske strukturer og datatyper

---

## 🧠 Grundbegreber i Node-RED

- **Node**: En funktionel blok i dit flow. F.eks. en `inject`-node sender data, en `function`-node bearbejder data, og en `debug`-node viser data i editoren.
- **Flow**: Et diagram bestående af noder, der arbejder sammen i rækkefølge. Flows kan være sekventielle eller parallelle.
- **msg**: Objektet, der transporteres mellem noder. Det indeholder data og metadata i struktureret form.
- **msg.payload**: Hovedfeltet i `msg`-objektet. Det er her selve informationen (sensorværdi, tekst, tal) ligger.
- **Deploy**: Når du klikker "Deploy", gemmer og aktiverer du dit flow i runtime-miljøet.

---

## 🧪 Trin-for-trin: Dit første flow

1. **Åbn Node-RED i browseren**:
   - Naviger til: `http://localhost:1880`

2. **Træk en `inject`-node ind på canvas**:
   - Dobbeltklik → Skift payload type til "string" → Indtast tekst: `Hej Node-RED`

3. **Træk en `debug`-node** ind på canvas:
   - Forbind `inject`-noden til `debug`-noden ved at trække en linje imellem dem

4. **Klik på knappen "Deploy" øverst til højre**:
   - Tryk herefter på den lille grå knap i `inject`-noden for at sende beskeden
   - Du bør nu se din tekst i debug-panelet i højre side af editoren

> 🎉 Du har netop bygget og aktiveret dit allerførste flow i Node-RED – en grundlæggende, men vigtig øvelse.

---

## 📌 Vigtige standardnoder i Node-RED

| Node-type  | Funktion                                            | Eksempel                                                  |
|------------|-----------------------------------------------------|-----------------------------------------------------------|
| inject     | Starter flow manuelt eller med tidsstyring          | "Send tekst hver 5. sekunder"                            |
| debug      | Viser data i højre debug-panel                     | `msg.payload` vises ved aktivering                        |
| function   | JavaScript-kodeblok der manipulerer `msg`          | F.eks. `msg.payload = msg.payload * 2; return msg;`       |
| change     | Ændrer, sætter eller fjerner felter i `msg`        | Erstat `msg.payload` med fast værdi eller flyt felter     |
| switch     | Sender `msg` til forskellige outputs afhængigt af indhold | Send kun videre hvis `msg.payload > 100`           |
| delay      | Indsætter forsinkelse                              | Udsæt besked i 1 sekund, eller begræns frekvensen         |
| template   | Formaterer tekst, HTML eller JSON                  | Brug til brugerflade eller logningsstruktur               |

---

## 📝 Opgaver
1. Lav et flow der sender tekstbeskeder med forskellige `inject`-noder til én `debug`-node
2. Brug en `function`-node til at manipulere `msg.payload`, fx ændre tekst til versaler
3. Tilføj en `switch`-node der sender data til forskellige outputs baseret på tekstindhold
4. Indsæt en `delay`-node og observer hvordan beskeden forsinkes eller begrænses
5. Eksperimentér med `template`-noden og lav en statisk HTML-visning af beskeden

---

## ✅ Læringsudbytte
Efter dette modul vil du kunne:
- Navigere i Node-RED-editorens brugergrænseflade
- Oprette og forbinde noder til simple flows
- Udføre første flow med debug-feedback
- Forstå hvordan data (i `msg.payload`) flyder og transformeres gennem noder
- Udføre en grundlæggende Node-RED installation og installere nødvendige udvidelser

---

## 💡 Tips til videre arbejde
- Brug `comment`-noder til at annotere og forklare dine flows
- Gem dine flows som JSON-filer (Menu → Export → Clipboard → Gem i tekstfil)
- Tilføj farvekodede noter og grupper til dine flows for overblik
- Test ét trin ad gangen og brug `debug` efter vigtige noder
- Hold din Node.js og noder opdaterede via `npm outdated && npm update`

Når du er tryg ved flowopbygning, nodetyper og runtime, er du klar til næste trin: Seriel kommunikation med en mikrokontroller i Modul 02.

