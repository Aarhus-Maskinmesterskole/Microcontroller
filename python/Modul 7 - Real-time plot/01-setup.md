# 🔧 **Modul 1: Installér nødvendige Python-biblioteker**

## 📌 **Forudsætninger**
✅ ESP32 er **allerede flashed med MicroPython**  
✅ **Thonny** er installeret og sat op til at forbinde til ESP32  
✅ **Python** er installeret på din PC  

---

## 📌 **1️⃣ Installér nødvendige Python-pakker**  
For at kunne **læse serielle data fra ESP32**, **gemme data** og **plotte målinger**, skal vi installere følgende Python-biblioteker:

```bash
pip install pyserial pandas matplotlib numpy
```

📌 **Beskrivelse af pakker:**  
| Pakke | Funktion |
|-------|----------|
| `pyserial` | Læser data fra ESP32 via USB (seriel kommunikation) |
| `pandas` | Håndterer og gemmer data i tabeller |
| `matplotlib` | Plotter data i grafer |
| `numpy` | Numeriske beregninger, bruges til dataanalyse |

✅ **Nu er alle pakker installeret!** 🎉  

---

## 📌 **2️⃣ Tjek om pakkerne er installeret**
For at sikre, at installationen lykkedes, kan vi tjekke versionerne:

```bash
python -c "import serial, pandas, matplotlib, numpy; print('Pakker installeret korrekt!')"
```

Hvis du ser beskeden **"Pakker installeret korrekt!"**, er alt sat op!  

✅ **Nu er dit Python-miljø klar til at kommunikere med ESP32!**  

🚀 **Fortsæt til næste modul: [02-esp32-serial.md](02-esp32-serial.md)**  
