# 🎬 Introduktion til PLC-kommunikation

## 📌 **Hvad er en PLC?**
En **PLC (Programmable Logic Controller)** er en industriel computer, der bruges til at styre maskiner og processer i fabrikker og automatiserede systemer. Siemens PLC’er som **S7-1200** og **S7-1500** er meget anvendt i industrien.

### **Hvorfor bruge Python til at kommunikere med en PLC?**
Python giver os mulighed for at:

✔️ Læse og skrive data fra en PLC  
✔️ Automatisere tests og overvågning af processer  
✔️ Visualisere data i real-time  
✔️ Integrere PLC’er med databaser og cloud-systemer  

## 🏗️ **Kommunikationsmuligheder**
Der findes flere måder at kommunikere med en Siemens PLC:
- **PROFINET (ISO-on-TCP)** – Industrielt Ethernet
- **MODBUS TCP** – Standardprotokol til kommunikation
- **OPC UA** – Avanceret protokol til IIoT-integration
- **S7 Protocol** – Siemens’ egen kommunikationsprotokol

I denne workshop bruger vi **S7 Protocol** via **Snap7-biblioteket** til Python.

## 🚀 **Næste skridt**
I næste modul opsætter vi en **Siemens PLC** i **TIA Portal**, så den er klar til kommunikation med Python.
