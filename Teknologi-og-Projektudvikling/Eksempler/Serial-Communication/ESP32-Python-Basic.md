# 💻 ESP32 Python Serial Communication Eksempel

## 📡 ESP32 Kode (Arduino IDE)

```cpp
/**
 * ESP32 Multi-Sensor Data Streamer
 * Sender struktureret sensor data til PC via USB serial
 * Understøtter kommandoer fra PC
 */

#include "DHT.h"

// Pin definitioner
#define DHT_PIN 4
#define DHT_TYPE DHT22
#define LDR_PIN A0
#define GAS_PIN A3
#define LED_PIN 2

// Sensor objekter
DHT dht(DHT_PIN, DHT_TYPE);

// Timing variabler
unsigned long lastSensorRead = 0;
const unsigned long SENSOR_INTERVAL = 5000; // 5 sekunder

// Data struktur
struct SensorData {
  float temperature;
  float humidity;
  int lightLevel;
  int gasLevel;
  unsigned long timestamp;
};

void setup() {
  // Initialiser seriel kommunikation
  Serial.begin(115200);
  
  // Initialiser sensorer
  dht.begin();
  pinMode(LED_PIN, OUTPUT);
  
  // Startup besked
  Serial.println("ESP32,Ready,Multi-Sensor");
  digitalWrite(LED_PIN, HIGH); // Indiker at systemet er klar
  delay(100);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  // Håndter indkommende kommandoer
  handleCommands();
  
  // Send sensor data med interval
  if (millis() - lastSensorRead >= SENSOR_INTERVAL) {
    sendSensorData();
    lastSensorRead = millis();
  }
  
  delay(10); // Lille pause for at undgå overload
}

void handleCommands() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    command.toUpperCase();
    
    if (command == "GET_ALL") {
      sendSensorData();
    } else if (command == "GET_TEMP") {
      sendTemperature();
    } else if (command == "GET_HUMID") {
      sendHumidity();
    } else if (command == "GET_LIGHT") {
      sendLight();
    } else if (command == "GET_GAS") {
      sendGas();
    } else if (command == "PING") {
      Serial.println("PONG");
    } else if (command == "LED_ON") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("ACK,LED_ON");
    } else if (command == "LED_OFF") {
      digitalWrite(LED_PIN, LOW);
      Serial.println("ACK,LED_OFF");
    } else if (command == "STATUS") {
      sendStatus();
    } else {
      Serial.println("ERROR,UNKNOWN_COMMAND," + command);
    }
  }
}

SensorData readSensors() {
  SensorData data;
  
  // Læs DHT22
  data.temperature = dht.readTemperature();
  data.humidity = dht.readHumidity();
  
  // Læs analog sensorer
  data.lightLevel = analogRead(LDR_PIN);
  data.gasLevel = analogRead(GAS_PIN);
  
  // Timestamp
  data.timestamp = millis();
  
  return data;
}

void sendSensorData() {
  SensorData data = readSensors();
  
  // Valider DHT22 data
  if (isnan(data.temperature) || isnan(data.humidity)) {
    Serial.println("ERROR,DHT22,READ_FAILED");
    return;
  }
  
  // Send som CSV format
  Serial.print("DATA,");
  Serial.print(data.timestamp);
  Serial.print(",");
  Serial.print(data.temperature, 1);
  Serial.print(",");
  Serial.print(data.humidity, 1);
  Serial.print(",");
  Serial.print(data.lightLevel);
  Serial.print(",");
  Serial.println(data.gasLevel);
}

void sendTemperature() {
  float temp = dht.readTemperature();
  if (isnan(temp)) {
    Serial.println("ERROR,DHT22,TEMP_READ_FAILED");
  } else {
    Serial.println("TEMP," + String(temp, 1));
  }
}

void sendHumidity() {
  float humid = dht.readHumidity();
  if (isnan(humid)) {
    Serial.println("ERROR,DHT22,HUMID_READ_FAILED");
  } else {
    Serial.println("HUMID," + String(humid, 1));
  }
}

void sendLight() {
  int light = analogRead(LDR_PIN);
  Serial.println("LIGHT," + String(light));
}

void sendGas() {
  int gas = analogRead(GAS_PIN);
  Serial.println("GAS," + String(gas));
}

void sendStatus() {
  unsigned long uptime = millis() / 1000;
  Serial.print("STATUS,ONLINE,");
  Serial.print("UPTIME,");
  Serial.print(uptime);
  Serial.print(",FREE_HEAP,");
  Serial.println(ESP.getFreeHeap());
}
```

---

## 🐍 Python Data Modtager

