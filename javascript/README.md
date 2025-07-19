# 🌍 JavaScript Workshop: IoT & Microcontrollers

Velkommen til JavaScript-delen af Microcontroller workshoppen! Her lærer du at bruge JavaScript til at interagere med microcontrollers via Node.js.

---

## 🎯 Læringsmål

Efter denne workshop vil du kunne:

- 📡 **Seriel kommunikation med JS**: Læs data fra ESP32 med Node.js
- 🔧 **Johnny-Five integration**: Brug af Johnny-Five til Arduino & ESP32
- 🌐 **IoT-dashboard**: Byg et dashboard med Vue.js eller React
- 📊 **Realtidsdata**: Websockets og realtids datavisualisering

---

## 📦 Hvad er Node.js for IoT?

Node.js giver dig mulighed for at kontrollere hardware direkte fra JavaScript. Med biblioteker som Johnny-Five og serialport kan du nemt kommunikere med microcontrollers.

---

## ⚙️ Kom godt i gang

1️⃣ **Installer Node.js**: https://nodejs.org/

2️⃣ **Installer afhængigheder**:
```bash
npm install serialport johnny-five
```

3️⃣ **Tilslut din ESP32** og kør dit første script

---

## 🔧 Grundlæggende eksempler

### Seriel kommunikation
```javascript
const { SerialPort } = require('serialport');
const { ReadlineParser } = require('@serialport/parser-readline');

const port = new SerialPort({
  path: '/dev/ttyUSB0',
  baudRate: 115200
});

const parser = port.pipe(new ReadlineParser({ delimiter: '\n' }));

parser.on('data', (data) => {
  console.log('Modtaget data:', data);
});
```

### Johnny-Five LED control
```javascript
const five = require('johnny-five');
const board = new five.Board();

board.on('ready', () => {
  const led = new five.Led(13);
  led.blink(500);
});
```

---

## 🌐 Web integration

JavaScript's styrke ligger i web-integration. Du kan nemt skabe:

- **Realtids dashboards** med Socket.io
- **REST APIs** for sensordata
- **Progressive Web Apps** til IoT kontrol

---

## 🤝 Bidrag & Feedback

Har du forslag eller ønsker at bidrage? Opret en **issue** eller en **pull request**!

🚀 **God læring og happy coding!** 🎉