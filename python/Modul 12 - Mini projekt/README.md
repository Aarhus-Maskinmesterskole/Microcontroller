# 🚀 Workshop: Node-RED, ESP32 og IPC-kommunikation

## 📌 Introduktion

Denne workshop guider dig gennem opsamling, visualisering og kommunikation af data mellem ESP32, IPC (med Node-RED) og en PLC. Fokus er på praktisk anvendelse, kravspecifikation, tests og dokumentation i henhold til PEP8.

## 🎯 Mål

- Dataopsamling fra ESP32 (DHT22, MQ2, LDR)
- Seriel kommunikation mellem ESP32 og IPC (USB)
- Visualisering og logging i Node-RED
- Overførsel af data til PLC (via Modbus TCP)
- Udarbejdelse af kravspecifikation og blokdiagram
- FAT/SAT/SIT-test og dokumentation

## 👌 Det du lærer

- Opsætning af ESP32 og sensorer
- Opsamling og print af CSV-lignende sensor output
- Seriel parsing og real-time dashboard i Node-RED
- Logging til CSV via Node-RED
- Kommunikere med PLC via Modbus
- Udarbejde teknisk dokumentation og testplaner

## 📅 Moduloversigt

| Modul | Filnavn                   | Emne                                       |
|-------|---------------------------|--------------------------------------------|
| 1     | 01-introduction.md        | Introduktion til system og komponenter     |
| 2     | 02-kravspecifikation.md   | Kravspecifikation og blokdiagram           |
| 3     | 03-esp32-setup.md         | Opsætning af ESP32 og MicroPython          |
| 4     | 04-sensor-data.md         | Opsamling og udskrivning af sensorværdier  |
| 5     | 05-serial-node-red.md     | Seriel kommunikation og parsing i Node-RED |
| 6     | 06-visualisering-logging.md | Real-time graf og CSV-logging              |
| 7     | 07-plc-kommunikation.md   | PLC-kommunikation via Snap7           |
| 8     | 08-fat-sat-sit.md         | Testplaner og validering                   |
| 9     | 09-dokumentation.md       | Teknisk dokumentation og PEP8-guidelines   |

## 🔧 Krav før du starter

### Hardware og software

- ESP32 med MicroPython installeret
- IPC med Node-RED installeret
- PLC med Modbus TCP (eller PLCSIM Advanced)
- (Valgfrit) Python 3.x til CSV-håndtering uden Node-RED

### Python-pakker (valgfrit)

```bash
pip install pyserial pandas
```

## 🚀 Mappestruktur (GitHub)

```plaintext
NodeRED-ESP32-Workshop/
├── modules/
│   ├── 01-introduction.md
│   ├── ...
│   └── 09-dokumentation.md
├── kode/
│   ├── esp32/main.py
│   ├── node-red/flow.json
│   └── python/csv_logger.py
├── dokumentation/
│   ├── kravspecifikation.pdf
│   ├── blokdiagram.drawio
│   ├── fat-sat-sit.xlsx
│   └── teknisk-dokumentation.md
├── README.md
└── LICENSE
```

## 🏆 Klar til start!

Du er nu klar til at arbejde med embedded systemer, seriel kommunikation, dataanalyse og dokumentation i praksis!
Gå til ![01-introduction](01-introduction.md)

