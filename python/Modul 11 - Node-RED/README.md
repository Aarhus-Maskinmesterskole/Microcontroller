# 🚀 Node-RED Standard Workshop – IPC, Python og PLC-integration

Denne workshop fokuserer på **standardfunktioner i Node-RED** til integration med Python-scripts, datavisualisering og kommunikation med industrielle systemer. Målgruppen er automationsteknologer, der skal lære at bruge Node-RED som et centralt værktøj i IPC-miljøer og industrielle automatiseringssystemer.

---

## 🎯 Læringsmål

Ved afslutningen af workshoppen skal den studerende kunne:

- Bruge Node-RED’s standardnoder til at opbygge komplette dataflows
- Kommunikere med Python-scripts via `exec`-noden og håndtere `stdout` og `stdin`
- Udveksle data mellem Node-RED og Siemens PLC’er vha. Snap7 og Python
- Læse og tolke output fra Python i Node-RED og sende data retur
- Opbygge realtids-visualisering med `ui_chart`, `ui_text`, `debug`, `switch` og `template`
- Logge data til CSV-filer fra Python eller Node-RED
- Strukturere flows med `function`, `change`, `switch`, `template`, `subflows` og `inject`
- Installere og bruge udvidelsesbiblioteker i Node-RED via palette manager
- Fejlsøge og dokumentere flows med `status`, `catch`, `complete`, `comment` og versionsstyring

---

## 📦 Teknologier og værktøjer
- Node-RED (lokal installation eller Docker)
- Python 3.x (lokalt installeret)
- Snap7 (Python-bibliotek til Siemens PLC)
- Siemens S7-1200 eller PLCSIM Advanced
- CSV-logger via Python eller Node-RED

---

## 📁 Workshopstruktur

```bash
NodeRED-Workshop/
├── 01-intro/                  # Introduktion, installation, begreber og standardnoder
│   ├── 01-installation-node-red.md
│   ├── 02-foerste-flow.md
│   ├── 03-node-red-begreber.md
│   └── 04-standardnoder/      # Underopdeling af basale noder
│       ├── 01-inject.md
│       ├── 02-debug.md
│       ├── 03-function.md
│       ├── 04-change.md
│       ├── 05-switch.md
│       ├── 06-delay.md
│       └── 07-template.md
├── 02-seriel/                 # Kommunikation over seriel port (USB, RS232)
├── 03-dashboard/              # Visualisering og brugerflader med node-red-dashboard
├── 04-logging/                # Dataopsamling og CSV-logning
├── 05-python-exec/            # Kørsel af Python-scripts via exec-node (5 miniworkshops)
│   ├── 01-python-stdout/
│   ├── 02-arguments-to-python/
│   ├── 03-stdin-to-python/
│   ├── 04-python-math/
│   └── 05-snap7-basic-read/
├── scripts/                   # Fælles Python-scripts og eksempler
├── Diverse/                   # Docker-opsætning, systeminstallation, m.m.
├── shared/                    # Fælles aktiver: billeder, flows, stylesheets
└── README.md                  # Overordnet kursusbeskrivelse og moduloversigt
```


---

## 🧩 Moduloversigt

| Modul | Titel                          | Indhold                                                          |
|--------|--------------------------------|-------------------------------------------------------------------|
| 01     | Introduktion til Node-RED      | UI, noder, deploy, eksempler                                      |
| 02     | Seriel kommunikation           | Seriel modtagelse og afsendelse, parsing og visualisering         |
| 03     | Dashboard og visualisering     | `ui_chart`, `ui_text`, `template`, `gauge`, `switch`              |
| 04     | Logging og CSV                 | Logging via Python eller Node-RED, struktur og rotation           |
| 05     | Python-integration (5 miniworkshops) | Miniworkshops med stdout, argv, stdin, Snap7 og beregning     |

---

## ✅ Slutresultat
- Du har lært at bruge Node-RED professionelt uden brug af IoT-elementer
- Du har opnået erfaring med at kombinere industrielle datakilder og Python
- Du kan bygge dashboards, eksekvere scripts, kommunikere med PLC og dokumentere flows