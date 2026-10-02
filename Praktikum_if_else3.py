print("=" * 50)
print("       PRAKTIKUM 3: IF, ELIF, DAN ELSE")
print("=" * 50)

#----------------------------------------------------------
print("\n--- LATIHAN 3: PENDEKATAN IF-ELIF-ELSE ---")
print("[!] Mengecek grade nilai DENGAN menggunakan elif")
nilai = float(input("Masukkan nilai akhir Anda (0-100): "))

# Memanfaatkan variabel 'nilai' dari input Latihan 2
if nilai >= 80:
    print("Evaluasi Elif: Grade A (Lulus)")
elif nilai >= 70:
    print("Evaluasi Elif: Grade B (Lulus)")
elif nilai >= 60:
    print("Evaluasi Elif: Grade C (Lulus)")
elif nilai >= 50:
    print("Evaluasi Elif: Grade D (Tidak Lulus)")
else:
    print("Evaluasi Elif: Grade E (Tidak Lulus)")