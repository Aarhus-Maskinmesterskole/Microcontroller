# 📄 Modul 8 – Testplaner og validering (FAT, SAT, SIT)

## 🎯 Formål

Dette modul giver dig forståelse for og praktisk erfaring med udarbejdelse og anvendelse af teststrategier i automatiseringsprojekter. Du vil lære, hvordan man dokumenterer og gennemfører:

- **FAT** – Factory Acceptance Test.
- **SAT** – Site Acceptance Test.
- **SIT** – System Integration Test.

Modulet knytter teorien til dit konkrete projekt med ESP32, IPC og PLC og viser, hvordan du evaluerer systemets funktionalitet, robusthed og integrationsevne.

---

## 🧰 Nødvendige komponenter

- Et gennemført og funktionelt system fra de foregående moduler.
- Testskabeloner (PDF, Excel eller Markdown).
- Testmiljø (lokalt eller via simulator).
- Dokumentation for alle komponenter og flows.

---

## 🧪 Testtyper og anvendelse

### ✅ FAT – Factory Acceptance Test
Test udført i laboratoriemiljø eller før systemet leveres.

- Kontrollerer at funktionaliteten matcher kravspecifikationen.
- Gennemføres typisk af leverandør.
- Eksempler:
  - Sensorer sender stabile værdier.
  - Node-RED visualiserer og logger data korrekt.
  - Snap7-script kan læse og skrive til PLC.

### ✅ SAT – Site Acceptance Test
Test udført på det endelige installationssted.

- Verificerer, at systemet fungerer i sin kontekst.
- Gennemføres sammen med slutbruger/kunde.
- Eksempler:
  - Netværksopsætning fungerer mellem IPC og PLC.
  - Dashboard vises korrekt på operatørstation.
  - CSV-logging sker i korrekt mappe på produktionsserver.

### ✅ SIT – System Integration Test
Helhedsorienteret test af samspillet mellem systemets komponenter.

- Kontrollerer end-to-end funktionalitet.
- Udføres både ved FAT og SAT-niveau.
- Eksempler:
  - ESP32 → Seriel → IPC → Snap7 → PLC → Feedback til IPC.
  - Håndtering af fejl (ingen sensorværdi, PLC offline, USB afbrudt).

---

## 📝 Opgaver

1. Udarbejd en FAT-testplan baseret på din kravspecifikation.
2. Udarbejd en SAT-tjekliste for onsite-afprøvning.
3. Design mindst 3 SIT-scenarier, som involverer hele systemkæden.
4. Gennemfør testene og dokumentér resultaterne.
5. Brug farvekoder (grøn/rød) til visuel markering af teststatus.
6. Diskutér hvad der gik godt og hvad der kræver forbedring.

---

## 📄 Skabelon til FAT/SAT-test (Excel eller Markdown)

| Test ID | Testbeskrivelse                | Forventet resultat              | Status  | Kommentar         |
|---------|--------------------------------|----------------------------------|---------|-------------------|
| FAT-01  | Sensor aflæser temperatur      | Temperatur vises i Node-RED     | ✅/❌    |                   |
| SAT-02  | Dashboard loader i browser     | Alle grafer vises korrekt       | ✅/❌    |                   |
| SIT-03  | End-to-end fra ESP32 til PLC   | PLC reagerer på data input      | ✅/❌    | Forsinkelse på 1s |

---

## ✅ Læringsudbytte

Efter dette modul kan du:

- Skelne mellem FAT, SAT og SIT samt kende deres rolle i projektforløb.
- Udarbejde enkle men effektive testskemaer.
- Gennemføre og dokumentere tests systematisk.
- Identificere svagheder og forbedringsmuligheder.
- Argumentere for vigtigheden af test i industrielle projekter.

---

## 💡 Tips

- FAT/SAT bør altid være baseret på en god kravspecifikation (se Modul 2).
- Gem testresultater sammen med projektets tekniske dokumentation.
- Brug screenshots og datalogning som bevis på gennemførte tests.
- Overvej at anvende automatiserede testskripter ved gentagne afprøvninger.

Test og validering er en kritisk disciplin i professionel automatisering og sikrer, at din løsning er pålidelig og klar til implementering i praksis.