# 🖥️ **Installation af Snap7 i Python**

## 📌 **Formål**
I dette modul installerer vi **Snap7**, som bruges til at kommunikere med Siemens PLC'er via Python.

---

## 🔧 **Trin 1: Installér Snap7**
Åbn en terminal/kommandoprompt og kør:

```sh
pip install python-snap7
```

For at bekræfte installationen, kør følgende i en Python-terminal:

```python
import snap7
print("Snap7 version:", snap7.__version__)
```

Hvis Snap7 er korrekt installeret, vises versionen.

---

## 🏗 **Trin 2: Download Snap7 DLL (Windows-brugere)**
Hvis du får en fejl relateret til manglende `snap7.dll`, skal du:

1. Download Snap7 DLL fra [Snap7 GitHub](https://github.com/fgsect/snap7).  
2. Udpak filerne og placer `snap7.dll` i samme mappe som din Python-kode.  
3. Tilføj DLL-filen til din **PATH-variabel** (Windows).  

På Linux/Mac kan du installere Snap7 som en systembibliotek:

```sh
sudo apt-get install snap7
```
---

Reference: [readthedocs](https://python-snap7.readthedocs.io/en/0.5/installation.html)

---

## 🔄 **Trin 3: Test Snap7-forbindelse**
Opret en testforbindelse til PLC’en:

```python
import snap7

plc = snap7.client.Client()
PLC_IP = "192.168.0.1"

plc.connect(PLC_IP, 0, 1)  # Slot 1 for S7-1200/1500
if plc.get_connected():
    print("Forbundet til PLC!")
plc.disconnect()
```

Hvis du ser `"Forbundet til PLC!"`, fungerer din Snap7-installation korrekt.

---

## 🚀 **Næste trin**
✅ Du har nu Snap7 klar til brug!  
Gå videre til næste modul: [📄 04-read-data.md](04-read-data.md) 📥
