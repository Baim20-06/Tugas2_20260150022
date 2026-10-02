"""
Program: Kalkulator BMI dan Kasir Sederhana
Bagian 1 : Menghitung BMI (Body Mass Index)
Bagian 2 : Menghitung total belanja di kasir (dengan diskon & pajak)
"""

# =========================================================
# BAGIAN 1: BMI
# =========================================================
print("=== BAGIAN 1: KALKULATOR BMI ===")

nama = input("Nama: ")
nim = input("NIM: ")
berat = float(input("Berat Badan (kg): "))
tinggi_cm = float(input("Tinggi Badan (cm): "))

# Konversi tinggi dari sentimeter ke meter menggunakan operator pembagian
tinggi_m = tinggi_cm / 100

# Rumus BMI = Berat / (Tinggi dalam meter ** 2)
bmi = berat / (tinggi_m ** 2)

print("\n--- Hasil Perhitungan BMI ---")
print(f"Nama          : {nama}")
print(f"NIM           : {nim}")
print(f"Berat Badan   : {berat} kg")
print(f"Tinggi Badan  : {tinggi_cm} cm ({round(tinggi_m, 2)} m)")
print(f"Nilai BMI     : {round(bmi, 2)}")

# =========================================================
# BAGIAN 2: KASIR
# =========================================================
print("\n=== BAGIAN 2: KASIR ===")

nama_barang1 = input("Masukkan nama barang 1: ")
harga_barang1 = float(input(f"Masukkan harga {nama_barang1}: "))

nama_barang2 = input("Masukkan nama barang 2: ")
harga_barang2 = float(input(f"Masukkan harga {nama_barang2}: "))

# Hitung subtotal
subtotal = harga_barang1 + harga_barang2

# Hitung diskon 5% dari subtotal
diskon = 0.05 * subtotal

# Harga setelah diskon
harga_setelah_diskon = subtotal - diskon

# Hitung pajak 11% dari harga setelah diskon
pajak = 0.11 * harga_setelah_diskon

# Total bayar keseluruhan
total_bayar = harga_setelah_diskon + pajak

print("\n--- Struk Belanja ---")
print(f"{nama_barang1:<15}: Rp{round(harga_barang1, 2)}")
print(f"{nama_barang2:<15}: Rp{round(harga_barang2, 2)}")
print("-" * 30)
print(f"Subtotal        : Rp{round(subtotal, 2)}")
print(f"Diskon (5%)     : Rp{round(diskon, 2)}")
print(f"Setelah Diskon  : Rp{round(harga_setelah_diskon, 2)}")
print(f"Pajak (11%)     : Rp{round(pajak, 2)}")
print("-" * 30)
print(f"TOTAL BAYAR     : Rp{round(total_bayar, 2)}")