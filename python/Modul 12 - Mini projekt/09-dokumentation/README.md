# 📄 Modul 9 – Teknisk dokumentation og PEP8-guidelines

## 🎯 Formål

I dette afsluttende modul lærer du at strukturere og formulere teknisk dokumentation for hele dit system. Du skal også sikre, at din Python-kode på både ESP32 og IPC overholder PEP8-standarder, som anvendes bredt i industrien og den akademiske verden for at sikre læsbarhed, vedligeholdelse og samarbejde.

Dokumentationen skal kunne anvendes som grundlag for vedligehold, fejlretning, udvidelser og test (jf. Modul 8).

---

## 📑 Hvad skal dokumenteres?

- **Systemarkitektur**
  - Beskrivelse af komponenter (ESP32, sensorer, IPC, PLC).
  - Blokdiagrammer og forbindelser.

- **Softwarestruktur**
  - Flowbeskrivelse i Node-RED.
  - Forklaring af Python-scripts (ESP32 og IPC).
  - Forklaring af Snap7-kommunikation og seriel parsing.

- **Kravspecifikation og test**
  - Referér til dokumenter fra Modul 2 og 8.

- **Brugerflade**
  - Screenshots af Node-RED dashboard.
  - Forklaring af funktioner og betjening.

- **Versionsstyring og ændringslog**
  - Kort changelog, fx i `CHANGELOG.md`.
  - Brug af Git anbefales, hvis muligt.

---

## 🧪 PEP8 – Python coding standards

PEP8 er en stilguide for Python-programmering, og indeholder bl.a.:

- Indrykning: 4 mellemrum per niveau.
- Maks linjelængde: 79 tegn.
- Imports: altid i toppen af filen.
- Variabelnavne: små bogstaver med underscore (`sensor_temp`).
- Funktioner: korte og præcise, dokumenteret med docstrings.
- Blank linje mellem funktioner og klasser.

> Anvend [pycodestyle](https://pypi.org/project/pycodestyle/) eller editor-plugins til at validere din kode:
```bash
pip install pycodestyle
pycodestyle main.py
```

---

## 📝 Opgaver

1. Udarbejd en samlet teknisk rapport over hele dit projekt.
2. Indsæt relevante diagrammer og flowbeskrivelser.
3. Tilføj kodeudsnit og forklar deres funktion.
4. Brug PEP8 til at kvalitetssikre al Python-kode.
5. Upload rapport som PDF og evt. Markdown-version i GitHub-repo.
6. (Hvis uploadet i GitHub-repo) Opsæt `README.md` til at give overblik over hele projektet.

---

## ✅ Læringsudbytte

- Du kan dokumentere et teknisk system struktureret og professionelt.
- Du forstår vigtigheden af læsbar kode og konsistens.
- Du kan anvende PEP8 som værktøj til kodestandard.
- Du har reflekteret over, hvordan dokumentation understøtter drift, test og overdragelse.

---

## 💡 Tips

- Lav en skabelon med forsiden, indholdsfortegnelse, figurer og bilag.
- Brug værktøjer som Typora, Obsidian, LaTeX eller Word – men hold fokus på indhold og faglighed.
- Overvej at inkludere en tabel over pin-konfigurationer, datatyper og logfilens struktur.
- Sørg for at dine Git-commits har meningsfulde beskeder.

Afslutningen af dette modul markerer overgangen fra udvikling til vedligehold – et vigtigt skridt i ethvert teknologiprojekt.