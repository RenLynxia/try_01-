import numpy as np
import matplotlib.pyplot as plt

E = 200e9
I = 1e-6
L = 10
P = 1000

n = 10
x = np.linspace(0, L, n+1)
h = x[1] - x[0]

K = np.zeros((2*(n+1), 2*(n+1)))  # Initialize K with the correct dimensions
for i in range(n):
    K[2*i:2*i+4, 2*i:2*i+4] += E*I/h**3 * np.array([[12, 6*h, -12, 6*h],
                                                 [6*h, 4*h**2, -6*h, 2*h**2],
                                                 [-12, -6*h, 12, -6*h],
                                                 [6*h, 2*h**2, -6*h, 4*h**2]])

# Vektor beban
F = np.zeros(2*n)
F[n] = -P  # Beban terpusat di tengah

# Kondisi batas (simply supported)
K[0, :] = 0
K[-1, :] = 0
F[0] = 0
F[-1] = 0
K[0, 0] = 1
K[-1, -1] = 1

# Vektor beban
F = np.zeros(2*(n+1))  # Initialize F with the correct dimensions
F[n+1] = -P  # Beban terpusat di tengah

# Calculate the deflections 'd' by solving the system of equations Kd = F
d = np.linalg.solve(K, F)

# Visualisasi
plt.plot(x, d[::2])
plt.xlabel('Panjang (m)')
plt.ylabel('Defleksi (m)')
plt.title('Simulasi Defleksi Balok Sederhana')
plt.grid(True)
plt.show()
