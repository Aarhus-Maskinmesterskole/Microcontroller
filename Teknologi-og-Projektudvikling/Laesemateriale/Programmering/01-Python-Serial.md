# 🐍 Python Serial Programming
**Python pySerial bibliotek til ESP32 kommunikation**

## 🎯 Introduktion
Python's pySerial bibliotek gør det nemt at etablere seriel kommunikation mellem din computer og ESP32. Dette er fundamentet for dataopsamling, real-time monitoring og bidirectional control.

## 📦 Installation og Setup

### pySerial Installation
```bash
# Via pip
pip install pyserial

# Via conda
conda install pyserial

# Verificér installation
python -c "import serial; print(serial.__version__)"
```

### Ekstra Pakker (Anbefalede)
```bash
pip install matplotlib  # For plotting
pip install pandas      # For data handling
pip install numpy       # For numerical operations
```

---

## 🔌 Basic Serial Connection

### 1. Port Detection
```python
import serial.tools.list_ports

def find_esp32_ports():
    """Find tilgængelige serielle porte"""
    ports = serial.tools.list_ports.comports()
    esp32_ports = []
    
    for port in ports:
        print(f"Port: {port.device}")
        print(f"Description: {port.description}")
        print(f"Hardware ID: {port.hwid}")
        print("---")
        
        # ESP32 har ofte disse beskrivelser
        if any(keyword in port.description.lower() for keyword in 
               ['cp210x', 'ch340', 'esp32', 'silicon labs']):
            esp32_ports.append(port.device)
    
    return esp32_ports

# Find ESP32 porte
available_ports = find_esp32_ports()
print(f"ESP32 porte fundet: {available_ports}")
```

### 2. Basic Connection
```python
import serial
import time

def connect_to_esp32(port, baudrate=115200, timeout=1):
    """Opret forbindelse til ESP32"""
    try:
        ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        
        # Vent på at forbindelsen stabiliseres
        time.sleep(2)
        
        print(f"Forbundet til {port} på {baudrate} baud")
        return ser
        
    except serial.SerialException as e:
        print(f"Fejl ved forbindelse: {e}")
        return None

# Eksempel på forbindelse
port = "COM3"  # Windows
# port = "/dev/ttyUSB0"  # Linux
# port = "/dev/cu.usbserial-0001"  # macOS

esp32 = connect_to_esp32(port)
```

---

## 📡 Data Modtagelse

### 1. Simpel Data Læsning
```python
def read_simple_data(serial_port):
    """Læs enkelt linje fra ESP32"""
    if serial_port.in_waiting > 0:
        line = serial_port.readline().decode('utf-8').strip()
        return line
    return None

# Eksempel på brug
while True:
    data = read_simple_data(esp32)
    if data:
        print(f"Modtaget: {data}")
    time.sleep(0.1)
```

### 2. Struktureret Data Parsing
```python
import json
from datetime import datetime

class ESP32DataParser:
    def __init__(self):
        self.data_buffer = []
    
    def parse_csv_data(self, line):
        """Parse CSV format: DATA,timestamp,temp,humid,light,gas"""
        try:
            parts = line.split(',')
            if parts[0] == "DATA" and len(parts) == 6:
                return {
                    'timestamp': int(parts[1]),
                    'temperature': float(parts[2]),
                    'humidity': float(parts[3]),
                    'light': int(parts[4]),
                    'gas': int(parts[5]),
                    'received_at': datetime.now()
                }
        except (ValueError, IndexError) as e:
            print(f"Parse fejl: {e}")
        return None
    
    def parse_json_data(self, line):
        """Parse JSON format"""
        try:
            return json.loads(line)
        except json.JSONDecodeError as e:
            print(f"JSON parse fejl: {e}")
            return None
    
    def process_line(self, line):
        """Process en linje baseret på format"""
        line = line.strip()
        
        if line.startswith("DATA,"):
            return self.parse_csv_data(line)
        elif line.startswith("{"):
            return self.parse_json_data(line)
        elif line.startswith("ERROR,"):
            print(f"ESP32 fejl: {line}")
        elif line == "ESP32,Ready,Start":
            print("ESP32 er klar!")
        
        return None

# Eksempel på brug
parser = ESP32DataParser()

while True:
    if esp32.in_waiting > 0:
        raw_line = esp32.readline().decode('utf-8')
        sensor_data = parser.process_line(raw_line)
        
        if sensor_data:
            print(f"Temperatur: {sensor_data['temperature']}°C")
            print(f"Luftfugtighed: {sensor_data['humidity']}%")
            print(f"Lys: {sensor_data['light']}")
            print(f"Gas: {sensor_data['gas']}")
            print("---")
```

