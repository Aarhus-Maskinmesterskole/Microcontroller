# 📄 Modul 2 – Kravspecifikation og blokdiagram

## 🎯 Formål

Formålet med dette modul er at lære deltagerne at udarbejde en kravspecifikation og visualisere systemets overordnede struktur gennem et blokdiagram.

## 📋 Kravspecifikation

En kravspecifikation beskriver:
- Hvad systemet skal kunne (funktionelle krav)
- Hvordan systemet skal fungere (tekniske krav)
- Hvilke komponenter og interfaces der indgår

### Eksempel: Funktionelle krav
- Systemet skal opsamle data fra tre sensorer: temperatur, gas og lys.
- Data skal overføres til en IPC via seriel kommunikation (USB).
- IPC skal visualisere data i realtid og gemme data i en CSV-fil.
- IPC skal sende data videre til en PLC.

### Eksempel: Ikke-funktionelle krav
- Systemet skal opdatere data hvert sekund.
- Kommunikation mellem enheder skal ske fejlfrit i mindst 10 minutter ad gangen.
- CSV-filen må højst være 10 MB stor.

## 🧩 Blokdiagram

Blokdiagrammet skal vise:
- Sensorer → ESP32 (analog/digital input)
- ESP32 → IPC (USB-seriel forbindelse)
- IPC → PLC (Modbus TCP eller Snap7)

Inkludér pile, navne på komponenter, og korte beskrivelser af forbindelser.

## 📝 Opgave

1. Udarbejd en kravspecifikation i punktform.
2. Tegn et blokdiagram over hele systemet med input/output.
3. Notér hvilke datatyper der forventes fra hver sensor.
4. Angiv opdateringshastighed og minimums-performancekrav.

## ✅ Output

- Kravspecifikation i Markdown eller Word-.
- Blokdiagram (tegnet i Draw.io, papir, eller digitalt værktøj).
- Liste over datatyper og kommunikationshastigheder.

## 💡 Tips
- Brug skabeloner fra tidligere moduler hvis muligt.
- Kravspecifikationen skal kunne bruges til FAT og SAT senere i projektet.

