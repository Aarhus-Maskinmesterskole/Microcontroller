# 🔧 **Opsætning af Siemens PLC i TIA Portal**

## 📌 **Formål**
I dette modul opsætter vi en **Siemens PLC** i **TIA Portal**, så den kan kommunikere med Python via **Snap7**.  
Dette inkluderer netværksopsætning, datablocks og tilladelser til ekstern adgang.

---

## 🖥️ **Trin 1: Opret et nyt projekt**
1. **Åbn TIA Portal** og opret et nyt projekt.  
2. Tilføj en **S7-1200 eller S7-1500 PLC**.  
3. Giv PLC'en et navn og vælg den korrekte **hardwarekonfiguration**.

---

## 🌐 **Trin 2: Konfigurer netværksindstillinger**
1. **Åbn "Devices & Networks"**.  
2. **Tildel en IP-adresse** til PLC'en (f.eks. `192.168.0.1`).  
3. Sørg for, at din computer er på samme subnet (f.eks. `192.168.0.x`).  

ℹ️ **Tip**: Du kan teste forbindelsen ved at "ping'e" PLC’en fra din computer:

```sh
ping 192.168.0.1
```

---

## 🔒 **Trin 3: Tillad adgang med Snap7**
For at Python kan kommunikere med PLC’en, skal **PUT/GET-kommunikation** aktiveres:

1. **Gå til PLC’s egenskaber** → "Protection & Security".  
2. **Aktiver "Permit access with PUT/GET communication from remote partner"**.  
3. **Deaktiver optimeret adgang til datablocks** (hvis nødvendigt).  

---

## 📂 **Trin 4: Opret en datablock (DB1)**
1. **Gå til "Program Blocks"** → Opret en **ny datablock** (DB1).  
2. **Tilføj følgende variabler**:  

| **Navn**       | **Datatype** | **Offset** |
|---------------|------------|------------|
| `RealValue`   | REAL       | 0.0        |
| `BoolValue`   | BOOL       | 4.0        |
| `IntValue`    | INT        | 6.0        |

3. **Download programmet til PLC’en**.

---

## 🚀 **Næste trin**
✅ Din PLC er nu klar til at kommunikere med Python!  
Gå videre til næste modul: [📄 03-snap7-installation.md](03-snap7-installation.md) 🖥️
