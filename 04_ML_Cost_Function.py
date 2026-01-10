import numpy as np

# 1. Veri Seti (Training Set)
x_train = np.array([50.0, 60.0, 80.0, 100.0, 120.0])
y_train = np.array([150.0, 180.0, 230.0, 290.0, 340.0])

# 2. Model Parametreleri (y = wx + b)
w = 2.0  # Bu sefer bilerek biraz yanlış bir değer verelim
b = 50.0

# 3. Maliyet Fonksiyonu (Cost Function - J)
def compute_cost(x, y, w, b):
    m = x.shape[0]  # Veri sayısı
    cost_sum = 0
    
    for i in range(m):
        f_wb = w * x[i] + b  # Modelin tahmini
        cost = (f_wb - y[i]) ** 2  # Hatanın karesi (Negatif değerlerden kurtulmak için)
        cost_sum += cost
    
    total_cost = (1 / (2 * m)) * cost_sum
    return total_cost

# Hesaplama
mevcut_maliyet = compute_cost(x_train, y_train, w, b)

print(f"w={w}, b={b} parametreleri için toplam maliyet: {mevcut_maliyet:.2f}")
print("Hedefimiz: Bir sonraki adımda bu sayıyı sıfıra yaklaştırmak!")