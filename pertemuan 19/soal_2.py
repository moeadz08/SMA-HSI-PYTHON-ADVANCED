"""
Latihan 2: Validasi Nomor Telepon Sederhana
Buat program yang meminta pengguna memasukkan nomor telepon. Program harus 
memvalidasi apakah input tersebut hanya berisi angka dan panjangnya antara 
10 sampai 13 digit.Gunakan re.search() dengan jangkar ^ dan $.
Gunakan quantifier + atau yang lebih spesifik.
Cetak "Format nomor telepon valid." atau "Format tidak valid."
Pola yang mungkin: ^\d+$ (ini hanya mengecek apakah semuanya digit, kamu 
perlu menambahkan pengecekan panjang dengan len()).
"""

import re

nomor = (input("masukkan nomor telepon: "))
pola = r'^\d{10,13}$'

match = re.search(pola, nomor)
if match:
    print("Format valid!")
    print("Objek Match:", match)
    print(f"Substring yang cocok: {match.group()}")
    print(f"Ditemukan di indeks: {match.start()} sampai {match.end()}")
elif len(nomor) < 10:
    print("kurang panjang!")
elif len(nomor) > 13:
    print("kurang pendek!")
else:
    print("Format invalid!")