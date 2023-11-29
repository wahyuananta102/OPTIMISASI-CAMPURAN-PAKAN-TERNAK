from scipy.optimize import linprog

# Koefisien fungsi tujuan (minimalkan biaya)
c = [10, 8]  # Harga per kg bahan pakan A dan B

# Koefisien batasan untuk protein (>= 18 unit)
A_protein = [[-3, -2]]  # Koefisien untuk bahan pakan A dan B
b_protein = [-18]  # Batasan protein

# Koefisien batasan untuk energi (>= 24 unit)
A_energi = [[-2, -4]]  # Koefisien untuk bahan pakan A dan B
b_energi = [-24]  # Batasan energi

# Batasan non-negatif untuk jumlah bahan pakan A dan B
bounds = [(0, None), (0, None)]  # Bahan pakan A dan B tidak bisa kurang dari 0 kg

# Solusi menggunakan linprog
result = linprog(c, A_ub=A_protein + A_energi, b_ub=b_protein + b_energi, bounds=bounds, method='highs')

# Tampilkan hasil
print("Jumlah kg bahan pakan A yang harus digunakan:", result.x[0], "kg")
print("Jumlah kg bahan pakan B yang harus digunakan:", result.x[1], "kg")
print("Biaya minimal yang diperlukan:", result.fun, "ribu rupiah")
