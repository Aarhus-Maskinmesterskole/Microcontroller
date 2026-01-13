# 🧰 00_introduktion: ESP32, Serielle Data og CSV-format

Velkommen til første modul i workshoppen! Her introduceres du til ESP32 som datakilde, hvordan den kommunikerer med computeren via seriel forbindelse, og hvordan vi arbejder med CSV-formatet til dataanalyse.

---

## 🎯 Læringsmål

Efter dette modul vil du kunne:

- Forstå, hvordan ESP32 sender data over USB/seriel forbindelse
- Forklare hvad CSV-formatet er, og hvorfor det er nyttigt
- Kende til grundprincipperne i dataopsamling med sensorer

---

## 📦 Hvad er ESP32?

ESP32 er en billig og kraftfuld mikrocontroller med Wi-Fi og Bluetooth. I denne workshop bruges den til at sende sensor- eller simuleret data i realtid til din computer via USB.

> Har du aldrig arbejdet med ESP32 før? Bare rolig. I næste modul opsætter vi det trin-for-trin.

---

## 🔌 Hvad er Seriel Kommunikation?

Seriel kommunikation er en metode hvor data sendes én bit ad gangen via USB-kabel. Vi bruger Python og `pyserial`-biblioteket til at aflæse disse data.

Eksempel på seriel output fra ESP32:

```
23.5, 45.1, 1013.6
23.4, 45.2, 1013.7
```

Dette kunne f.eks. være temperatur, fugtighed og lufttryk i CSV-format.

---

## 📄 Hvad er CSV?

CSV (Comma-Separated Values) er en simpel og udbredt måde at gemme data på. Hver linje i filen er en datapunkt, og hver værdi er adskilt med komma:

```csv
temp,hum,pressure
23.5,45.1,1013.6
23.4,45.2,1013.7
```

Vi bruger `pandas` til at indlæse og analysere CSV-filer i Python.

---

## ✅ Klar til næste trin?

Nu hvor du forstår formålet med ESP32 og CSV-data, er du klar til at opsætte din ESP32 og begynde at aflæse data i næste modul:

➡️ Gå videre til [`01_esp32_setup/`](../01_esp32_setup/)

---

📌 Tip: Hvis du ikke har en sensor, kan du sende simuleret data med `random()` i ESP32-koden!