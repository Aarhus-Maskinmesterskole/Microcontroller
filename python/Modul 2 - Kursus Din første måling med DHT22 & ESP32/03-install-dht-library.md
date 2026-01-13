# 💾 Modul 2.3: Installation af DHT22-biblioteket

## 📌 **Introduktion**
For at kunne læse temperatur og luftfugtighed fra **DHT22**-sensoren, skal vi installere et MicroPython-bibliotek, der håndterer kommunikationen med sensoren.

🔗 **Forrige modul:** [02-install-drivers.md](02-install-drivers.md)  
🔜 **Næste modul:** [04-first-measurement.md](04-first-measurement.md)  

---

## 📥 **Trin 1: Tilslut ESP32 til Thonny**
1. **Tilslut ESP32 via USB**  
2. **Åbn Thonny**  
3. **Vælg MicroPython (ESP32)** som interpreter (`Tools → Options → Interpreter`)  
4. **Vælg korrekt COM-port** (fx `COM3` på Windows, `/dev/ttyUSB0` på Linux/Mac)  
5. **Tjek at ESP32 svarer** ved at skrive:
   ```python
   print("ESP32 er forbundet!")
   ```
Hvis du får output i Shell, er du klar til næste trin. ✅

---

## 📦 Trin 2: Installer DHT22-biblioteket
MicroPython har et DHT-bibliotek, som vi kan installere via upip, en simpel pakkehåndtering for MicroPython.
1. I Thonny’s Shell (nederste vindue), kør:
   ```python
   import upip
   upip.install("micropython-dht")
   ```
2. Vent på installationen (kan tage et øjeblik afhængigt af din netværksforbindelse).
💡 Tip: Hvis upip ikke virker, kan du prøve en manuel installation (se næste trin).

---

## 🖥️ Alternativ: Manuel installation af DHT22-biblioteket
Hvis din ESP32 ikke har internetadgang, kan du downloade biblioteket manuelt og uploade det via Thonny.

### 📂 Trin 1: Download DHT22-biblioteket
1. Gå til GitHub-repositoriet: 🔗 https://github.com/micropython/micropython-lib
2. Find dht.py
3. Download dht.py til din computer

## 📡 Trin 2: Upload filen til ESP32
1. Åbn Thonny
2. Gå til "Files" (Filer) → Open / Upload to /esp"
3. Upload dht.py til ESP32's flash-hukommelse
4. Bekræft upload ved at skrive i Shell:
   ```python
   import dht
   print("DHT22-biblioteket er nu tilgængeligt!")
   ```
✅ Hvis du ser beskeden "DHT22-biblioteket er nu tilgængeligt!", er alt sat op korrekt!

---

## 📌 Tjek at biblioteket virker
For at teste, at biblioteket er installeret korrekt, kan du køre følgende:
```python
import dht
import machine

dht_pin = machine.Pin(4)
sensor = dht.DHT22(dht_pin)

sensor.measure()
print(f"Temperatur: {sensor.temperature()}°C")
print(f"Luftfugtighed: {sensor.humidity()}%")
```
💡 Hvis du får output uden fejl, er biblioteket installeret korrekt!

---

## 🚀 Næste skridt
Vi er nu klar til at måle temperatur og luftfugtighed med DHT22!    
🔜 Fortsæt til næste modul:    
📄 [04-first-measurement](04-first-measurement.md)
