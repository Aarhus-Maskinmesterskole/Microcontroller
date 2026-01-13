# 📤 **Skrivning af data til PLC med Python**

## 📌 **Formål**
I dette modul lærer du, hvordan du **skriver data** til en Siemens PLC ved hjælp af **Snap7** i Python.

---

## 🔗 **Trin 1: Opret forbindelse til PLC**
Sørg for, at din PLC er konfigureret korrekt, og brug følgende kode for at oprette forbindelse:

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

---

## 🗄 **Trin 2: Skriv data til datablock**
For at skrive data til **DB1** i PLC’en, brug følgende kode:

```python
from snap7.util import set_real, set_bool, set_int

DB_NUMBER = 1  # Datablock nummer

# Opret en bytearray til datablock
data = bytearray(10)

# Sæt værdier
set_real(data, 0, 75.32)  # REAL (4 bytes)
set_bool(data, 4, 0, True)  # BOOL (bit 0 i byte 4)
set_int(data, 6, 456)  # INT (2 bytes)

# Skriv data til PLC
plc.db_write(DB_NUMBER, 0, data)

print("Data skrevet til PLC!")

plc.disconnect()
```

---

## ✅ **Test din kode**
Efter at have kørt scriptet, skal du kunne se de nye værdier i **TIA Portal** under "Online & Diagnostics".

---

## ⚠ **Fejlhåndtering**
Hvis du oplever problemer:
1. Sørg for, at **PUT/GET kommunikation** er aktiveret i TIA Portal.  
2. Kontrollér, at datablocken **ikke er optimeret** i TIA Portal.  
3. Brug `plc.get_connected()` for at verificere forbindelsen.  
4. Tjek PLC’ens IP-adresse og netværksindstillinger.  

---

## 🚀 **Næste trin**
✅ Du kan nu skrive data til PLC’en!  
Gå videre til næste modul: [📄 06-realtime-plot.md](06-realtime-plot.md) 📊
