# 🔁 Læs og skriv Modbus-data med ESP32

I dette modul udvider vi ESP32-scripts til at læse *og* skrive holding registers via Modbus TCP.

---

## 📖 Læsning af holding registers
Her er en gentagelse og udbygning af tidligere læseforespørgsel:
```python
import socket
from umodbus_tcp import read_holding_registers

host = '192.168.1.100'  # IP på Modbus-serveren
sock = socket.socket()
sock.connect((host, 502))

response = read_holding_registers(sock, unit_id=1, address=0, count=2)
print("Læste værdier:", response)

sock.close()
```
> `address=0, count=2` henter register 0 og 1 (fx `[10, 20]`)

---

## ✍️ Skriv til holding registers
Følgende eksempel sender værdien `123` til holding register 0:
```python
from umodbus_tcp import write_single_register

sock = socket.socket()
sock.connect((host, 502))

result = write_single_register(sock, unit_id=1, address=0, value=123)
print("Skriveresultat:", result)

sock.close()
```
> Husk at din Modbus-server skal tillade skrivning.

---

## 🧠 Brug i kombination
Vil du først skrive og derefter læse:
```python
write_single_register(sock, 1, 0, 99)
values = read_holding_registers(sock, 1, 0, 2)
print("Efter skrivning:", values)
```

---

## 🧪 Testidéer
- Skriv en værdi til register 1 og vis ændringen i ModbusPal
- Lav en loop, hvor ESP32 ændrer et setpunkt hvert 5. sekund
- Brug data fra en sensor på ESP32 som input til Modbus write

---

I næste modul `06-error-handling.md` lærer vi at fange og logge netværksfejl og Modbus timeouts.
