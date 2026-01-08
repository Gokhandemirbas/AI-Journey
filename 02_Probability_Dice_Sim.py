import numpy as np
import matplotlib.pyplot as plt

# 1. Deney: 10.000 kez zar atalım
# Zarın her yüzü (1-6) teorik olarak 1/6 (~0.166) olasılığa sahiptir.
deney_sayisi = 10000
zarlar = np.random.randint(1, 7, size=deney_sayisi)

# 2. Sonuçları sayalım
degerler, adetler = np.unique(zarlar, return_counts=True)
olasiliklar = adetler / deney_sayisi

# 3. Görselleştirme (Probability Mass Function - PMF)
plt.figure(figsize=(10, 6))
plt.bar(degerler, olasiliklar, color='skyblue', edgecolor='black', alpha=0.7)
plt.axhline(y=1/6, color='red', linestyle='--', label='Teorik Olasılık (1/6)')

plt.title(f"{deney_sayisi} Zar Atışının Olasılık Dağılımı")
plt.xlabel("Zar Yüzü")
plt.ylabel("Gözlemlen Olasılık")
plt.xticks(degerler)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Mühendisçe çıktı:
for i, prob in enumerate(olasiliklar):
    print(f"Zarın {i+1} gelme olasılığı: {prob:.4f}")