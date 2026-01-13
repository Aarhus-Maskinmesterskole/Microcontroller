# 📥 **Læsning af data fra PLC med Python**

## 📌 **Formål**
I dette modul lærer du, hvordan du læser data fra en Siemens PLC ved hjælp af **Snap7** i Python.

---

## 🔗 **Trin 1: Opret forbindelse til PLC**
Opret en ny Python-fil (`read_plc.py`) og tilføj følgende kode:

```python
import snap7

# PLC-indstillinger
PLC_IP = "192.168.0.1"  # Ændr til din PLC's IP
RACK = 0  # Standard for S7-1200/1500
SLOT = 1  # Standard for S7-1200/1500

# Opret forbindelse
plc = snap7.client.Client()
plc.connect(PLC_IP, RACK, SLOT)

if plc.get_connected():
    print("Forbundet til PLC!")
else:
    print("Kunne ikke forbinde til PLC.")
```

Kør scriptet for at teste forbindelsen.

---

## 🗄 **Trin 2: Læs en datablock**
For at læse data fra PLC’ens **DB1**, brug følgende kode:

```python
from snap7.util import get_real, get_bool, get_int

DB_NUMBER = 1  # Datablock nummer
START_BYTE = 0  # Startadresse i datablock

# Læs data fra PLC
data = plc.db_read(DB_NUMBER, START_BYTE, 8)

# Dekod værdier
real_value = get_real(data, 0)  # Læser en REAL (4 bytes)
bool_value = get_bool(data, 4, 0)  # Læser en BOOL (bit 0 i byte 4)
int_value = get_int(data, 6)  # Læser en INT (2 bytes)

# Udskriv resultater
print(f"Real Value: {real_value}")
print(f"Bool Value: {bool_value}")
print(f"Int Value: {int_value}")

plc.disconnect()
```

---

## ⚠ **Fejlhåndtering**
Hvis du får en **timeout-fejl**, så:
1. Kontrollér, at din PLC er **tændt** og på det **samme netværk**.  
2. Sørg for, at **PUT/GET kommunikation** er aktiveret i TIA Portal.  
3. Prøv at pinge PLC’en:  

```sh
ping 192.168.0.1
```

---

## 🚀 **Næste trin**
✅ Du kan nu læse data fra PLC’en!  
Gå videre til næste modul: [📄 05-write-data.md](05-write-data.md) 📤
