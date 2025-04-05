# 📄 Modul 02 – Seriel kommunikation med mikrokontroller

## 🎯 Formål
I dette modul lærer du at oprette og teste seriel kommunikation mellem Node-RED og en mikrokontroller, typisk via USB (fx ESP32, Arduino, eller lignende). Seriel kommunikation er en af de mest almindelige metoder til dataudveksling i embedded systemer, og Node-RED har native understøttelse for dette via `serial in` og `serial out` noder. Du vil få erfaring med at modtage, parse og viderebehandle data i realtid.

---

## 🧰 Forudsætninger
- Du har en fungerende Node-RED installation med `serialport`-noden installeret
- Du har en mikrokontroller med USB-tilkobling, som sender data til computeren
- Eventuelt: Driver til CH340 eller CP210x er installeret afhængigt af hardware
- Din mikrokontroller sender gentagne eller triggere data over seriel port i klar tekst eller CSV-format

---

## 🔌 Forbindelse og portidentifikation

### 🔍 Find den korrekte port
- **Windows:** Brug Enhedshåndtering → Porte (COM og LPT)
- **Linux/Mac:** Brug `ls /dev/tty*` før og efter tilkobling af enheden

### 📋 Eksempel: Serial output fra ESP32 i MicroPython
```python
import time
import machine
from machine import ADC

ldr = ADC(machine.Pin(34))
ldr.atten(ADC.ATTN_11DB)

while True:
    value = ldr.read()
    print("LDR:", value)
    time.sleep(1)
```

Output i seriel port vil ligne:
```
LDR: 1234
LDR: 1241
LDR: 1250
```

---

## 🧪 Opret dit første serielle flow

1. Tilføj en `serial in`-node
   - Dobbeltklik og vælg den korrekte port (fx `/dev/ttyUSB0` eller `COM4`)
   - Baud rate = 115200 (afhængigt af din mikrokontroller)
   - Output som tekst (ikke buffer)

2. Tilføj en `debug`-node og forbind den til `serial in`
   - Deploy flowet
   - Når mikrokontrolleren sender data, vises det i debug-panelet

3. (Valgfrit) Tilføj en `function`-node til parsing
```javascript
let parts = msg.payload.split(":");
msg.sensor = parts[0];
msg.payload = parseInt(parts[1]);
return msg;
```

4. Tilføj en `chart` eller `gauge` fra dashboard, og vis data i realtid

---

## 🛠️ Fejlfinding
- Intet input? Kontroller at COM-port er korrekt og at baud-rate matcher
- Data uforståelig? Kontroller output-format fra mikrokontroller
- `serialport` fejler? Genstart Node-RED og prøv at geninstallere pakken

```bash
npm install node-red-node-serialport
```

---

## 📝 Opgaver
1. Opret serielt flow med debug og visualisering
2. Udvid med `function`-node der også tilføjer timestamp
3. Gem seneste værdi i `flow.set()` for senere brug i anden del af flowet
4. Tilføj `ui_text` og `ui_chart` noder for visuel feedback
5. Test hvordan mikrokontrolleren reagerer ved at sende forskellige data (simulér fejl og outliers)

---

## ✅ Læringsudbytte
Efter dette modul kan du:
- Identificere og forbinde en seriel port til Node-RED
- Modtage og afkode data sendt fra en mikrokontroller
- Strukturere og parse serielle data til brug i visualisering og logning
- Implementere et stabilt flow til opsamling og visning af realtidsdata

---

Modul 03 vil bygge videre på dette ved at udvide med realtidsdashboard og opsætning af `ui`-noder til operatørbrug.

