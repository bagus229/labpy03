# Modal awal
modal_awal = 100000000  # 100 juta

# Persentase laba per bulan selama 8 bulan
laba_persen = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]

# Inisialisasi total laba
total_laba = 0

# Loop untuk menghitung laba per bulan
for bulan in range(8):
    laba_bulan = modal_awal * laba_persen[bulan]
    total_laba += laba_bulan
    print(f"laba bulan ke-{bulan+1} sebesar: {laba_bulan}")

# Menampilkan total laba setelah 8 bulan
print(f"Total laba adalah: {total_laba}")