# Latihan 1: Menulis File
# Pertemuan 12

import os

# Membuat folder data jika belum ada
os.makedirs("data", exist_ok=True)

# Menulis file
with open("data/catatan.txt", "w", encoding="utf-8") as file:
    file.write("Algoritma dan Pemrograman\n")
    file.write("Pertemuan 12\n")