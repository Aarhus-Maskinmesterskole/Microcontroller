# ⚠️ **Fejlhåndtering og troubleshooting**

## 📌 **Formål**
I dette modul lærer du, hvordan du **diagnosticerer og løser fejl**, når du kommunikerer mellem Python og Siemens PLC.

---

## 🔍 **1️⃣ Tjek netværksforbindelsen**
Før du fejlretter Snap7, skal du sikre, at din computer kan kommunikere med PLC’en.

### **Test med ping**
Åbn en terminal eller kommandoprompt og kør:

```sh
ping 192.168.0.1
```

Hvis du ikke får svar:
- Kontroller, at PLC’en er **tændt** og forbundet til netværket.
- Tjek netværksopsætningen i **TIA Portal**.

---

## 🔄 **2️⃣ Verificer Snap7-forbindelsen**
Test forbindelsen til PLC’en fra Python:

```python
import snap7

plc = snap7.client.Client()
plc.connect("192.168.0.1", 0, 1)

if plc.get_connected():
    print("Forbundet til PLC!")
else:
    print("Kunne ikke forbinde til PLC.")

plc.disconnect()
```

Hvis forbindelsen fejler:
- Sørg for, at IP-adressen er korrekt.
- Tjek, om **PUT/GET kommunikation** er aktiveret i **TIA Portal**.

---

## 🛠 **3️⃣ Almindelige Snap7-fejl og løsninger**

| **Fejlmeddelelse** | **Mulig årsag** | **Løsning** |
|---------------------|----------------|-------------|
| `Connection refused` | PLC IP forkert eller offline | Tjek IP-adressen og ping PLC'en |
| `Timed out` | Firewalls eller netværksproblemer | Deaktiver firewall midlertidigt og test igen |
| `snap7.snap7exceptions.Snap7Exception` | PUT/GET ikke aktiveret | Aktivér "Permit access with PUT/GET communication" i TIA Portal |
| `ModuleNotFoundError: No module named 'snap7'` | Snap7 ikke installeret | Kør `pip install python-snap7` |
| `AttributeError: 'NoneType' object has no attribute 'db_read'` | Ingen forbindelse til PLC | Tjek forbindelsen med `plc.get_connected()` |

---

## 🚀 **Næste trin**
✅ Du kan nu fejlfinde og optimere din PLC-kommunikation! 🎯  

Dette er det sidste modul i workshoppen. Hvis du vil udvide dit projekt, kan du:
- **Integrere Python og en database** til logning af PLC-data.  
- **Bruge Flask eller FastAPI** til at bygge et webinterface for PLC-styring.  
- **Udvide til MQTT eller OPC UA** for IoT-integration.  

Tak for at have deltaget i workshoppen! 🚀  
