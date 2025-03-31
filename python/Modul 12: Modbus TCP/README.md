# 🚀 Workshop: ESP32 som Modbus TCP-klient med MicroPython

## 🎯 Hvad du lærer:

✔️ Grundlæggende om Modbus TCP-protokollen  
✔️ Installation af MicroPython på ESP32   
✔️ Brug af umodbus (eller andet MicroPython-bibliotek)   
✔️ Læsning og skrivning af holding/input registers    
✔️ Dataopsamling og visualisering i Python    
✔️ Brug af Modbus TCP-server til test (f.eks. på PC)    

## 🧱 Modulstruktur
|Modul|	Filnavn|	Indhold|
|-----|--------|---------|
|📄 01|	01-intro-modbus.md|	Introduktion til Modbus TCP og ESP32|
|📄 02|	02-micropython-setup.md|	Flash MicroPython og opsætning af ESP32|
|📄 03|	03-modbus-client.md|	Kør ESP32 som Modbus TCP-klient|
|📄 04|	04-modbus-server.md|	Opsætning af PC som Modbus TCP-server (fx ModbusPal, pymodbus)|
|📄 05|	05-data-read-write.md|	Læs og skriv registre fra ESP32|
|📄 06|	06-error-handling.md|	Fejlhåndtering og timeout-diagnostik|
|📄 07|	07-integration.md|	Opsamling og visning af data i Python på PC|

## 🔧 Krav
### 💻 Software:
- Thonny / mpremote / rshell
- MicroPython firmware
- umodbus eller modbus-tcp bibliotek
- PC med Modbus TCP-server (pymodbus / ModbusPal / PLCsim)

## 📦 Installation på PC (eksempel med pymodbus):
```python
pip install pymodbus
```
## 📱 Hardware:
- ESP32 med WiFi
- En sensor (valgfrit)
- Adgang til testserver på PC (localhost eller LAN)
