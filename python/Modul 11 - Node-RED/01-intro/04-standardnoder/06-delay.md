# ⏱️ 06 – Delay-noden

`delay`-noden bruges til at **forsinke beskeder** eller **begrænse antallet af beskeder pr. sekund**. Den er nyttig, når du vil simulere tidsforsinkelse eller undgå, at dit flow bliver overbelastet.

---

## 🎯 Formål
- Forsinke beskeder med fast tid (ms eller sekunder)
- Begrænse antallet af beskeder i et givent tidsinterval
- Skabe pacing i flows med høj frekvens

---

## 🧪 Eksempel 1: Fast forsinkelse
1. Tilføj en `inject`-node med `payload = "Start"`
2. Tilføj en `delay`-node
   - Mode: **delay each message**
   - Delay: 3 sekunder
3. Tilføj en `debug`-node og forbind
4. Klik Deploy og test

Du vil se beskeden i debug-panelet – men **3 sekunder efter**, du klikkede på inject.

---

## 🧪 Eksempel 2: Rate limiting
1. Tilføj en `inject`-node med repeat = hver 0.1 sekunder
2. Tilføj en `delay`-node
   - Mode: **Rate limit**
   - Maximum rate: 1 besked hvert sekund
3. Tilføj en `debug`-node og forbind

Nu vil Node-RED begrænse antallet af beskeder, der sendes videre, til én i sekundet.

---

## ⚙️ Indstillinger i delay-noden
| Indstilling             | Funktion                                                  |
|-------------------------|-----------------------------------------------------------|
| Delay each message      | Forsinker hver enkelt besked med angivet tid             |
| Rate limit              | Maksimalt antal beskeder pr. sekund eller minut          |
| Drop intermediate msgs  | Slipper kun første/nyeste besked – resten smides væk     |
| Queue all msgs          | Venter med at sende til der er plads                     |

> ⏳ Bemærk at delay-noden ikke ændrer beskeden – den påvirker **timingen**.

---

## 🧠 Tips
- Brug `delay` når du arbejder med flows der sender mange målinger hurtigt
- Kombinér med `switch` for kun at forsinke bestemte beskeder
- Brug til at simulere svartider fra hardware

---

## ✅ Klar til næste node
👉 Gå videre til `07-template.md` og lær hvordan du kan generere tekst og HTML dynamisk

