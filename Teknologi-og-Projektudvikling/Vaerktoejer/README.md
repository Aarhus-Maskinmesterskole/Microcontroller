# ⚙️ Værktøjer og Utilities

Denne mappe indeholder installationsguides, konfigurationsfiler og troubleshooting information for alle værktøjer brugt i kurset.

## 📁 Struktur

### 📥 [Installation Guides](Installation-guides/)
Step-by-step guides til installation af alle nødvendige værktøjer.

**Guides tilgængelige:**
- [Arduino IDE Setup](Installation-guides/Arduino-IDE-Setup.md) - Komplet opsætning til ESP32
- Python Environment Setup - Python, pip og virtual environments
- Node-RED Installation - Platform setup og initial configuration
- Home Assistant Setup - Installation og basic configuration
- Development Tools - VS Code, Git og andre utilities

### ⚙️ [Konfiguration](Konfiguration/)
Konfigurationsfiler og templates for forskellige værktøjer.

**Indhold:**
- Arduino IDE preferences
- Node-RED default flows
- Home Assistant configurations
- Python requirements.txt filer
- Environment variable templates

### 🔧 [Troubleshooting](Troubleshooting/)
Løsninger på almindelige problemer og fejl.

**Problem kategorier:**
- ESP32 Hardware issues
- USB Driver problems  
- Software installation errors
- Network og communication problems
- Performance og optimization issues

---

## 🛠️ Værktøj Oversigt

### Hardware Udvikling
| Værktøj | Formål | Installation Guide |
|---------|--------|-------------------|
| **Arduino IDE** | ESP32 programmering | [Setup Guide](Installation-guides/Arduino-IDE-Setup.md) |
| **PlatformIO** | Avanceret embedded development | Coming soon |
| **Thonny** | Alternative til Arduino IDE | Python-based ESP32 programming |

### Software Udvikling
| Værktøj | Formål | Installation Guide |
|---------|--------|-------------------|
| **Python 3.8+** | Data processing og automation | Python Environment Setup |
| **VS Code** | Code editor med ESP32 support | Development Tools |
| **Git** | Version control (optional) | Development Tools |

### Integration Platforme
| Værktøj | Formål | Installation Guide |
|---------|--------|-------------------|
| **Node-RED** | Flow-baseret programmering | Node-RED Installation |
| **Home Assistant** | Home automation platform | Home Assistant Setup |
| **MQTT Broker** | Message passing (optional) | Advanced Integration |

### Data og Visualization
| Værktøj | Formål | Installation Guide |
|---------|--------|-------------------|
| **Python Matplotlib** | Real-time plotting | Python Environment Setup |
| **Python Pandas** | Data analysis | Python Environment Setup |
| **InfluxDB** | Time-series database (optional) | Advanced Data Storage |

---

## 🚀 Quick Start

### Minimal Setup (Første lektion)
**Hvad skal du have installeret:**
1. **Arduino IDE** - til ESP32 programmering
2. **USB Drivers** - til ESP32 kommunikation
3. **Python** - til data processing

**Estimated time:** 30-45 minutter

### Complete Setup (Uge 2-3)
**Alt til hele kurset:**
1. **Hardware tools** (Arduino IDE, drivers)
2. **Python environment** (Python, packages)
3. **Integration platforms** (Node-RED, Home Assistant)

**Estimated time:** 2-3 timer over flere sessioner

### Advanced Setup (Optional)
**For entusiaster:**
1. **Development tools** (VS Code, Git)
2. **Database systems** (InfluxDB, Grafana)
3. **Advanced networking** (VPN, SSL certificates)

---

## 💻 Platform Support

### Windows 10/11
**Fully supported** - alle guides testet på Windows
- Native USB driver support
- PowerShell scripts til automation
- Windows Terminal anbefalet

### macOS (10.15+)
**Well supported** - de fleste features fungerer
- Homebrew package manager anbefalet
- Nogle USB drivers kræver manual installation
- Terminal.app eller iTerm2

### Linux (Ubuntu/Debian)
**Community supported** - grundlæggende guides tilgængelige
- Package managers (apt, yum) supported
- USB permissions kan kræve configuration
- Terminal med sudo access nødvendig

---

## ⚡ Performance Tips

### ESP32 Optimization
- **Baudrate:** Start med 115200, øg hvis stable
- **Power supply:** Brug kvalitets USB kabler
- **Heat management:** Undgå overophedning ved intensive tasks

### Python Performance
- **Virtual environments:** Isolér project dependencies
- **Package versions:** Brug tested versions fra requirements.txt
- **Memory management:** Monitor RAM usage ved large datasets

### Network Optimization
- **WiFi stability:** 2.4GHz netværk anbefales for ESP32
- **Firewall configuration:** Allow relevant ports
- **Bandwidth:** Monitor network usage under streaming

---

## 🔧 Development Workflow

### Anbefalet Workflow
1. **Hardware test** - verificér ESP32 og sensorer
2. **Software development** - implementér features iterativt
3. **Integration testing** - test på target platform
4. **Documentation** - dokumentér opsætning og kode
5. **Deployment** - deploy til production environment

### Version Control (Optional)
```bash
# Basic Git workflow for projects
git init
git add .
git commit -m "Initial commit"
git branch feature/sensor-integration
git checkout feature/sensor-integration
# ... develop feature ...
git add .
git commit -m "Add DHT22 sensor support"
git checkout main
git merge feature/sensor-integration
```

### Backup Strategy
- **Code:** Git repositories eller cloud storage
- **Configurations:** Export settings before major changes
- **Data:** Regular CSV exports fra logging
- **Hardware:** Photo documentation af wiring

---

## 📞 Support Channels

### Self-Service
1. **Check troubleshooting guide** for dit problem
2. **Search online** - Stack Overflow, Reddit
3. **Review documentation** for relevant tools
4. **Test with minimal setup** to isolate issues

### Peer Support
- **Class Discord/Teams** - ask classmates
- **Study groups** - work through problems together
- **Code review** - help each other improve

### Instructor Support
- **Office hours** - scheduled help sessions
- **Email** - for complex technical issues
- **In-class** - questions during lessons
- **Project meetings** - one-on-one guidance

---

## 📈 Skill Development Path

### Beginner (Uge 1-3)
**Focus:** Get tools working reliably
- Install og configure basic tools
- Understand hardware connections
- Basic programming concepts

### Intermediate (Uge 4-9)
**Focus:** Integration og automation
- Multi-platform development
- Advanced debugging techniques
- System architecture design

### Advanced (Uge 10-12)
**Focus:** Production-ready systems
- Performance optimization
- Security considerations
- Deployment strategies

---

## 🔄 Updates og Maintenance

### Keeping Tools Updated
- **Arduino IDE:** Check monthly for ESP32 platform updates
- **Python packages:** Use `pip list --outdated` regularly
- **Node-RED:** Update via npm when stable versions release
- **Home Assistant:** Follow their release schedule

### Configuration Backup
Before major updates:
```bash
# Backup Arduino IDE preferences
# Windows: %APPDATA%/Arduino15/
# macOS: ~/Library/Arduino15/
# Linux: ~/.arduino15/

# Export Node-RED flows
# Dashboard → Menu → Export → All flows

# Export Home Assistant configuration
# /config/ directory backup
```

---

*Disse værktøjer er jeres foundation - investér tid i at få dem konfigureret korrekt fra start! 🛠️*