```python
#!/usr/bin/env python3
"""
ESP32 Serial Data Receiver
Modtager og behandler sensor data fra ESP32
Gemmer data i CSV format og viser real-time statistikker
"""

import serial
import serial.tools.list_ports
import csv
import time
import json
from datetime import datetime
from collections import deque
import threading
import queue

class ESP32DataReceiver:
    def __init__(self, port=None, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None
        self.is_connected = False
        self.data_queue = queue.Queue()
        self.running = False
        
        # Data storage
        self.csv_filename = f"esp32_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.init_csv_file()
        
        # Statistics
        self.packet_count = 0
        self.error_count = 0
        self.last_10_packets = deque(maxlen=10)
        
        # Auto-detect port if not provided
        if self.port is None:
            self.port = self.auto_detect_esp32()
    
    def auto_detect_esp32(self):
        """Automatisk detect ESP32 port"""
        ports = serial.tools.list_ports.comports()
        
        for port in ports:
            # ESP32 ofte har disse beskrivelser
            if any(keyword in port.description.lower() for keyword in 
                   ['cp210x', 'ch340', 'esp32', 'silicon labs']):
                print(f"ESP32 fundet på: {port.device}")
                return port.device
        
        # Hvis ikke fundet, vis tilgængelige porte
        print("ESP32 ikke auto-detekteret. Tilgængelige porte:")
        for port in ports:
            print(f"  {port.device}: {port.description}")
        
        return None
    
    def init_csv_file(self):
        """Initialiser CSV fil med headers"""
        with open(self.csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'esp32_time', 'temperature', 'humidity', 'light', 'gas']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print(f"CSV fil oprettet: {self.csv_filename}")
    
    def connect(self):
        """Opret forbindelse til ESP32"""
        if self.port is None:
            print("Ingen port specificeret")
            return False
        
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1
            )
            time.sleep(2)  # Vent på ESP32 restart
            self.is_connected = True
            print(f"Forbundet til ESP32 på {self.port}")
            return True
            
        except serial.SerialException as e:
            print(f"Forbindelsesfejl: {e}")
            return False
    
    def disconnect(self):
        """Afbryd forbindelse"""
        self.running = False
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
        self.is_connected = False
        print("Forbindelse afbrudt")
    
    def send_command(self, command):
        """Send kommando til ESP32"""
        if not self.is_connected:
            print("Ikke forbundet")
            return None
        
        try:
            self.serial_connection.write((command + '\n').encode())
            print(f"Sendt: {command}")
            
            # Vent på svar (timeout efter 3 sekunder)
            start_time = time.time()
            while time.time() - start_time < 3:
                if self.serial_connection.in_waiting > 0:
                    response = self.serial_connection.readline().decode().strip()
                    print(f"Svar: {response}")
                    return response
                time.sleep(0.01)
            
            print("Timeout - intet svar")
            return None
            
        except Exception as e:
            print(f"Kommando fejl: {e}")
            return None
    
    def parse_data_line(self, line):
        """Parse en data linje fra ESP32"""
        line = line.strip()
        
        try:
            if line.startswith("DATA,"):
                # Format: DATA,timestamp,temp,humid,light,gas
                parts = line.split(',')
                if len(parts) == 6:
                    return {
                        'timestamp': datetime.now().isoformat(),
                        'esp32_time': int(parts[1]),
                        'temperature': float(parts[2]),
                        'humidity': float(parts[3]),
                        'light': int(parts[4]),
                        'gas': int(parts[5])
                    }
            elif line.startswith("ERROR,"):
                print(f"ESP32 fejl: {line}")
                self.error_count += 1
            elif "Ready" in line:
                print(f"ESP32 status: {line}")
            
        except (ValueError, IndexError) as e:
            print(f"Parse fejl: {e} - Linje: {line}")
            self.error_count += 1
        
        return None
    
    def save_data(self, data):
        """Gem data til CSV fil"""
        with open(self.csv_filename, 'a', newline='') as csvfile:
            fieldnames = ['timestamp', 'esp32_time', 'temperature', 'humidity', 'light', 'gas']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)
    
    def process_data(self, data):
        """Behandl modtaget sensor data"""
        self.packet_count += 1
        self.last_10_packets.append(data)
        
        # Gem til fil
        self.save_data(data)
        
        # Print summary
        print(f"Pakke #{self.packet_count}")
        print(f"  Temp: {data['temperature']:.1f}°C")
        print(f"  Luftfugtighed: {data['humidity']:.1f}%")
        print(f"  Lys: {data['light']}")
        print(f"  Gas: {data['gas']}")
        print("---")
    
    def data_receiver_thread(self):
        """Thread til kontinuerlig data modtagelse"""
        print("Data modtager startet...")
        
        while self.running:
            try:
                if self.serial_connection.in_waiting > 0:
                    line = self.serial_connection.readline().decode().strip()
                    
                    if line:
                        data = self.parse_data_line(line)
                        if data:
                            self.process_data(data)
                
            except Exception as e:
                print(f"Modtager fejl: {e}")
                time.sleep(1)
            
            time.sleep(0.01)  # Lille pause
        
        print("Data modtager stoppet")
    
    def start_monitoring(self):
        """Start kontinuerlig monitoring"""
        if not self.is_connected:
            print("Skal være forbundet først")
            return
        
        self.running = True
        
        # Start data modtager thread
        receiver_thread = threading.Thread(target=self.data_receiver_thread)
        receiver_thread.daemon = True
        receiver_thread.start()
        
        print("Monitoring startet. Tryk Ctrl+C for at stoppe")
        try:
            while self.running:
                time.sleep(1)
                
                # Print statistikker hver 30. sekund
                if self.packet_count > 0 and self.packet_count % 6 == 0:
                    self.print_statistics()
                    
        except KeyboardInterrupt:
            print("\nStopper monitoring...")
            self.running = False
    
    def print_statistics(self):
        """Print data statistikker"""
        print("\n=== STATISTIKKER ===")
        print(f"Total pakker: {self.packet_count}")
        print(f"Fejl: {self.error_count}")
        
        if self.last_10_packets:
            recent_temps = [p['temperature'] for p in self.last_10_packets]
            recent_humids = [p['humidity'] for p in self.last_10_packets]
            
            print(f"Seneste 10 målinger:")
            print(f"  Temp: {min(recent_temps):.1f} - {max(recent_temps):.1f}°C (avg: {sum(recent_temps)/len(recent_temps):.1f})")
            print(f"  Luftfugtighed: {min(recent_humids):.1f} - {max(recent_humids):.1f}% (avg: {sum(recent_humids)/len(recent_humids):.1f})")
        
        print("===================\n")

def interactive_mode(receiver):
    """Interaktiv kommando mode"""
    print("\n=== INTERAKTIV MODE ===")
    print("Kommandoer:")
    print("  get_all    - Få alle sensor data")
    print("  get_temp   - Få kun temperatur")
    print("  ping       - Test forbindelse")
    print("  led_on     - Tænd LED")
    print("  led_off    - Sluk LED")
    print("  status     - ESP32 status")
    print("  monitor    - Start kontinuerlig monitoring")
    print("  quit       - Afslut")
    print("========================\n")
    
    while True:
        command = input("ESP32> ").strip().lower()
        
        if command == "quit":
            break
        elif command == "monitor":
            receiver.start_monitoring()
            break
        elif command in ["get_all", "get_temp", "ping", "led_on", "led_off", "status"]:
            receiver.send_command(command.upper())
        else:
            print("Ukendt kommando")

def main():
    """Main function"""
    print("ESP32 Serial Data Receiver")
    print("=========================")
    
    # Opret receiver (auto-detect port)
    receiver = ESP32DataReceiver()
    
    # Manuel port specification hvis nødvendigt
    if receiver.port is None:
        port = input("Indtast COM port (f.eks. COM3): ").strip()
        receiver.port = port
    
    # Forbind
    if not receiver.connect():
        print("Kunne ikke forbinde. Afslutter.")
        return
    
    # Test forbindelse
    print("Tester forbindelse...")
    response = receiver.send_command("PING")
    if response != "PONG":
        print("Advarsel: Uventet svar på PING")
    
    try:
        # Start interactive mode
        interactive_mode(receiver)
        
    finally:
        receiver.disconnect()

if __name__ == "__main__":
    main()
```

