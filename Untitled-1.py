import sys
import numpy as np

# Hangi Python'ı kullanıyoruz?
print(f"Aktif Python Yolu: {sys.executable}")

# NumPy yüklü mü?
try:
    print(f"NumPy Sürümü: {np.__version__}")
    print("Sistem Hazır! İlk DSP sinyali için her şey tamam.")
except:
    print("NumPy henüz yüklü değil, 'conda install numpy' yapmalısın.")