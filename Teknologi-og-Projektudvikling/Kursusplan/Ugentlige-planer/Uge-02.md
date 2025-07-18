# 📅 Uge 2: Sensor Integration og Data Læsning
**Teknologi og Projektudvikling - Uge 2**

## 🎯 Ugens Fokus
- Integration af sensorer med ESP32
- Analog og digital sensor læsning
- Grundlæggende databehandling og formatering

## 📚 Lektioner Denne Uge

### 🌡️ Lektion 4: DHT22 Temperatur/Luftfugtighed Sensor
**Mandag** | [Detaljeret plan](../Detaljerede-lektionsplaner/Lektion-04.md)
- DHT22 bibliotek installation og opsætning
- Sensor tilslutning og kabling
- Læsning af temperatur og luftfugtighed
- Data validering og fejlhåndtering

### 💡 Lektion 5: LDR Lyssensor (Analog Input)
**Onsdag** | [Detaljeret plan](../Detaljerede-lektionsplaner/Lektion-05.md)
- Analog-til-digital konvertering (ADC)
- LDR karakteristika og kalibrering
- Voltage divider kredsløb
- Mapping af analog værdier

### 🌬️ Lektion 6: Gassensor Integration
**Fredag** | [Detaljeret plan](../Detaljerede-lektionsplaner/Lektion-06.md)
- MQ-2 gassensor opsætning
- Kalibrering og warm-up tid
- Threshold detection
- Kombination af multiple sensorer

---

## 📖 Læsemateriale
**Før uge 2:**
- [Sensor Grundlag](../../Laesemateriale/Sensorer/01-Sensor-Principper.md)
- [ADC på ESP32](../../Laesemateriale/ESP32-grundlag/03-Analog-Input.md)

**Under ugen:**
- [DHT22 Dokumentation](../../Laesemateriale/Sensorer/02-DHT22-Guide.md)
- [LDR og Fotoresistorer](../../Laesemateriale/Sensorer/03-LDR-og-Lyssensorer.md)
- [Gassensor Teknologier](../../Laesemateriale/Sensorer/04-Gassensor-Guide.md)

---

## 🎯 Aktiviteter og Øvelser

### 🏫 I Klassen
- **Sensor workshop**: Hands-on med alle tre sensortyper
- **Kabling øvelse**: Breadboard og forbindelser
- **Kalibrering session**: Praktisk sensor justering
- **Fejlfinding**: Debugging af sensor problemer

### 🏠 Hjemmeopgaver
1. **Kombiner sensorer**: Læs alle tre sensorer samtidigt
2. **Datalogning**: Gem målinger i serial output
3. **Kalibrering**: Test sensorer under forskellige forhold
4. **Eksperimenter**: Modificér sampling rates og intervals

---

## 🔧 Værktøjer og Komponenter
- **DHT22 sensor** og bibliotek
- **LDR** (fotoresistor) og modstand
- **MQ-2 gassensor**
- **Breadboard** og jumper wires
- **Multimeter** til måling

## 📊 Data Formatering
Introduktion til struktureret data output:
```
Timestamp,Temperature,Humidity,Light,Gas
12:34:56,23.5,65.2,456,87
```

---

## 🎯 Ugens Læringsmål
Efter uge 2 skal de studerende kunne:
- **Tilslutte** og konfigurere forskellige sensortyper
- **Læse** analog og digital sensor data
- **Validere** og behandle sensor input
- **Formatere** data til videre behandling
- **Kombinere** multiple sensorer i samme program

## 📈 Evaluering
- **Praktisk øvelse**: Alle sensorer fungerer korrekt (50%)
- **Dataformat**: Struktureret output med timestamps (25%)
- **Fejlhåndtering**: Robust kode med validering (25%)

---

## 🔗 Forbindelse til Næste Uge
Uge 3 introducerer:
- Seriel kommunikation til PC
- Python data modtagelse
- Real-time data streaming

---

## ⚠️ Almindelige Problemer
- **DHT22**: Kræver 2 sekunder mellem læsninger
- **LDR**: Husker voltage divider (10kΩ modstand anbefales)
- **Gassensor**: Kræver 24-48 timer warm-up tid for præcise målinger

## 📋 Kontrollér Funktionalitet
- [ ] DHT22 læser temperature og luftfugtighed
- [ ] LDR reagerer på lysændringer
- [ ] Gassensor giver konsistente værdier
- [ ] Data outputtes i struktureret format
- [ ] Fejlhåndtering implementeret

*Fokusér på at få alle sensorer til at fungere pålideligt - det er fundamentet for resten af kurset!*