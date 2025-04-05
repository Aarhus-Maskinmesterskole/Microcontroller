# 📄 Modul 1 – Introduktion til system og komponenter

## 🎯 Formål

Modulet introducerer deltagerne til de grundlæggende komponenter og systemarkitekturen i projektet. Det giver overblik over ESP32, IPC, PLC og deres roller i det samlede system.

## 🧩 Systemarkitektur

Systemet består af:
- **ESP32**: Mikrocontroller til opsamling af data fra sensorer
- **Sensorer**: Temperatur (DHT22), Gas (MQ2), Lys (LDR)
- **IPC (Industrial PC)**: Visualiserer og logger data, samt kommunikerer med PLC
- **PLC**: Modtager eller sender styringsdata

## 🗺 Diagram

Tegn et blokdiagram med:
- Pile fra sensorer til ESP32
- Seriel forbindelse fra ESP32 til IPC
- Modbus/TCP eller Snap7 fra IPC til PLC

## 📝 Opgave

1. Sæt dig ind i og beskriv hvad en ESP32 er, og hvordan den programmeres med MicroPython.
2. Find information om Node-RED og hvordan det visualiserer data.
3. Undersøg hvordan PLC'er kommunikerer med eksterne enheder (fx Snap7 eller Modbus TCP).
4. Udarbejd et simpelt blokdiagram over hele systemet.

## ✅ Output

- Kort beskrivelse af de anvendte komponenter (ESP32, sensorer, IPC, PLC)
- Blokdiagram over systemet
- Forståelse af datavejen fra sensor til IPC