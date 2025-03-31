# 🔌 ESP32 som Modbus TCP-klient i MicroPython

I dette modul sætter vi ESP32 op til at fungere som **Modbus TCP-klient**, der forbinder til en server over WiFi og læser/skriver holding registers.

---

## 📦 Installation af Modbus-bibliotek
Der findes flere uofficielle Modbus TCP-klientbiblioteker til MicroPython. Vi anbefaler fx `umodbus` eller en tilpasset version som understøtter TCP-klient.

### Eksempel: Installation via `mpremote`
```bash
mpremote connect COM5 fs cp umodbus_tcp.py :umodbus_tcp.py
```
> Brug evt. `wget` eller Thonny til at overføre filen, hvis du ikke bruger `mpremote`.

---

## 📡 Tilslut ESP32 til WiFi
Opret filen `wifi.py` og tilslut til dit netværk:
```python
import network
import time

ssid = 'INSERT_SSID'
password = 'INSERT_PASSWORD'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Tilslutter...")
    time.sleep(1)

print("Forbundet til:", wlan.ifconfig())
```

---

## 🧪 Første Modbus TCP-forespørgsel
Eksempel med `umodbus_tcp`:
```python
import socket
from umodbus_tcp import read_holding_registers

host = '192.168.1.100'  # IP på Modbus TCP-serveren
port = 502
unit_id = 1
start_address = 0
quantity = 2

sock = socket.socket()
sock.connect((host, port))

response = read_holding_registers(sock, unit_id, start_address, quantity)
print("Registerdata:", response)

sock.close()
```
> Husk at køre `wifi.py` først eller importere `connect_wifi()`-funktion før dette script.

---

## ✅ Bekræftelse
Når du ser en liste som fx `[123, 456]`, har du opnået forbindelse og læst data korrekt.

Hvis du får timeout eller fejl:
- Tjek at serveren kører og lytter på port 502
- IP er korrekt
- ESP32 er på samme netværk

---

I næste modul `04-modbus-server.md` sætter vi en Modbus TCP-server op på din PC til test og simulering.


