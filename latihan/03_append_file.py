# Latihan 3: Append File
# Pertemuan 12

with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write("Latihan append berhasil.\n")