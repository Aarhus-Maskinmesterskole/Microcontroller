# 🔄 04 – Change-noden

`change`-noden bruges til at **ændre, slette eller kopiere felter** i en besked (`msg`) uden at skrive kode. Det er en visuel og enkel måde at transformere data i et flow.

---

## 🎯 Formål
- Ændre værdien af `msg.payload` eller andre felter
- Slette unødvendige felter
- Omdøbe eller kopiere værdier til nye felter

---

## 🧪 Eksempel: Erstat tekst
1. Tilføj en `inject`-node med `payload` sat til: `status`
2. Tilføj en `change`-node og konfigurer:
   - Action: **Set**
   - Property: `msg.payload`
   - To: `"Maskine kører"`
3. Tilføj en `debug`-node og forbind
4. Klik Deploy og test flowet

Du vil nu se:
```
msg.payload : string
"Maskine kører"
```

---

## ⚙️ Konfigurationsmuligheder
| Handling        | Effekt                                                        |
|----------------|---------------------------------------------------------------|
| Set            | Sætter en ny værdi for et felt                                |
| Change         | Finder og erstatter tekst i en streng                         |
| Delete         | Fjerner et felt fra `msg`                                     |
| Move           | Flytter en værdi fra ét felt til et andet                     |
| Copy           | Kopierer værdien fra ét felt til et andet                    |

> 📌 Tip: Du kan også ændre fx `msg.topic` eller oprette `msg.status`, `msg.level` osv.

---

## 🧠 Eksempler på avanceret brug
- Slet `msg.topic`:
  - Action: **Delete** → Property: `msg.topic`
- Flyt `msg.payload` til `msg.data`:
  - Action: **Move** → From: `msg.payload` → To: `msg.data`
- Find og erstat:
  - Action: **Change** → From: `OFF` → To: `0`

---

## ✅ Klar til næste node
👉 Gå videre til `05-switch.md` og lær at filtrere og forgrene dit flow baseret på dataindhold