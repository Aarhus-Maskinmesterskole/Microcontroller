# 🖥️ Opsætning af Modbus TCP-server til test

I dette modul sætter vi en Modbus TCP-server op på din PC, så du kan teste ESP32’s forespørgsler uden en fysisk PLC.

---

## 🛠️ Metode 1: Brug af `pymodbus` i Python
`pymodbus` kan bruges til at simulere en Modbus TCP-server.

### 📦 Installation
```bash
pip install pymodbus
```

### 📄 Eksempel: Enkel server med holding registers
```python
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [100, 200, 300, 400])
)
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'ESP32 Test'
identity.ProductCode = 'ESP32'
identity.VendorUrl = 'https://micropython.org'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'ModSim'
identity.MajorMinorRevision = '1.0'

StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))
```
> Serveren lytter nu på port 502 og har holding registers 0-3 sat til [100, 200, 300, 400].

---

## 🖥️ Metode 2: Brug af ModbusPal (GUI)
Hvis du foretrækker en grafisk grænseflade, kan du bruge **[ModbusPal](https://sourceforge.net/projects/modbuspal/)** (Java).

1. Download og kør ModbusPal
2. Tilføj en slave med Unit ID = 1
3. Tilføj holding registers og giv dem værdier
4. Start serveren

---

## ✅ Test fra PC (valgfrit)
Du kan teste din Modbus-server med fx **QModMaster** eller `pymodbus` klientkode:
```python
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('localhost')
client.connect()

rr = client.read_holding_registers(0, 4, unit=1)
print(rr.registers)
client.close()
```

---

Nu har du en funktionel Modbus TCP-server klar til test!
I næste modul `05-data-read-write.md` udvider vi ESP32-koden til at læse *og* skrive Modbus-data.

