# Latihan 5: File Tidak Ditemukan
# Pertemuan 12

try:
    with open("data/tidak_ada.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("File tidak ditemukan.")