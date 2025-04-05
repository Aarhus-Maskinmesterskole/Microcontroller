# 🔘 01 – Inject-noden

`inject`-noden bruges til at **starte et flow**. Den kan sende forskellige typer data ind i et flow – manuelt (ved klik) eller automatisk (på et interval).

---

## 🎯 Formål
- Lære at sende forskellige typer data ind i et flow
- Forstå forskellen på manuelle og tidsstyrede injects
- Kombinere med fx `debug`, `function`, `template` eller `switch`

---

## 🧪 Eksempel: Send tekst til debug

1. Træk en `inject`-node ind i editoren
2. Dobbeltklik på den for at åbne konfigurationen
3. Vælg payload-type `string` og skriv fx: `Hej Node-RED`
4. Tilføj en `debug`-node og forbind den
5. Klik “Deploy” og tryk på knappen ved `inject`

Output i debug-panelet:
```
msg.payload : string
“Hej Node-RED”
```

---

## 🛠 Konfigurationsmuligheder
| Felt              | Beskrivelse                                                |
|-------------------|-------------------------------------------------------------|
| Payload-type      | Fx string, number, boolean, timestamp                      |
| Topic             | Bruges til at mærke beskeden med en kategori               |
| Repeat            | Gentag med interval (fx hvert 5. sekund)                   |
| Inject once       | Kør automatisk ved opstart                                 |
| Timestamp         | Standardvalget – sender tidspunktet som tal                |

---

## 🧠 Tips
- Brug `timestamp` når du tester flows og vil se hvornår beskeder ankommer
- Brug `topic` hvis du skal adskille flere injects nedstrøms
- Kombiner med `switch` til betinget styring af flows

---

## ✅ Klar til næste node
👉 Fortsæt med `02-debug.md` for at lære at vise output af dine data