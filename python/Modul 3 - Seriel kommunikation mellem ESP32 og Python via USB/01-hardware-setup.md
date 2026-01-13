# 🔌 Modul 1: Tilslutning af ESP32 til PC

## 📌 **Introduktion**
For at kunne sende serielle data fra **ESP32 til Python**, skal vi sikre, at ESP32 er korrekt tilsluttet computeren via **USB**.

I dette modul sørger vi for, at din ESP32 er **forbundet og synlig for computeren**.

🔜 **Næste modul:** [02-serial-print-esp32.md](02-serial-print-esp32.md)  

---

## ✅ **Trin 1: Tilslut ESP32 med USB-kabel**
1. **Brug et USB-kabel, der understøtter data** (ikke kun opladning).  
2. **Sæt ESP32 i computeren via USB-porten**.  
3. **Tjek, om en LED på ESP32 lyser op** – det betyder, at den får strøm.  

---

## 🖥️ **Trin 2: Find ESP32’s serielle port**
### 🔹 **Windows**
1. Tryk **Win + X** → Vælg **Enhedshåndtering**  
2. Find **"Porte (COM & LPT)"**  
3. Kig efter en enhed som **"USB-to-Serial"**, **CP210x**, eller **CH340**  
4. Notér COM-portnummeret (fx `COM3` eller `COM4`).  

### 🍏 **Mac**
1. Åbn **Terminal** og skriv:  
   ```bash
   ls /dev/tty.*
   ```
2. Kig efter en enhed som `/dev/tty.SLAB_USBtoUART` (CP210x) eller `/dev/tty.wchusbserial` (CH340).  

### 🐧 **Linux**
1. Åbn **Terminal** og kør:  
   ```bash
   ls /dev/ttyUSB*
   ```
2. Hvis du ser `/dev/ttyUSB0` eller `/dev/ttyUSB1`, er din ESP32 forbundet.  

---

## 🔍 **Trin 3: Test forbindelse med Thonny**
1. **Åbn Thonny**  
2. Gå til **`Tools → Options → Interpreter`**  
3. **Vælg MicroPython (ESP32)**  
4. **Vælg den COM-port, du fandt før**  
5. Klik **OK**, og åbn **Shell-vinduet** nederst  
6. **Test forbindelsen ved at skrive:**
   ```python
   print("ESP32 er forbundet!")
   ```
7. Hvis `"ESP32 er forbundet!"` vises i Shell, er din ESP32 klar! ✅  

---

## 🛠 **Fejlfinding**
### ❌ **ESP32 vises ikke i enhedshåndtering / terminal**
- Prøv et **andet USB-kabel** (nogle kabler understøtter kun opladning).  
- Brug en **anden USB-port** på computeren.  
- Prøv at **genstarte computeren** og gentag Trin 2.  

### ❌ **Thonny kan ikke finde ESP32**
- **Tjek COM-porten igen** (se Trin 2).  
- **Luk Arduino IDE**, hvis det kører, da det kan blokere forbindelsen.  
- **Genstart ESP32** ved at tage USB-kablet ud og sætte det i igen.  

---

## ✅ **Hvad har vi opnået?**
✔️ ESP32 er forbundet til computeren  
✔️ Vi har fundet ESP32’s **serielle port**  
✔️ Vi har testet forbindelsen i **Thonny**  

🔜 **Fortsæt til næste modul:** [02-serial-print-esp32.md](02-serial-print-esp32.md), hvor vi lærer at sende serielle data fra ESP32 til computeren!  
