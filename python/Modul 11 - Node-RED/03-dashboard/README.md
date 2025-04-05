# 📄 Modul 03 – Realtidsvisualisering i Node-RED Dashboard

## 🎯 Formål
Dette modul introducerer dig til visualisering af data i realtid ved hjælp af Node-RED’s dashboard-komponent. Du vil lære at anvende en række forskellige UI-elementer som `chart`, `gauge`, `text`, `switch`, `button` og `ui_group` for at give brugere (f.eks. operatører) mulighed for både at overvåge og interagere med systemet. Visualisering er afgørende i automatiseringssystemer, hvor overblik, status og hurtig reaktion er centrale.

---

## 🧰 Forudsætninger
- Du har installeret `node-red-dashboard` (`npm install node-red-dashboard`)
- Du har gennemført Modul 02 og kan modtage serielle data
- Din browser er klar til at vise dashboardet på `http://localhost:1880/ui`

---

## 🧠 Grundbegreber

- **Dashboard**: Grafisk brugerflade genereret af Node-RED baseret på UI-noder
- **ui_group**: En logisk gruppe af komponenter
- **ui_tab**: Et faneblad hvor flere grupper kan samles
- **Widgets**: Interaktive elementer som charts, knapper og indikatorer

---

## 📊 Opret dit første dashboard

1. Træk en `ui_chart`-node ind i dit flow
   - Forbind den til en `function` eller direkte til `serial in`
   - Dobbeltklik på noden → Opret ny `tab` og `group`

2. Tilføj en `ui_gauge`-node
   - Angiv værdier (min/max) og enhed (fx Lux, °C, %)
   - Forbind til samme datakilde som chart

3. Tilføj en `ui_text`-node
   - Bruges til at vise seneste værdi som tal eller tekst

4. Klik på **Deploy** og åbn `http://localhost:1880/ui`

---

## 💻 Eksempel – Flowstruktur
```text
[ serial in ] → [ function ] → [ gauge ]
                                 ↘ [ chart ]
                                 ↘ [ text ]
```

Eksempel på `function`-node:
```javascript
let val = parseInt(msg.payload);
msg.payload = val;
return msg;
```

---

## 🎛️ Avancerede widgets (valgfrit)
- `ui_slider`: Brugeren vælger en værdi (fx setpunkt)
- `ui_button`: Udløs handling som videresendes til mikrokontroller eller script
- `ui_switch`: Tænd/sluk tilstand, fx ventilator

Du kan bruge disse sammen med `change`, `function` og `serial out` for at sende data tilbage til en mikrokontroller eller Python-script.

---

## 📝 Opgaver
1. Visualisér sensorværdier med både `gauge` og `chart`
2. Tilføj et tekstfelt der viser dato og klokkeslæt for seneste opdatering
3. Implementér et `ui_switch` til at simulere manuel tænd/sluk af en enhed
4. Kombinér `ui_slider` med `serial out` og verificér output
5. Dokumentér layout og grupper med `comment`-noder

---

## ✅ Læringsudbytte
Efter dette modul kan du:
- Designe og strukturere brugerflader i Node-RED dashboard
- Vælge relevante UI-komponenter til dine målinger og kontroller
- Visualisere data i realtid og formatere dem for klar præsentation
- Interagere med flows gennem brugerinput (slider, switch, knap)

---

I næste modul ser vi på, hvordan du logger data til CSV-filer og gemmer målinger over tid for senere analyse eller dokumentation.