---

## 📋 Sådan Bruger Du Eksemplet

### 1. ESP32 Setup
1. **Upload** ESP32 koden til din ESP32
2. **Tilslut** sensorer:
   - DHT22 til pin 4
   - LDR til A0 (med 10kΩ pull-down)
   - Gas sensor til A3
3. **Forbind** ESP32 til PC via USB

### 2. Python Setup
```bash
# Installer nødvendige pakker
pip install pyserial

# Kør programmet
python esp32_receiver.py
```

### 3. Test Kommandoer
```
ESP32> ping          # Test forbindelse
ESP32> get_all       # Få alle sensor data
ESP32> led_on        # Tænd LED
ESP32> monitor       # Start kontinuerlig monitoring
```

---

## 📊 Data Output Format

### CSV Fil (esp32_data_YYYYMMDD_HHMMSS.csv)
```csv
timestamp,esp32_time,temperature,humidity,light,gas
2024-01-15T14:30:15.123456,15234,23.5,65.2,456,87
2024-01-15T14:30:20.456789,20456,23.6,65.1,458,89
```

### Console Output
```
ESP32 fundet på: COM3
CSV fil oprettet: esp32_data_20240115_143015.csv
Forbundet til ESP32 på COM3
Tester forbindelse...
Sendt: PING
Svar: PONG

Pakke #1
  Temp: 23.5°C
  Luftfugtighed: 65.2%
  Lys: 456
  Gas: 87
---
```

---

## 🔧 Customization Muligheder

### Tilføj Flere Sensorer
```cpp
// I ESP32 koden - tilføj nye pins
#define PRESSURE_PIN A1

// I readSensors() function
data.pressure = analogRead(PRESSURE_PIN);

// I sendSensorData()
Serial.print(data.pressure);
```

### Ændr Data Format til JSON
```cpp
// I sendSensorData() - erstat CSV med JSON
Serial.print("{\"temp\":");
Serial.print(data.temperature);
Serial.print(",\"humid\":");
Serial.print(data.humidity);
Serial.println("}");
```

### Tilføj Data Filtering
```python
# I Python koden - tilføj data validation
def validate_data(data):
    if data['temperature'] < -40 or data['temperature'] > 85:
        return False
    if data['humidity'] < 0 or data['humidity'] > 100:
        return False
    return True
```

---

Dette eksempel giver en komplet foundation for ESP32-PC kommunikation og kan nemt udvides med yderligere funktionalitet! 🚀