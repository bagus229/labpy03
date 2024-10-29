import random

# Meminta input dari pengguna
n = int(input("Masukkan nilai N: "))

# Inisialisasi variabel untuk menghitung jumlah bilangan acak yang dihasilkan
count = 0

# Menghasilkan bilangan acak kurang dari 0.5
while count < n:
    angka = random.random()
    if angka < 0.5:
        count += 1
        print(f"data ke-{count} => {angka}")

print("Selesai")