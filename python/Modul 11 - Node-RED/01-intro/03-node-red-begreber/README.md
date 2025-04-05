# 🧠 03 – Centrale begreber i Node-RED

I dette dokument får du en grundig introduktion til de vigtigste begreber i Node-RED. Forståelsen af disse begreber er afgørende for at kunne arbejde effektivt med flows, data og funktionelle noder.

---

## 🎯 Formål
- Forklare begreber som node, flow, msg, msg.payload og deploy
- Skabe forståelse for runtime-miljøet
- Differentiering mellem data og kontrolstruktur i et flow

---

## 📘 Centrale begreber

### 🔹 Node
En **node** er den grundlæggende byggesten i Node-RED. Hver node har en specifik funktion, fx:
- `inject`: sender en besked
- `debug`: viser beskedens indhold
- `function`: tillader JavaScript-kode til at manipulere data
- `switch`: videresender beskeder baseret på indhold

### 🔹 Flow
Et **flow** er en samling af noder forbundet med linjer (wires), hvor data flyder fra én node til den næste. Flows kan organiseres i faner og kan opdeles i logiske sektioner.

### 🔹 msg
Når en node sender data videre, sker det i form af et **msg**-objekt. Det er et JavaScript-objekt, som indeholder forskellige felter – vigtigst af alt:

```json
{
  "payload": "Hej verden",
  "topic": "sensor1",
  "_msgid": "1234567890"
}
```

### 🔹 msg.payload
`msg.payload` er det vigtigste datafelt i `msg`. Det er her den primære information (tekst, tal, målinger, objekter) transporteres.

### 🔹 Deploy
Når du trykker på knappen **Deploy** øverst til højre, bliver dine ændringer gemt og aktiveret. Node-RED kører som en runtime, og deploy opdaterer det aktive flow.

---

## 🧪 Eksempel på dataflow
```text
[inject] → [function] → [switch] → [debug]
```
1. `inject` sender `"50"` som tal
2. `function` ganger værdien med 2: `msg.payload = msg.payload * 2`
3. `switch` sender kun videre hvis `msg.payload > 50`
4. `debug` viser resultatet i højre side

---

## 🧩 Andre nyttige egenskaber i `msg`
| Felt        | Funktion                              |
|-------------|----------------------------------------|
| `msg.topic` | Bruges til at kategorisere beskeder    |
| `msg._msgid`| Unik ID for hver besked                |
| `msg.payload` | Hoveddatafelt for information        |

---

## ✅ Klar til næste trin
Du har nu overblik over hvordan data transporteres og behandles i Node-RED. I næste dokument skal vi dykke dybere ned i hver af de vigtige standardnoder.

👉 Fortsæt til `04-standardnoder/README.md`