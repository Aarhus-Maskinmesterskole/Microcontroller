# 📄 Modul 4 – Opsamling og udskrivning af sensorværdier

## 🎯 Formål
Dette modul har til formål at gøre dig i stand til at læse data fra tre forskellige sensorer tilsluttet ESP32 og sende dem ud som CSV-lignende tekst over den serielle port. Dataene skal senere bruges i Node-RED til realtidsvisualisering og datalogning. Formålet er både at lære om selve sensoropsamlingen og hvordan man strukturerer og formaterer data, så de let kan integreres i et større automatiseringssystem.

Du vil desuden lære om ADC-konfiguration på ESP32, fejlhåndtering i MicroPython og hvordan man strukturerer kode, så den er genanvendelig i andre projekter.

## 🧰 Anvendte sensorer
| Sensor | Funktion               | Tilslutning         | Beskrivelse |
|--------|------------------------|----------------------|-------------|
| DHT22  | Temperatur og luftfugt | Digital, GPIO14     | Sender digitale signaler med temperatur og fugt
| MQ2    | Gasdetektion           | Analog, GPIO35      | Måler luftkvalitet (fx metan, propan, butan)
| LDR    | Lysintensitet          | Analog, GPIO34      | Reagerer på lysmængde (høj værdi = mørkt)

> Husk at tilslutte GND og 3.3V korrekt. Nogle sensorer kræver modstande for korrekt funktion. Undersøg om jeres DHT22 fungerer bedst med en pull-up modstand i produktdatabladet.

Ved opbygning af kredsløbet skal du sikre, at spændingsniveauet fra sensorerne ikke overstiger 3.3V, da ESP32 ikke tåler 5V på input-pins.

---

## ⚙️ MicroPython-kodeeksempel

Herunder ses et eksempel på, hvordan du kan læse data fra alle tre sensorer og sende værdierne til seriel port som kommasepareret output.

```python
from machine import Pin, ADC
from dht import DHT22
from time import sleep

# Initialisering
sensor_dht = DHT22(Pin(14))
sensor_gas = ADC(Pin(35))
sensor_ldr = ADC(Pin(34))
sensor_gas.atten(ADC.ATTN_11DB)  # Tillader op til ca. 3.6V input
sensor_ldr.atten(ADC.ATTN_11DB)

# Læs data i loop
while True:
    try:
        sensor_dht.measure()
        temp = sensor_dht.temperature()
        hum = sensor_dht.humidity()
        gas = sensor_gas.read()
        light = sensor_ldr.read()

        # Send CSV-lignende data til seriel port
        print("{},{},{},{}".format(temp, hum, gas, light))
        sleep(1)
    except Exception as e:
        print("Fejl: ", e)
        sleep(2)
```

> Output eksempel:
```
24.5,40.2,601,832
24.6,40.0,607,829
```

Denne type output er ideel til at blive læst og parseret af Node-RED via en `serial in` node, som kan splitte linjer og fordele værdier til visning eller lagring.

---

## 📝 Opgave
1. Tilslut de tre sensorer korrekt på breadboard og dokumentér kredsløbet.
2. Upload og afprøv MicroPython-koden via Thonny eller mpremote.
3. Observer outputtet i den serielle konsol og forklar, hvad hver værdi repræsenterer.
4. Rediger evt. koden, så den sender data med labels (fx `print("T:{},H:{},G:{},L:{}".format(...))`), eller som JSON.
5. Forklar forskellen på analog og digital input og hvorfor det er vigtigt for ESP32-konfiguration.
6. Skriv en kort analyse: Hvad betyder det, hvis LDR-værdien er lav men MQ2-værdien er høj?.
7. Udvid koden, så den også sender en timestamp med hver måling (brug evt. `time.localtime()` hvis RTC er sat).

## ✅ Output
- Sensorer er korrekt tilsluttet og verificeret fysisk og elektrisk.
- Seriel output viser fire relevante værdier hvert sekund.
- Koden er veldokumenteret med kommentarer og fejlhåndtering.
- Du har eksperimenteret med forskellige datapræsentationer (raw, label, JSON).

---

## 💡 Tips og fejlretning
- Du kan øge spændingsstabilitet med kondensator (10μF–100μF) mellem VCC og GND tæt på sensorerne
- Brug `print("\n")` mellem målinger hvis Node-RED splitter på linjeskift
- Hvis DHT22 fejler, prøv at sætte en 10k pull-up modstand på data-pin (ikke nødvendigt med jeres DHT22)
- LDR og MQ2 skal initialiseres korrekt som ADC og attenueres for at undgå klipning ved høje værdier
- Brug en logbog eller tag screen shots: skriv hvad du ser i terminalen og hvordan det ændrer sig når du påvirker sensorerne (lys, gas, temperatur)

---

Når du har styr på sensoropsamlingen og forstår hvordan signalerne ser ud på seriel port, er du klar til at forbinde IPC og visualisere dataene i **Node-RED** i næste modul!