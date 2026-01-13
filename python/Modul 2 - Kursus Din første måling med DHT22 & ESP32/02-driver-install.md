# 🔌 Modul 2.1: Installation af CP210x / CH340 USB-Seriel Drivere

## 📌 **Hvorfor skal du installere en driver?**
ESP32 bruger en USB-til-seriel chip til at kommunikere med din computer. De mest almindelige chips er:

- **CP210x** (Silicon Labs)  
- **CH340** (WCH)  

Hvis din ESP32 ikke vises som en **COM-port (Windows)** eller **/dev/ttyUSB0 (Mac/Linux)**, skal du installere den korrekte driver.

---

## 💾 **Trin 1: Identificer din driver**
1. **Slut din ESP32 til computeren via USB**.  
2. **Åbn Enhedshåndtering (Windows) eller Terminal (Mac/Linux)**.  
3. **Find din ESP32-port:**  

### 🖥️ **Windows**
- Tryk **Win + X → Enhedshåndtering**  
- Gå til **"Porte (COM & LPT)"**  
- Hvis du ser **CP210x** eller **CH340**, er driveren allerede installeret!  
- Hvis du ser **"Ukendt enhed"**, skal du installere en driver.

### 🍏 **Mac**
- Åbn **Terminal** og skriv:
  ```bash
  ls /dev/tty.*
  ```

  - Hvis du ser /dev/tty.SLAB_USBtoUART → Brug CP210x driver
  - Hvis du ser /dev/tty.wchusbserial → Brug CH340 driver

## 🐧 Linux
1. Trin 1: Åbn Terminal og kør:
```bash
ls /dev/ttyUSB*
```
Hvis du ser /dev/ttyUSB0, /dev/ttyUSB1, osv. → Driveren er sandsynligvis installeret.

## 📥 Trin 2: Download og installer driveren
### 🔵 CP210x Driver (Silicon Labs)
1. Download driveren:
    - 🔗 https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

2. Installer driveren:
    - Windows: Kør .exe-installationsfilen.
    - Mac: Kør .dmg-filen og følg vejledningen.
    - Linux: Kør: sudo apt install cp210x-dkms

### 🟢 CH340 Driver (WCH)
1. Download driveren:
    - 🔗 https://www.wch.cn/downloads/category/30.html

2. Installer driveren:
    - Windows: Kør .exe-installationsfilen.
    - Mac: Kør .pkg-filen og følg vejledningen.
    - Linux: Driveren er ofte inkluderet, men hvis ikke, kør:

```bash
sudo modprobe ch341
```

## ✅ Trin 3: Bekræft installationen
Efter installation, genstart computeren, og tjek igen i Enhedshåndtering (Windows) eller Terminal (Mac/Linux).
- Windows: Din ESP32 skal nu vises som COM3, COM4, osv.
- Mac: Din ESP32 skal nu vises som /dev/tty.SLAB_USBtoUART (CP210x) eller /dev/tty.wchusbserial (CH340).
- Linux: Din ESP32 skal nu vises som /dev/ttyUSB0 eller /dev/ttyUSB1.

## 🔗 Fortsæt nu til opsætningen af MicroPython:
📄 [micropython-setup](03-micropython-setup.md)
