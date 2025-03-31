# ⚠️ Fejlhåndtering og diagnosticering i ESP32 Modbus TCP

I dette modul lærer du at opdage og håndtere fejl under Modbus TCP-kommunikation. Dette er især vigtigt i industrielle netværk, hvor forbindelser kan være ustabile eller midlertidigt nede.

---

## 🔁 Typiske fejlscenarier
| Problem | Sandsynlig årsag | Løsning |
|--------|------------------|---------|
| Timeout ved `connect()` | Server svarer ikke | Tjek IP, serverstatus, port 502 åben? |
| `OSError: [Errno 113] EHOSTUNREACH` | Forkert IP eller ingen netforbindelse | Tjek WiFi og IP |
| Fejlagtigt Modbus-respons | Forkert unit ID, offset eller datatyper | Brug korrekt Modbus-specifikation |

---

## 🧱 Brug try/except til at fange fejl
```python
import socket
from umodbus_tcp import read_holding_registers

try:
    sock = socket.socket()
    sock.settimeout(3)  # max 3 sek. timeout
    sock.connect(('192.168.1.100', 502))

    values = read_holding_registers(sock, 1, 0, 2)
    print("Data:", values)

except Exception as e:
    print("Fejl under Modbus-læsning:", e)

finally:
    sock.close()
```

---

## 🧠 Tips til robusthed
- Brug `settimeout()` for at undgå hængende forbindelser
- Tilføj `finally:` til at sikre lukning af socket uanset fejl
- Log fejl i en lokal fil, hvis ESP32 har filsystem (fx med `open('log.txt', 'a')`)

---

## 🧪 Ekstra øvelse
Lav et script, der forsøger at forbinde til Modbus-server hvert 10. sekund, og logger fejltilstande uden at stoppe programmet:
```python
import time
while True:
    try:
        # forsøg på kommunikation her
        pass
    except Exception as e:
        print("Kommunikationsfejl:", e)
    time.sleep(10)
```

---

I næste og sidste modul `07-integration.md` integrerer vi det hele og opsamler Modbus-data til videre brug i Python på PC'en.


