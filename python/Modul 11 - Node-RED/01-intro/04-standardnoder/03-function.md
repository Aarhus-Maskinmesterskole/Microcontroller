# 🧮 03 – Function-noden

`function`-noden er en af de mest kraftfulde noder i Node-RED, fordi den tillader dig at skrive **JavaScript-kode**, der kan manipulere beskeder, oprette nye værdier eller udføre beregninger.

---

## 🎯 Formål
- Ændre `msg.payload` med egne beregninger
- Tilføje nye felter til beskeden
- Kontrollere logik, forgrening og strukturering

---

## 📦 Beskeder og struktur i Node-RED
I Node-RED sendes data mellem noder i form af **beskeder** – kaldet `msg`. Hver besked er et JavaScript-objekt med flere egenskaber:

```javascript
{
  payload: 123,
  topic: "sensor/temperatur",
  _msgid: "8a73f70.16f0a9"
}
```

- `msg.payload`: Hovedindholdet – fx en måling, tekst eller JSON-objekt
- `msg.topic`: Bruges ofte til at kategorisere beskeder (kan sammenlignes med en overskrift eller datakilde)

En **node tager en `msg` som input**, behandler den, og sender typisk en ny eller modificeret `msg` videre til næste node.

---

## 🧪 Eksempel: Gange input med 2
1. Tilføj en `inject`-node og sæt payload til et tal, fx `5`
2. Tilføj en `function`-node og indsæt følgende kode:
```javascript
msg.payload = msg.payload * 2;
return msg;
```
3. Forbind til en `debug`-node og klik Deploy

Output bliver:
```
msg.payload : number
10
```

---

## ⚙️ Funktionelt input og output
- Funktionens input er altid `msg`
- Du kan læse og skrive til `msg.payload`, `msg.topic` eller tilføje fx `msg.status = 'OK'`
- Returnér et objekt (eller array) for at sende det videre

```javascript
msg.temperature = 22.5;
msg.unit = "C";
return msg;
```

Du kan også sende **flere beskeder**:
```javascript
return [msg1, msg2];
```

---

## 🛠 Tips til brug
- Brug `typeof` til at kontrollere datatyper:
```javascript
if (typeof msg.payload === 'number') {
  msg.payload = msg.payload + 10;
}
```
- Du kan returnere `null` for at stoppe beskeden
- Brug `node.warn()` eller `node.error()` til fejlhåndtering

---

## 🧠 Avancerede anvendelser
- Byg objekter som JSON:
```javascript
msg.payload = {
  id: 1,
  status: "OK",
  value: 123.45
};
return msg;
```
- Kombinér med `switch` for betingede flows
- Opret `context`-variabler for at gemme værdier mellem beskeder

---

## ✅ Klar til næste node
👉 Fortsæt med `04-change.md` og lær hvordan man ændrer beskeder uden kode

