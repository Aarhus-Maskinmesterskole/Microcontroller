# 📝 Modul 2: ESP32 sender serielle data via `print()`

## 📌 **Introduktion**
Nu hvor vi har ESP32 forbundet til computeren, skal vi sende data via **USB-seriel kommunikation**.

Vi bruger `print()` til at sende tekst og måledata fra ESP32 til computeren.

🔗 **Forrige modul:** [01-hardware-setup.md](01-hardware-setup.md)  
🔜 **Næste modul:** [03-python-read-serial.md](03-python-read-serial.md)  

---

## ✅ **Trin 1: Opret en simpel seriel test**
1. **Åbn Thonny**  
2. **Opret en ny fil (`File → New`)**  
3. **Indsæt følgende kode:**
   ```python
   import time

   while True:
       print("Hello from ESP32!")
       time.sleep(1)  # Vent 1 sekund
   ```
4. **Gem filen som `serial_test.py`**  
5. **Klik "Run" (▶️) eller tryk F5**  

🔹 **Forventet output i Thonny Shell:**  
```
Hello from ESP32!
Hello from ESP32!
Hello from ESP32!
...
```

💡 **Tip:** Hvis du ikke ser noget, tjek at du har valgt den rigtige **COM-port** (`Tools → Options → Interpreter → Port`).  

---

## 📊 **Trin 2: Send måledata fra ESP32**
Lad os sende temperatur- og fugtighedsdata i stedet.

1. **Tilslut en DHT22-sensor til ESP32** (`VCC → 3.3V, GND → GND, DATA → GPIO4`)  
2. **Erstat din kode med dette:**
   ```python
   import machine
   import dht
   import time

   sensor = dht.DHT22(machine.Pin(4))  # DHT22 på GPIO4

   while True:
       sensor.measure()
       temp = sensor.temperature()
       hum = sensor.humidity()

       print(f"TEMP:{temp:.1f}C HUM:{hum:.1f}%")  # Send data serielt
       time.sleep(2)
   ```
3. **Kør koden** (`F5` i Thonny).  

I **Shell** vil du nu se data som:
```
TEMP:22.5C HUM:50.1%
TEMP:22.6C HUM:49.8%
TEMP:22.5C HUM:50.0%
```

✅ **ESP32 sender nu måledata via USB-seriel!**  

🔜 **Fortsæt til næste modul:** [03-python-read-serial.md](03-python-read-serial.md), hvor vi lærer at læse serielle data i Python.
