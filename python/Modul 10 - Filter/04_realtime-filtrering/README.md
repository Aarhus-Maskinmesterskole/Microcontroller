# 🧪 Modul 04 – Mini-projekt: Filtrering og realtidsvisualisering

I dette modul skal du selvstændigt kombinere det, du har lært i de tidligere moduler. Du skal hente realtidsdata fra ESP32, filtrere dem og visualisere dem live i ét samlet Python-script.

---

## 🎯 Mål for mini-projektet

✔️ Kombinere seriel dataopsamling og visualisering  
✔️ Filtrere temperaturdata i realtid  
✔️ Visualisere både rå og filtrerede data samtidig  
✔️ Øge forståelsen af filtre og realtidsplotning gennem praktisk anvendelse

---

## 🔧 Forslag til struktur

1. Læs realtidsdata via `pyserial`
2. Pars data som `timestamp`, `temperature`, `humidity`
3. Brug en glidende liste eller buffer til de seneste datapunkter
4. Beregn og vis filtrerede værdier live
5. Brug `matplotlib.animation` til at opdatere plottet kontinuerligt

---

## 📜 Eksempel (skitse)

```python
# pseudokode / struktur
buffer = []
window_size = 5

while True:
    t, temp, hum = læs_fra_serial()
    buffer.append(temp)
    if len(buffer) > window_size:
        buffer.pop(0)
    filtered = sum(buffer) / len(buffer)  # glidende gennemsnit
    opdater_plot(t, temp, filtered)
```

---

## 💡 Udvidelsesidéer

- Tilføj medianfilter eller FFT-baseret filtrering
- Gem data i en fil undervejs
- Tilføj knapper, sliders eller interaktion med `matplotlib.widgets`
- Filtrer både temperatur og fugtighed

---

## 🔁 Din opgave

1. Lav en komplet Python-applikation, der:
   - Læser seriel data i CSV-format fra ESP32
   - Filtrerer temperatur (mean, median eller andet)
   - Plottet både rå og filtreret temperatur i realtid

2. *(Valgfrit)* Udvid med:
   - Fugtighedsdata
   - Dataopsamling i fil
   - Dynamisk valg af filtertype eller vinduesstørrelse

---

✅ Når du har lavet dit mini-projekt, kan du eksperimentere videre i de avancerede moduler: [`05_ekstra`](../05_ekstra/) og [`06_signalfiltrering`](../06_signalfiltrering/)!