---

## 📊 Real-time Data Logging

### 1. CSV Data Logger
```python
import csv
from datetime import datetime
import os

class DataLogger:
    def __init__(self, filename=None):
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"esp32_data_{timestamp}.csv"
        
        self.filename = filename
        self.fieldnames = ['timestamp', 'temperature', 'humidity', 'light', 'gas', 'received_at']
        
        # Opret CSV fil med headers
        self.init_csv_file()
    
    def init_csv_file(self):
        """Opret CSV fil med kolonnenavne"""
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
        print(f"Data logger oprettet: {self.filename}")
    
    def log_data(self, sensor_data):
        """Tilføj data til CSV fil"""
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow(sensor_data)

# Eksempel på brug
logger = DataLogger()

while True:
    if esp32.in_waiting > 0:
        raw_line = esp32.readline().decode('utf-8')
        sensor_data = parser.process_line(raw_line)
        
        if sensor_data:
            logger.log_data(sensor_data)
            print(f"Data gemt: {sensor_data['temperature']}°C")
```

### 2. Rolling File Logger
```python
import os
from datetime import datetime, timedelta

class RollingDataLogger:
    def __init__(self, max_file_size_mb=10, max_files=5):
        self.max_file_size = max_file_size_mb * 1024 * 1024  # Convert to bytes
        self.max_files = max_files
        self.current_file = None
        self.current_filename = None
        self.create_new_file()
    
    def create_new_file(self):
        """Opret ny log fil"""
        if self.current_file:
            self.current_file.close()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_filename = f"esp32_rolling_{timestamp}.csv"
        
        self.current_file = open(self.current_filename, 'w', newline='')
        writer = csv.DictWriter(self.current_file, fieldnames=['timestamp', 'temperature', 'humidity', 'light', 'gas'])
        writer.writeheader()
        
        self.cleanup_old_files()
        print(f"Ny log fil: {self.current_filename}")
    
    def cleanup_old_files(self):
        """Slet gamle log filer"""
        log_files = [f for f in os.listdir('.') if f.startswith('esp32_rolling_') and f.endswith('.csv')]
        log_files.sort()
        
        while len(log_files) > self.max_files:
            old_file = log_files.pop(0)
            os.remove(old_file)
            print(f"Slettet gammel log: {old_file}")
    
    def log_data(self, sensor_data):
        """Log data med automatisk fil rotation"""
        # Check om fil er for stor
        if os.path.getsize(self.current_filename) > self.max_file_size:
            self.create_new_file()
        
        writer = csv.DictWriter(self.current_file, fieldnames=['timestamp', 'temperature', 'humidity', 'light', 'gas'])
        writer.writerow(sensor_data)
        self.current_file.flush()  # Ensure data is written
```

---

## 🔄 Bidirectional Communication

### 1. Command Sending
```python
class ESP32Controller:
    def __init__(self, serial_port):
        self.serial = serial_port
        self.command_timeout = 5.0
    
    def send_command(self, command):
        """Send kommando til ESP32"""
        command_line = command + '\n'
        self.serial.write(command_line.encode('utf-8'))
        print(f"Sendt kommando: {command}")
    
    def send_command_with_response(self, command, timeout=None):
        """Send kommando og vent på svar"""
        if timeout is None:
            timeout = self.command_timeout
        
        # Ryd input buffer
        self.serial.reset_input_buffer()
        
        # Send kommando
        self.send_command(command)
        
        # Vent på svar
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.serial.in_waiting > 0:
                response = self.serial.readline().decode('utf-8').strip()
                return response
            time.sleep(0.01)
        
        return None  # Timeout
    
    def get_sensor_reading(self, sensor="ALL"):
        """Få specifik sensor læsning"""
        command = f"GET_{sensor}"
        response = self.send_command_with_response(command)
        
        if response and response.startswith("DATA,"):
            return parser.parse_csv_data(response)
        return None

# Eksempel på brug
controller = ESP32Controller(esp32)

# Få alle sensor data
all_data = controller.get_sensor_reading("ALL")
if all_data:
    print(f"Temperatur: {all_data['temperature']}°C")

# Få kun temperatur
temp_data = controller.get_sensor_reading("TEMP")
```

