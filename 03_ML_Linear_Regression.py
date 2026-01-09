import numpy as np
import matplotlib.pyplot as plt

# 1. Veri Seti (Training Set)
# x_train: Evin metrekaresi, y_train: Evin fiyatı (1000 TL cinsinden)
x_train = np.array([50.0, 60.0, 80.0, 100.0, 120.0])
y_train = np.array([150.0, 180.0, 230.0, 290.0, 340.0])

# 2. Model Parametreleri (y = wx + b)
# Başlangıçta rastgele değerler veriyoruz, model bunları düzeltecek
w = 2.5
b = 20

# 3. Tahmin Fonksiyonu (Prediction)
def predict(x, w, b):
    return w * x + b

y_pred = predict(x_train, w, b)

# 4. Görselleştirme
plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train, marker='x', c='r', label='Gerçek Veriler')
plt.plot(x_train, y_pred, c='b', label='Model Tahmini (İlkel Hal)')

plt.title("Evin Metrekaresine Göre Fiyat Tahmini")
plt.xlabel("Metrekare (m^2)")
plt.ylabel("Fiyat (1000 TL)")
plt.legend()
plt.grid(True)
plt.show()

print(f"100 metrekarelik ev için ilk tahmin: {predict(100, w, b)} bin TL")