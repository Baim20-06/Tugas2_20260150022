#----------------------------------------------------------------
print("\n--- LATIHAN 4: NESTED IF & OPERATION LOGIKA ---")
print("[!] Simulasi Penentuan Predikat Kelulusan Cumlaude")

ipk = float(input("Masukkan IPK total Anda (0.00-4.00): "))
masa_studi = int(input("Masa studi Anda (dalam semester): "))

# Menggunakan operator 'and' (kedua syarat harus True)
if ipk >= 3.51 and masa_studi <= 8:
    print("-> Syarat dasar Cumlaude terpenuhi.")

    # Nested IF (Pengecekan lanjutan di dalam blok True)
    if nilai_d == "tidak":
        print("STATUS AKHIR: LULUS DENGAN PUJIAN (Cumlaude)!")
    else:
        print("STATUS AKHIR: LULUS SANGAT MEMUASKAN (Gagal Cumlaude karena nilai 0)")

else:
    print("STATUS AKHIR: LULUS BIASA (Tidak memenuhi standar IPK/Masa Studi")

print("\n" + "=" * 50)