# 🔄 Modul 4: Fejlfinding af seriel kommunikation mellem ESP32 og Python

## 📌 **Introduktion**
Hvis din **ESP32 ikke sender data korrekt** til din computer, eller hvis **Python ikke kan læse dataene**, er her nogle **typiske fejl og løsninger**.

🔗 **Forrige modul:** [03-python-read-serial.md](03-python-read-serial.md)  
🔜 **Næste modul:** [05-next-steps.md](05-next-steps.md)  

---

## ❌ **Problem 1: ESP32 vises ikke i enhedshåndtering / terminal**
### 🔎 **Fejlbeskrivelse**
ESP32 vises ikke i **Windows Enhedshåndtering**, **Mac Terminal** eller **Linux Terminal**, når du tjekker for serielle porte.

### 🛠 **Løsning**
1. **Tjek, om ESP32 lyser op, når du sætter USB-kablet i.**  
2. **Brug et andet USB-kabel** (nogle kabler understøtter kun opladning, ikke data).  
3. **Prøv en anden USB-port** på din computer.  
4. **Genstart computeren** og prøv igen.  

---

## ❌ **Problem 2: Python kan ikke finde ESP32’s serielle port**
### 🔎 **Fejlbeskrivelse**
Når du kører Python-scriptet (`esp32_serial_read.py`), får du en fejl som:
```
serial.serialutil.SerialException: could not open port 'COM3': FileNotFoundError(2, 'The system cannot find the file specified.')
```

### 🛠 **Løsning**
1. **Find den rigtige COM-port**:
   - **Windows:** Åbn **Enhedshåndtering** (`Win + X → Enhedshåndtering`) og tjek "Porte (COM & LPT)".  
   - **Mac/Linux:** Kør:
     ```bash
     ls /dev/tty.*
     ```
     eller
     ```bash
     ls /dev/ttyUSB*
     ```
2. **Opdater din Python-kode** med den korrekte port (fx `"COM4"`, `"/dev/ttyUSB0"`).  

---

## ❌ **Problem 3: Ingen data vises i Python**
### 🔎 **Fejlbeskrivelse**
Python-scriptet kører uden fejl, men der vises ingen data i terminalen.

### 🛠 **Løsning**
1. **Sørg for, at ESP32 rent faktisk sender data**:  
   - Åbn **Thonny**, og kør:
     ```python
     print("ESP32 test")
     ```
   - Hvis du ikke ser `"ESP32 test"` i Shell, er der et problem med din ESP32-forbindelse.  

2. **Tjek baud rate i Python-koden**:  
   - Hvis ESP32 sender data ved **115200 baud**, skal Python læse ved samme hastighed:
     ```python
     ser = serial.Serial("COM3", 115200, timeout=1)
     ```

3. **Prøv at genstarte ESP32**:  
   - Afbryd og tilslut ESP32 igen.  
   - Hvis den stadig ikke sender data, prøv:
     ```python
     import machine
     machine.reset()
     ```

---

## ❌ **Problem 4: Data fra ESP32 er ulæselige eller har fejl**
### 🔎 **Fejlbeskrivelse**
Python viser mærkelige tegn i stedet for måledata:
```
ÿÿÿÿÿÿTEMP:22.5C HUM:50.1%
```
Eller ESP32 sender data i ét langt stykke uden linjeskift.

### 🛠 **Løsning**
1. **Tjek, at du bruger `print()` korrekt**:  
   - Sørg for, at ESP32 sender data med et linjeskift (`\n`):
     ```python
     print(f"TEMP:{temp:.1f}C HUM:{hum:.1f}%")
     ```

2. **Tjek baud rate**:  
   - ESP32 og Python skal have **samme baud rate** (`115200` anbefales).  
   - Opdater din Python-kode, hvis baud rate er forkert.  

---

## ✅ **Tjekliste: Er alt sat op korrekt?**
| ✅ **Test** | **Er det korrekt?** |
|------------|-----------------|
| **ESP32 lyser op ved tilslutning** | 🔲 Ja / 🔲 Nej |
| **ESP32 vises som en COM-port i Enhedshåndtering / Terminal** | 🔲 Ja / 🔲 Nej |
| **Baud rate er sat til 115200 i både ESP32 og Python** | 🔲 Ja / 🔲 Nej |
| **Python har den rigtige COM-port** | 🔲 Ja / 🔲 Nej |
| **ESP32 sender data i Thonny Shell** | 🔲 Ja / 🔲 Nej |

✅ **Hvis du har sagt "Ja" til alt, burde din ESP32 nu virke!**  

---

## 🚀 **Næste skridt**
Har du fået ESP32 til at virke? Så er du klar til at **udvide projektet** med **logging, cloud-integration eller real-time visualisering**!  

🔜 **Fortsæt til næste modul:** [05-next-steps.md](05-next-steps.md), hvor vi udforsker videreudvikling af dit projekt!  
