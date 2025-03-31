# 🌌 Introduktion til Modbus TCP og ESP32

I denne workshop skal vi bruge **ESP32** til at kommunikere med en Modbus TCP-server over WiFi. Vi bruger **MicroPython** som programmeringssprog og arbejder hands-on med registrene, der er typiske i industriel automation.

---

## 🛠️ Hvad er Modbus TCP?
**Modbus TCP** er en industriel kommunikationsprotokol, der anvender TCP/IP-netværk til at udveksle data mellem en **client** (ESP32) og en **server** (fx en PLC eller PC).

### 🔌 Modbus datatyper
Modbus arbejder med registre:
- **Coils (0xxxx)**: digitale outputs (boolske)
- **Discrete Inputs (1xxxx)**: digitale inputs (kun læsning)
- **Input Registers (3xxxx)**: analoge inputs (kun læsning)
- **Holding Registers (4xxxx)**: analoge outputs (læs/skriv)

Vi fokuserer på **holding registers** i denne workshop.

---

## 🚀 Mål for workshoppen
- Forstå opbygningen af Modbus TCP-rammer og registerstruktur
- Få ESP32 til at forbinde til en Modbus TCP-server via WiFi
- Læs og skriv holding registers fra MicroPython
- Visualisér Modbus-data i Python på PC (valgfrit)

---

## 🚀 Kommunikationstopologi
```
[ESP32] --- WiFi ---> [Modbus TCP Server på PC eller PLC]
```
ESP32 fungerer som **klient**, der initierer forespørgsler og henter/skriver data.

Modbus TCP-serveren kan enten være:
- En faktisk PLC med Modbus-understøttelse
- En virtuel server på din PC (fx **pymodbus**, **ModbusPal**, **QModMaster**)

---

## 🧰 Forudsætninger
- ESP32 med MicroPython installeret (se modul 02)
- Et fungerende WiFi-netværk
- Kendskab til Python og terminal
- Modbus TCP-server klar (eller klar til at blive sat op)

---

I næste modul installerer vi MicroPython og forbinder ESP32 via USB: `02-micropython-setup.md`


