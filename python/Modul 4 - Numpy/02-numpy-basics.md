# 🔢 Modul 2: Grundlæggende NumPy operationer

## 📌 **Introduktion**
Dette modul introducerer NumPy’s grundlæggende funktioner til **databehandling og analyse**, som er vigtige i automation og signalbehandling.

🔗 **Forrige modul:** [01-installation.md](01-installation.md)  
🔜 **Næste modul:** [03-signal-processing.md](03-signal-processing.md)  

---

## ✅ **Trin 1: Opret en NumPy-array**
En **NumPy-array** er en datastruktur, der er hurtigere og mere effektiv end Python-lister.

```python
import numpy as np

data = np.array([10, 20, 30, 40])
print(data)
```
🔹 Output:
```
[10 20 30 40]
```
✅ **Nu har du oprettet din første NumPy-array!**  

---

## 📊 **Trin 2: Matematiske operationer med arrays**
Med NumPy kan du udføre **vektoriserede beregninger** uden loops.

```python
result = data * 2  # Ganger hvert element med 2
print(result)
```
🔹 Output:
```
[20 40 60 80]
```
✅ **NumPy gør det let at udføre hurtige matematiske beregninger!**  

---

## 📏 **Trin 3: Generér en sekvens af tal**
I automation er det ofte nødvendigt at generere **jævnt fordelte talværdier**.

```python
sequence = np.linspace(0, 10, 5)  # 5 tal mellem 0 og 10
print(sequence)
```
🔹 Output:
```
[ 0.   2.5  5.   7.5 10. ]
```
✅ **`linspace()` er nyttig til signal- og tidsanalyse!**  

---

## 📋 **Trin 4: Statistiske funktioner**
NumPy har indbyggede funktioner til **statistisk analyse af data**, som bruges i dataopsamling og automation.

```python
data = np.array([5, 10, 15, 20, 25])

print("Gennemsnit:", np.mean(data))
print("Maksimum:", np.max(data))
print("Minimum:", np.min(data))
print("Standardafvigelse:", np.std(data))
```
🔹 Output:
```
Gennemsnit: 15.0
Maksimum: 25
Minimum: 5
Standardafvigelse: 7.0710678118654755
```
✅ **Nu kan du analysere data med NumPy!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Oprettet NumPy-arrays  
✔️ Udført matematiske beregninger uden loops  
✔️ Genereret talrækkefølger til signalanalyse  
✔️ Brugt statistiske funktioner til dataanalyse  

🔜 **Fortsæt til næste modul:** [03-signal-processing.md](03-signal-processing.md), hvor vi arbejder med **signalbehandling i NumPy**!  
