# 🐳 Workshop: Filtrering af CSV-filer og Real-tids Plot fra ESP32

📡 En hands-on workshop, hvor du lærer at filtrere CSV-filer og skabe real-tids plots fra ESP32 serielle data. Denne workshop er skræddersyet til studerende, teknikere og hobbyfolk, der er interesseret i dataanalyse og visualisering i realtid.

---

## 🚀 Hvad du lærer i denne workshop

✔️ Opsætning af ESP32 til at sende serielle data i CSV-format  
✔️ Filtrering af CSV-data ved hjælp af Python  
✔️ Visualisering af real-tids data fra ESP32  
✔️ Brug af relevante Python-biblioteker (`pandas`, `matplotlib`, `serial`)  
✔️ Grundlæggende fejlfinding og optimering  
✔️ Glidende gennemsnit og medianfiltrering  
✔️ Fourier-analyse til frekvensanalyse  
✔️ Generering og tilføjelse af støj til datasæt  
✔️ Fjernelse af støj fra datasæt  

---

## 📚 Workshopindhold

| Modul                  | Emne                                                                 |
|------------------------|----------------------------------------------------------------------|
| 📁 00_introduktion/     | 🧰 Introduktion til ESP32, serielle data og CSV-format               |
| 📁 01_esp32_setup/      | ⚙️ Opsætning af ESP32 og udlæsning af serielle data i CSV-format     |
| 📁 02_csv_filtrering/   | 🐍 Filtrering af CSV-data med Python og pandas                       |
| 📁 03_realtime_plot/    | 📈 Real-tids plot af serielle data med matplotlib og pyserial        |
| 📁 04_projekt/          | 🧪 Kombiner filtrering og real-tids plot i et mini-projekt           |
| 📁 05_ekstra/           | ➕ Avancerede emner (valgfrit): f.eks. web-baseret visualisering     |
| 📁 06_signalfiltrering/ | ⚡️ Glidende gennemsnit, medianfiltrering og Fourier-analyse         |
| 📁 07_støjgenerering/   | 🎛️ Generering og tilføjelse af støj til datasæt                     |
| 📁 08_støjreduktion/    | 🧹 Fjernelse af støj med forskellige filtreringsteknikker            |

---

## 🔧 Krav før du starter

### 💻 Software

✅ Python 3.x installeret  
✅ pip (Python pakkehåndtering)  
✅ En teksteditor (f.eks. VS Code, Atom)  
✅ Thonny eller VS Code (til programmering af ESP32)

### 🔌 Hardware

✅ ESP32 udviklingsboard  
✅ USB-kabel til at forbinde ESP32 til computeren  
✅ *(Valgfrit)* Sensorer (f.eks. temperatur, fugtighed) til at generere data

---

## 🐍 Python-biblioteker

Installér følgende Python-biblioteker:

```bash
pip install pandas
pip install matplotlib
pip install pyserial
pip install numpy
