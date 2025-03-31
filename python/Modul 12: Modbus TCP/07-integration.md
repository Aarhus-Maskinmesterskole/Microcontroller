# 🔗 Integration af Modbus-data i Python på PC

I dette afsluttende modul samler vi hele forløbet: Vi henter Modbus TCP-data fra en ESP32-server (eller en anden Modbus-server), og bruger en Python-klient på PC’en til at analysere og visualisere data.

---

## 🧭 Hvad skal vi opnå?
- Hente data fra Modbus TCP-server via PC (ESP32 som server eller anden Modbus TCP-server)
- Gemme og analysere data
- Visualisere med matplotlib

---

## 📦 Installation af pymodbus og matplotlib
På din PC:
```bash
pip install pymodbus matplotlib
```

---

## 🖥️ Python-klient til læsning fra Modbus TCP-server
```python
from pymodbus.client.sync import ModbusTcpClient
import matplotlib.pyplot as plt
import time

client = ModbusTcpClient('192.168.1.123')  # IP på ESP32 eller anden server
client.connect()

x_vals = []
y_vals = []

for i in range(50):
    rr = client.read_holding_registers(0, 1, unit=1)
    if rr.isError():
        print("Fejl i læsning")
    else:
        y = rr.registers[0]
        y_vals.append(y)
        x_vals.append(i)
    time.sleep(1)

client.close()

plt.plot(x_vals, y_vals)
plt.xlabel("Tid (s)")
plt.ylabel("Sensorværdi")
plt.title("Modbus data fra ESP32")
plt.grid()
plt.show()
```

---

## 🧪 Ekstra idéer
- Kombiner med pandas og gem som CSV
- Brug sensor på ESP32 og send live-værdier
- Kombiner Modbus-data med anden datakilde (fx HTTP, MQTT, filinput)

---

Tillykke! Du har nu lavet et fuldt funktionelt system hvor:
- ESP32 er Modbus TCP-klient
- PC’en simulerer Modbus TCP-server (eller omvendt)
- Data kan visualiseres og analyseres i Python

🎉 Du er klar til at tage dine ESP32-projekter til industriel standard!
