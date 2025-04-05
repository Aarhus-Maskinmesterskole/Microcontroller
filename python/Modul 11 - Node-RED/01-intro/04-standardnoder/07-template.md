# 🧾 07 – Template-noden

`template`-noden bruges til at **formatere tekst, HTML eller JSON** baseret på inputdata. Den fungerer som en mini-skabelonmotor, hvor du kan kombinere statisk og dynamisk indhold direkte i dit flow.

---

## 🎯 Formål
- Generere tekstbeskeder med dynamiske data
- Skabe HTML-output til dashboards
- Opbygge JSON-strukturer på baggrund af beskedfelter

---

## 🧪 Eksempel: Dynamisk tekst med måleværdi
1. Tilføj en `inject`-node med payload = 24.5 (number)
2. Tilføj en `template`-node med følgende indhold:
```text
Temperaturmåling: {{payload}} °C
```
3. Tilføj en `debug`-node og forbind

Resultat i debug:
```
msg.payload : string
Temperaturmåling: 24.5 °C
```

---

## ⚙️ Skabelonsyntaks (Mustache)
Node-RED bruger [Mustache-syntaks](https://mustache.github.io/) til at udfylde skabeloner. Du kan referere til felter i `msg`, fx:

| Skabelon               | Effekt                                               |
|------------------------|------------------------------------------------------|
| `{{payload}}`          | Viser indhold af `msg.payload`                      |
| `{{topic}}`            | Viser `msg.topic`                                   |
| `{{payload.value}}`    | Viser `msg.payload.value`, hvis `payload` er et objekt |

Du kan også lave multiline-tekst og HTML:
```html
<h3>Sensorværdi:</h3>
<p>{{payload}} °C</p>
```

---

## 📄 Eksempel: Generér JSON-output
1. Tilføj en `template`-node
2. Vælg "Output as parsed JSON"
3. Indsæt:
```json
{
  "status": "OK",
  "måling": {{payload}},
  "enhed": "°C"
}
```
4. Output vil nu være et struktureret JSON-objekt som `msg.payload`

> 📌 Du kan bruge dette til at pakke data til API-kald, logning eller videre analyse.

---

## 🧠 Tips til brug
- Template-noden kan bruges i både backend og frontend (fx `ui_template` til dashboards)
- Kombiner med `change`- eller `function`-noder for at forberede dine data først
- Husk at vælge korrekt output-type: tekst, HTML eller JSON
- Brug `{{payload}}` og `{{topic}}` som minimum – og udvid efter behov

---

## 🌐 Avanceret: Brug af `ui_template`
- `ui_template` er en særskilt node fra `node-red-dashboard`
- Tillader dig at skrive HTML, CSS og AngularJS direkte til brugergrænsefladen
- Du kan binde værdier med `{{msg.payload}}` og skabe widgets, grafer eller dynamisk tekst

Eksempel:
```html
<div>
  <h3 style="color:green">Systemstatus:</h3>
  <p>{{msg.payload}}</p>
</div>
```

---

## ✅ Sammenfatning
`template`-noden er en alsidig komponent til:
- Formatér data til tekst eller HTML
- Pak data i strukturerede formater
- Skab visuel feedback eller rapportering i flows

👉 Med denne node i værktøjskassen kan du nu gå videre til de næste moduler og bygge endnu mere udtryksfulde og interaktive flows.


