# 🛠️ 01 – Installation af Node-RED

Dette dokument guider dig gennem installationen af Node-RED på din lokale computer, så du kan udvikle og teste flows lokalt i en IPC- eller undervisningssammenhæng.

---

## 🎯 Formål
- Installere Node.js og NPM
- Installere Node-RED globalt
- Starte Node-RED lokalt og tilgå editoren
- Installere nødvendige noder og dashboards

---

## 📋 Systemkrav
- Windows 10+, macOS eller Linux
- Administratorrettigheder til installation
- Stabil internetforbindelse

---

## 🔧 Installationstrin
Følg denne video [YouTube](https://www.youtube.com/watch?v=S6ykD6SwO7Q) eller Installationstrin her under
### 1. Installer Node.js
Gå til [https://nodejs.org](https://nodejs.org) og hent **LTS-versionen** (anbefalet). Følg installationsguiden og accepter standardindstillinger.

### 2. Bekræft installation i terminal eller kommandoprompt
```bash
node -v
npm -v
```
Begge kommandoer skal returnere et versionsnummer, fx `v18.19.0`.

### 3. Installer Node-RED globalt
```bash
npm install -g --unsafe-perm node-red
```
Dette installerer Node-RED som globalt CLI-værktøj.

### 4. Start Node-RED
```bash
node-red
```
Du vil se en række loglinjer, der slutter med:
```
[info] Server now running at http://127.0.0.1:1880/
```

### 5. Åbn Node-RED i browser
Åbn følgende URL i din browser:
```
http://localhost:1880
```
Dette åbner editoren hvor du kan bygge dine første flows.

---

📦 Installation af udvidelser

Skift til burger-menuen (☰) øverst til højre i Node-RED-editoren og vælg Manage palette. Herfra kan du:

Klikke på fanen Install

Søge efter de ønskede noder, fx:

node-red-dashboard → giver adgang til brugerfladeelementer (UI)

node-red-node-serialport → anvendes til seriel kommunikation i senere moduler

Klik Install ved siden af den ønskede node

💡 Det anbefales at installere node-red-dashboard allerede nu, mens serialport først er relevant i modul 02.

> 💡 På Windows kan `serialport` kræve installation af drivere som **CH340** eller **CP210x**, afhængigt af din USB-adapter.

---

## 🧪 Testinstallation
For at teste, at alt virker:
1. Start Node-RED med `node-red`
2. Gå til `localhost:1880`
3. Træk en `inject` og `debug` node ind
4. Forbind dem og klik `Deploy`
5. Tryk på `inject` og se output i højre panel

---

## ✅ Klar til næste trin
Du er nu klar til at opbygge dit første flow og arbejde med noder i Node-RED. Fortsæt til `02-foerste-flow.md`.

