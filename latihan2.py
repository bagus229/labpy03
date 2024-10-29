modal_awal = 100000000  # 100 juta

laba_persen = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.02]

total_laba = 0

for bulan in range(8):
    laba_bulan = modal_awal * laba_persen[bulan]
    total_laba += laba_bulan
    print(f"laba bulan ke-{bulan+1} sebesar: {laba_bulan}")

print(f"Total laba adalah: {total_laba}")