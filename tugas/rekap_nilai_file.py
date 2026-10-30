
# Tugas 5: Rekap Nilai dari File
# Pertemuan 12 - Algoritma dan Pemrograman

import os

# Fungsi membaca dan memvalidasi data
def baca_data(nama_file):
    data_valid = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(f"Baris {nomor}: Format tidak valid")
                    continue

                nim = bagian[0].strip()
                teks_nilai = bagian[1].strip()

                if not nim:
                    print(f"Baris {nomor}: NIM kosong")
                    continue

                try:
                    nilai = float(teks_nilai)

                    if not (0 <= nilai <= 100):
                        print(f"Baris {nomor}: Nilai di luar 0-100")
                        continue

                    data_valid.append({
                        "nim": nim,
                        "nilai": nilai
                    })

                except ValueError:
                    print(f"Baris {nomor}: Nilai tidak valid")

    except FileNotFoundError:
        print("File tidak ditemukan.")
        return None

    return data_valid


# Fungsi menulis hasil rekap
def tulis_rekap(nama_file, data):
    jumlah = len(data)

    if jumlah == 0:
        hasil = "Tidak ada data valid."
    else:
        daftar_nilai = [m["nilai"] for m in data]

        rata_rata = sum(daftar_nilai) / jumlah
        minimum = min(daftar_nilai)
        maksimum = max(daftar_nilai)
        lulus = sum(1 for nilai in daftar_nilai if nilai >= 60)

        hasil = (
            "=== HASIL REKAP NILAI ===\n"
            f"Jumlah data valid : {jumlah}\n"
            f"Rata-rata nilai   : {rata_rata:.2f}\n"
            f"Nilai minimum     : {minimum:.2f}\n"
            f"Nilai maksimum    : {maksimum:.2f}\n"
            f"Jumlah lulus      : {lulus}\n"
        )

    os.makedirs(os.path.dirname(nama_file), exist_ok=True)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(hasil)

    print("\n" + hasil)
    print("Hasil rekap berhasil disimpan.")


# Program utama
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data is not None:
    tulis_rekap(output_file, data)
