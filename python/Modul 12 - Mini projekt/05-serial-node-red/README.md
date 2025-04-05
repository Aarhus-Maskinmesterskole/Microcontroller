# 📄 Modul 5 – Seriel kommunikation og parsing i Node-RED

## 🎯 Formål

I dette modul skal du lære at etablere seriel kommunikation mellem din ESP32 og IPC via USB og modtage data i Node-RED. Målet er at kunne læse de kommaseparerede sensorværdier fra ESP32, parse dem i Node-RED og forberede dem til visualisering eller logging.

---

## 📦 Hvad du skal bruge

- ESP32 med kørende MicroPython-program fra Modul 4.
- IPC (eller almindelig PC) med Node-RED installeret.
- USB-forbindelse mellem ESP32 og IPC.
- Tilføjelse af `node-red-node-serialport` i Node-RED.

> 💡 Node-RED skal køre med adgang til den serielle port (COMx eller /dev/ttyUSBx). Du skal muligvis starte Node-RED med administrator/root-rettigheder.

---

## 🧪 Trin 1: Installer nødvendige noder

1. Åbn Node-RED i din browser (typisk på http://localhost:1880).
2. Gå til menuen (øverst til højre) → `Manage palette`.
3. Klik på `Install`.
4. Søg efter `node-red-node-serialport` og installer.

---

## 🔌 Trin 2: Opret seriel forbindelse i Node-RED

1. Træk en **serial in** node ind på flowet.
2. Dobbeltklik og konfigurer:
   - Serial port: fx `/dev/ttyUSB0` eller `COM3`.
   - Baudrate: `115200`.
   - Output: `stream of Strings`.
   - Newline karakter: `\n`.
3. Tilføj en **split** node til at dele CSV-strengen op i værdier.
4. Brug evt. en **function** node til at konvertere til JSON-objekt:

```javascript
let parts = msg.payload.split(",");
msg.payload = {
    temperature: parseFloat(parts[0]),
    humidity: parseFloat(parts[1]),
    gas: parseInt(parts[2]),
    light: parseInt(parts[3])
};
return msg;
```

5. Tilføj en **debug** node og en **chart** eller **gauge** node fra dashboard (hent node fra manage palette) for at vise data.

---

## 🌐 Eksempel-flow (beskrivelse)

```text
[serial in] → [function] → [debug + gauge + chart]
```

- `serial in` læser fra USB.
- `function` omdanner CSV til JSON.
- `debug` viser data i sidebar.
- `gauge/chart` visualiserer temperatur, gas, lys etc.

> Gem flowet jævnligt. Brug evt. `inject` node til test.

---

## 📝 Opgave
1. Installer `node-red-node-serialport`.
2. Lav flow med `serial in` og parser til JSON.
3. Visualiser mindst to værdier i dashboard.
4. Vis data i `debug`-vinduet.
5. Prøv at simulere fejl: fx hvis én værdi mangler i CSV – hvad sker der?
6. Udvid flowet til at sende en advarsel, hvis gas-værdien overstiger et grænsetal.

---

## ✅ Output
- Node-RED modtager data korrekt fra ESP32 via USB.
- CSV-strenge parses til JSON.
- Data vises i debug og som visuelle elementer.
- Flowet håndterer fejl og uventede input.

---

## 💡 Tips
- Brug `console.log()` i ESP32-koden til fejlsøgning.
- Tjek at ESP32 sender nye linjer `\n` og ikke `\r\n`.
- Brug `node.status()` i function node for fejlindikator.
- Du kan også gemme data i fil eller sende til cloud i næste modul.

Når du har lært at modtage og parse data, er du klar til at logge dem og viderebehandle dem – fx til CSV eller PLC!