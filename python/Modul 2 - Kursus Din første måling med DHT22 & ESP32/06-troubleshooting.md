# 🔄 Modul 2.6: Fejlfinding af DHT22 & ESP32

## 📌 **Introduktion**
Hvis du oplever problemer med at få **DHT22 til at virke med ESP32**, er der flere typiske fejlkilder. Dette modul hjælper dig med at **identificere og løse de mest almindelige fejl**.

🔗 **Forrige modul:** [05-first-measurement.md](05-first-measurement.md)  
🔜 **Næste modul:** [07-next-steps.md](07-next-steps.md)  

---

## ❌ **Problem 1: Ingen data vises / Sensor svarer ikke**
### 🔎 **Fejlbeskrivelse**
Når du kører koden, sker der ingenting, eller du ser kun:

```bash
Fejl ved aflæsning af DHT22: [OSError]
```

### 🛠 **Løsning**
1. **Tjek GPIO-forbindelserne**  
   - Sørg for, at **DATA**-pinden på DHT22 er korrekt forbundet til **GPIO4** (eller den GPIO, du har valgt).  
   - Hvis du er i tvivl, prøv en anden GPIO (fx **GPIO15**).  

2. **Tjek din pull-up modstand**  
   - Brug **en 10kΩ pull-up modstand** mellem **VCC og DATA**, hvis din DHT22 ikke har én indbygget.  

3. **Brug en anden spænding**  
   - DHT22 kan bruge **3.3V eller 5V**, men nogle modeller fungerer bedre med **5V**.  

4. **Genstart ESP32 og prøv igen**  
   - I Thonny, tryk `Ctrl+D` for at genstarte ESP32 og kør koden igen.  

---

## 🔄 **Problem 2: Temperatur- og fugtighedsdata er unormale**
### 🔎 **Fejlbeskrivelse**
DHT22 giver **for høje eller for lave værdier**, fx:     
```python
Temperatur: -40.0°C  Luftfugtighed: 0.0%
```
eller    
```python
Temperatur: 99.9°C  Luftfugtighed: 120.0%
```

---

### 🛠 **Løsning**
1. **Giv ESP32 mere tid mellem målinger**  
   - DHT22 kræver mindst **2 sekunder mellem målinger**. Hvis du laver målinger for hurtigt, kan du få fejl.  
   - Ret din kode, så du **sætter `time.sleep(2)` i loopet**:
     ```python
     time.sleep(2)  # Vent mindst 2 sekunder mellem målinger
     ```

2. **Sørg for stabil strømforsyning**  
   - Hvis ESP32 får ustabil strøm, kan sensoren give fejlværdier.  
   - Prøv at bruge **en ekstern 5V-strømkilde** til DHT22.

---

## 🚨 **Problem 3: ESP32 kan ikke finde DHT-biblioteket**
### 🔎 **Fejlbeskrivelse**
Når du kører koden, får du en fejl som:    
```python
ImportError: no module named 'dht'
```

### 🛠 **Løsning**
1. **Tjek, at biblioteket er installeret**  
   - Åbn **Thonny Shell**, og kør:
     ```python
     import dht
     ```
   - Hvis du får en fejl, skal du **geninstallere biblioteket**:
     ```python
     import upip
     upip.install("micropython-dht")
     ```
   - Eller upload `dht.py` manuelt (se [03-install-dht-library.md](03-install-dht-library.md)).

2. **Tjek, at filnavnet ikke er `dht.py`**  
   - Hvis du selv har lavet en fil ved navn `dht.py`, vil den konflikte med biblioteket.  
   - Omdøb din fil, fx til **`dht22_test.py`**, og prøv igen.

---

## 🏗 **Problem 4: ESP32 kan ikke findes i Thonny**
### 🔎 **Fejlbeskrivelse**
ESP32 vises ikke i Thonny, eller du får en fejl som:
```python
Cannot connect to COM3
```

### 🛠 **Løsning**
1. **Tjek, om CP210x eller CH340 driveren er installeret**  
   - Følg vejledningen i [02-install-drivers.md](02-install-drivers.md).  

2. **Find den rigtige COM-port**  
   - Windows: Åbn **Enhedshåndtering** (`Win + X → Enhedshåndtering`) og find **"USB-to-Serial"**.  
   - Mac/Linux: Kør i terminalen:
     ```bash
     ls /dev/ttyUSB*
     ```

3. **Tjek, om en anden process bruger ESP32**  
   - Hvis du bruger **Arduino IDE** eller et andet program, skal du lukke det, da det kan blokere forbindelsen.  

4. **Genstart ESP32**  
   - Tryk `Ctrl+D` i Thonny for at genstarte ESP32.  

---

## ✅ **Tjekliste: Er alt sat op korrekt?**
| ✅ **Test** | **Er det korrekt?** |
|------------|-----------------|
| **DHT22 er forbundet til ESP32 GPIO4** | 🔲 Ja / 🔲 Nej |
| **10kΩ pull-up modstand er tilsluttet (hvis nødvendig)** | 🔲 Ja / 🔲 Nej |
| **ESP32 har en stabil strømforsyning** | 🔲 Ja / 🔲 Nej |
| **DHT22 måles kun hvert 2. sekund** | 🔲 Ja / 🔲 Nej |
| **DHT-biblioteket er installeret korrekt** | 🔲 Ja / 🔲 Nej |
| **ESP32 kan forbindes til Thonny** | 🔲 Ja / 🔲 Nej |

✅ **Hvis du har sagt "Ja" til alt, burde din DHT22 nu virke!**  

---

## 🚀 **Næste skridt**
Har du fået DHT22 til at virke? Så er du klar til at **udvide projektet** med Wi-Fi, logging og web-dashboard!  

🔜 **Fortsæt til næste modul:**  
📄 **[07-next-steps.md](07-next-steps.md)**
