# ⚙️ 02 – Dit første flow i Node-RED

Dette dokument guider dig trin-for-trin gennem opbygningen af dit første flow i Node-RED. Målet er at introducere dig for brugerfladen, hvordan man forbinder noder, og hvordan data (`msg.payload`) bevæger sig gennem et flow.

---

## 🎯 Formål
- Oprette og forbinde noder
- Bruge `inject` og `debug` noder
- Deploye og aktivere et flow
- Observere dataflow og output

---

## 📂 Forberedelse
Gå til *kommando prompt* Sørg for at Node-RED kører på din maskine:
```bash
node-red
```
Åbn derefter din browser og gå til:
```
http://localhost:1880
```

---

## 🧪 Trin-for-trin: Lav dit første flow

### 1. Opret `inject` node
- Find `inject`-noden i venstre menu
- Træk den ind på arbejdsområdet (canvas)
- Dobbeltklik på noden for at konfigurere
  - Sæt `payload` til **string**
  - Indtast tekst: `Hej Node-RED`
  - Klik “Done”

### 2. Opret `debug` node
- Find `debug`-noden i menuen
- Træk den ind på canvas
- Forbind `inject` til `debug` ved at trække en linje mellem dem
- `debug`-noden viser som standard `msg.payload`

### 3. Klik “Deploy” øverst til højre
Dette gemmer og aktiverer dit flow.

### 4. Kør flowet
- Klik på den lille grå knap til venstre for `inject`-noden
- I højre side af skærmen (debug-panelet) vil du se:
```
msg.payload : string
“Hej Node-RED”
```

> 🎉 Tillykke! Du har netop bygget og aktiveret dit første flow i Node-RED.

---

## 📝 Øvelse
Prøv nu selv at:

- Oprette flere `inject`-noder med forskelligt indhold
- Bruge `function`-noden til at ændre `msg.payload`
- Tilføje en `switch`-node der sender forskellige data til forskellige outputs
- Tilføje en `template`-node for at lave simpel tekstformatering

---

## ✅ Klar til næste trin
Du har nu et grundlæggende kendskab til flows, noder og data. Næste dokument handler om de centrale begreber i Node-RED: `msg`, `payload`, `flow`, `node`, `runtime`, og `deploy`. Fortsæt til `03-node-red-begreber.md`.

