# 🐞 02 – Debug-noden

`debug`-noden bruges til at **vise output** af beskeder i Node-RED. Den er afgørende til fejlfinding og til at forstå, hvordan dine `msg`-objekter ser ud gennem et flow.

---

## 🎯 Formål
- Vise indholdet af `msg.payload` eller hele `msg`
- Bruges til fejlfinding og verificering af flowlogik
- Kombineres med næsten alle noder

---

## 🧪 Eksempel: Vis tekst fra inject
1. Tilføj en `inject`-node og vælg `string` som payload: `Hej Node-RED`
2. Tilføj en `debug`-node og forbind den med `inject`
3. Klik “Deploy” og tryk på `inject`

Du ser i højre side:
```
msg.payload : string
“Hej Node-RED”
```

---

## ⚙️ Konfigurationsmuligheder
| Indstilling             | Funktion                                                    |
|-------------------------|-------------------------------------------------------------|
| Output                  | Vælg om du vil vise `msg.payload`, `msg.topic` eller hele `msg` |
| Label                   | Eget navn på noden i debug-panelet                          |
| Send to debug tab       | Skal output vises i debug-panelet i højre side?             |
| Console output          | (Valgfri) log også til serverens terminal                   |

> 🔍 Du kan vælge at vise hele `msg`-objektet og få adgang til fx `msg.topic`, `_msgid`, m.m.

---

## 🧠 Tips
- Brug **flere debug-noder** i et flow for at se ændringer undervejs
- Brug **labels** for at holde styr på hvor dine outputs kommer fra
- Højreklik og vælg "Disable" for midlertidigt at slå debug fra
- Brug `function`-node + debug for at se effekten af din kode

---

## ✅ Klar til næste node
👉 Gå videre til `03-function.md` for at lære at manipulere dine beskeder med JavaScript

