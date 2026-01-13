# 💻 C++ Workshop: Microcontroller-programmering

Velkommen til C++-delen af Microcontroller workshoppen! Her lærer du at programmere ESP32 med C++ og Arduino IDE.

---

## 🎯 Læringsmål

Efter denne workshop vil du kunne:

- 🔌 **GPIO-styring**: Læs og skriv til pins
- 🕹️ **Sensorintegration**: Tilslut og aflæs sensorer
- 🔄 **PWM & Motorstyring**: Styr servomotorer og LEDs
- 🌐 **WiFi & MQTT**: Forbind din ESP32 til internettet

---

## 📦 Hvad er ESP32?

ESP32 er en kraftfuld mikrocontroller med Wi-Fi og Bluetooth integration. Med C++ kan du programmere den direkte og få fuld kontrol over hardware-funktionerne.

---

## ⚙️ Kom godt i gang

1️⃣ **Download Arduino IDE**: https://www.arduino.cc/en/software

2️⃣ **Installer ESP32 board**: Følg vejledningen i Arduino IDE

3️⃣ **Tilslut din ESP32** og upload dit første program

---

## 🔧 Grundlæggende koncepter

### GPIO (General Purpose Input/Output)
```cpp
// Tænd LED på pin 2
pinMode(2, OUTPUT);
digitalWrite(2, HIGH);
```

### Analog læsning
```cpp
// Læs analog værdi fra pin A0
int sensorValue = analogRead(A0);
```

### PWM (Pulse Width Modulation)
```cpp
// Styr LED brightness
analogWrite(9, 128); // 50% brightness
```

---

## 🤝 Bidrag & Feedback

Har du forslag eller ønsker at bidrage? Opret en **issue** eller en **pull request**!

🚀 **God læring og happy coding!** 🎉