### 2. Interactive Control
```python
def interactive_mode(controller):
    """Interaktiv kommando mode"""
    print("ESP32 Interactive Mode")
    print("Kommandoer: GET_ALL, GET_TEMP, GET_HUMID, QUIT")
    
    while True:
        user_input = input("ESP32> ").strip().upper()
        
        if user_input == "QUIT":
            break
        elif user_input in ["GET_ALL", "GET_TEMP", "GET_HUMID"]:
            response = controller.send_command_with_response(user_input)
            if response:
                print(f"Svar: {response}")
            else:
                print("Ingen svar (timeout)")
        else:
            print("Ukendt kommando")

# Start interactive mode
interactive_mode(controller)
```

---

## 🛡️ Error Handling og Robusthed

### 1. Connection Management
```python
class RobustESP32Connection:
    def __init__(self, port, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        self.connected = False
        self.reconnect_attempts = 0
        self.max_reconnect_attempts = 5
    
    def connect(self):
        """Opret forbindelse med retry logic"""
        try:
            if self.serial and self.serial.is_open:
                self.serial.close()
            
            self.serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1
            )
            
            time.sleep(2)  # Stabilization time
            self.connected = True
            self.reconnect_attempts = 0
            print(f"Forbundet til {self.port}")
            return True
            
        except serial.SerialException as e:
            print(f"Forbindelsesfejl: {e}")
            self.connected = False
            return False
    
    def read_line_safe(self):
        """Sikker læsning med automatic reconnect"""
        if not self.connected:
            if self.reconnect_attempts < self.max_reconnect_attempts:
                print("Forsøger at genetablere forbindelse...")
                if self.connect():
                    self.reconnect_attempts = 0
                else:
                    self.reconnect_attempts += 1
                    time.sleep(2)
                return None
            else:
                print("Max reconnect attempts nået")
                return None
        
        try:
            if self.serial.in_waiting > 0:
                line = self.serial.readline().decode('utf-8').strip()
                return line
        except (serial.SerialException, UnicodeDecodeError) as e:
            print(f"Læsefejl: {e}")
            self.connected = False
        
        return None

# Eksempel på robust forbindelse
robust_esp32 = RobustESP32Connection("COM3")
robust_esp32.connect()

while True:
    data = robust_esp32.read_line_safe()
    if data:
        sensor_data = parser.process_line(data)
        if sensor_data:
            logger.log_data(sensor_data)
    time.sleep(0.1)
```

---

## 📈 Performance Monitoring

### 1. Data Rate Monitoring
```python
import time
from collections import deque

class PerformanceMonitor:
    def __init__(self, window_size=100):
        self.timestamps = deque(maxlen=window_size)
        self.packet_count = 0
        self.error_count = 0
        self.start_time = time.time()
    
    def record_packet(self, success=True):
        """Registrer modtaget pakke"""
        self.timestamps.append(time.time())
        self.packet_count += 1
        if not success:
            self.error_count += 1
    
    def get_packet_rate(self):
        """Beregn pakker per sekund"""
        if len(self.timestamps) < 2:
            return 0
        
        time_span = self.timestamps[-1] - self.timestamps[0]
        if time_span > 0:
            return len(self.timestamps) / time_span
        return 0
    
    def get_error_rate(self):
        """Beregn fejl procent"""
        if self.packet_count > 0:
            return (self.error_count / self.packet_count) * 100
        return 0
    
    def print_stats(self):
        """Print performance statistikker"""
        runtime = time.time() - self.start_time
        print(f"Runtime: {runtime:.1f}s")
        print(f"Total packets: {self.packet_count}")
        print(f"Packet rate: {self.get_packet_rate():.1f} pps")
        print(f"Error rate: {self.get_error_rate():.1f}%")

# Eksempel på brug
monitor = PerformanceMonitor()

while True:
    data = esp32_connection.read_line_safe()
    if data:
        sensor_data = parser.process_line(data)
        monitor.record_packet(sensor_data is not None)
        
        if monitor.packet_count % 50 == 0:
            monitor.print_stats()
```

---

## 🎯 Sammenfatning

Python's pySerial bibliotek giver kraftfulde værktøjer til:

- **Robust seriel kommunikation** med ESP32
- **Struktureret data parsing** og validation
- **Real-time data logging** og persistence
- **Bidirectional control** og kommando systemer
- **Error handling** og automatic recovery
- **Performance monitoring** og optimization

I de næste lektioner vil vi kombinere disse teknikker med matplotlib til real-time visualization og pandas til avanceret data analyse.

---

*Python og pySerial er jeres bridge mellem hardware og high-level data processing! 🐍*