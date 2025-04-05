# 🧩 Modul 05 – Python-integration via `exec`-noden

Dette modul består af en række praktiske mini-workshops, hvor du lærer at integrere Python med Node-RED ved hjælp af `exec`-noden. Hver workshop fokuserer på en konkret teknik, som bygger videre på dine eksisterende Node-RED-kompetencer og gradvist udvider dem med Python-funktionalitet.

Ved hjælp af `exec`-noden kan du:
- Udføre Python-scripts direkte fra dine flows
- Sende data fra Node-RED til Python via argumenter eller `stdin`
- Læse resultater fra Python via `stdout`
- Integrere med eksterne systemer, herunder Siemens PLC’er via Snap7

Denne tilgang giver dig en stærk low-code/high-code kombination, hvor logik, visualisering og kontrol håndteres i Node-RED, mens Python bruges til databehandling, avancerede biblioteker og kommunikation med hardware.

---

## 📂 Indhold
Herunder ses oversigten over de fem mini-workshops, som du kan arbejde dig igennem:

- [🔧 Workshop 1 – Simpelt Python-output](./01-python-stdout/README.md)  
  Lær at modtage tekst-output fra et Python-script i Node-RED.

- [📤 Workshop 2 – Sende argumenter til Python](./02-arguments-to-python/README.md)  
  Skriv data til Python som kommandolinjeargumenter og få det returnerede resultat.

- [📥 Workshop 3 – Sende input via stdin](./03-stdin-to-python/README.md)  
  Send tekst direkte til Python-scriptet via standard input og behandl det i realtid.

- [➕ Workshop 4 – Beregninger med input](./04-python-math/README.md)  
  Kombinér brug af `exec`, `function` og Python til simple beregninger.

- [🏭 Workshop 5 – Snap7 læsning](./05-snap7-basic-read/README.md)  
  Brug Python og Snap7-biblioteket til at læse data fra en Siemens PLC og sende værdier tilbage til Node-RED.

Alle tilhørende scripts findes i [`scripts`](./scripts/) mappen og kan redigeres og udvides efter behov.

---

🚀 Klar til at begynde? Start med [Workshop 1](./01-python-stdout/README.md) og følg rækkefølgen for at opbygge kompetencerne trin for trin.

