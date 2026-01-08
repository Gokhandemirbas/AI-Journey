import numpy as np
import matplotlib.pyplot as plt

# n aralığı (Zaman ekseni: -5'ten +10'a kadar tam sayılar)
n = np.arange(-5, 11)

# 1. Birim Basamak Sinyali: u[n]
# n >= 0 ise 1, diğer durumlarda 0
u_n = np.where(n >= 0, 1, 0)

# 2. Birim Darbe Sinyali: delta[n] (Kronecker Delta)
# Sadece n = 0 iken 1, diğer her yerde 0
delta_n = np.where(n == 0, 1, 0)

# Görselleştirme
plt.figure(figsize=(12, 7))

# İlk grafik: Unit Step (Birim Basamak)
plt.subplot(2, 1, 1)
plt.stem(n, u_n)
plt.title("Birim Basamak Fonksiyonu - $u[n]$")
plt.ylabel("Genlik")
plt.grid(True)

# İkinci grafik: Unit Impulse (Birim Darbe)
plt.subplot(2, 1, 2)
plt.stem(n, delta_n, linefmt='r-', markerfmt='ro') # Kırmızı renk
plt.title("Birim Darbe Fonksiyonu - $\delta[n]$")
plt.xlabel("n (Örnekleme)")
plt.ylabel("Genlik")
plt.grid(True)

plt.tight_layout()
plt.show()