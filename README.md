# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Farid Ardiansah  
**NIM:** 2225250125  
**Kelas:** 3E

## Tujuan

Mempelajari cara membaca, memvalidasi, mengolah, dan menulis data file menggunakan Python. Selain itu, memahami penggunaan error handling untuk menangani kesalahan agar program tetap berjalan dengan baik.

## Format File Input

Program menggunakan file `data/nilai.txt` dengan format:

```text
NIM,nilai
```

Contoh isi file:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Setiap baris berisi NIM dan nilai mahasiswa yang dipisahkan dengan tanda koma. Data yang tidak valid akan dilewati agar tidak mengganggu proses perhitungan.

## Cara Menjalankan

1. Buka folder proyek Pertemuan 12 di VS Code.
2. Pastikan file `data/nilai.txt` tersedia.
3. Buka terminal dan jalankan perintah:

```bash
python3 tugas/rekap_nilai_file.py
```

4. Program akan membaca data, melakukan validasi, menghitung statistik nilai, dan menyimpan hasil ke `data/hasil_rekap.txt`.

## Error yang Ditangani

1. **FileNotFoundError:** Terjadi ketika file `nilai.txt` tidak ditemukan. Program akan menampilkan pesan "File tidak ditemukan." tanpa mengalami crash.

2. **ValueError:** Terjadi ketika nilai tidak dapat dikonversi menjadi angka, misalnya `A004,abc`. Program akan melewati baris tersebut dan melanjutkan proses data lainnya.

## Test Case

| No | Kondisi | Hasil yang Diharapkan | Hasil Aktual (Contoh) | Status |
|---|---|---|---|---|
| 1 | Semua baris valid | Seluruh data diproses | Seluruh data valid diproses | Berhasil |
| 2 | File tidak ditemukan | Muncul pesan kesalahan | File tidak ditemukan | Berhasil |
| 3 | Nilai invalid A004,abc | Baris invalid dilewati | Baris 4 dilewati | Berhasil |
| 4 | Terdapat baris kosong | Baris kosong dilewati | Baris kosong tidak diproses | Berhasil |
| 5 | Nilai mahasiswa 60 | Dihitung sebagai lulus | Nilai 60 termasuk
