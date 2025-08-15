"""
Latihan 4: Histogram Kata
Buat program yang:
1. Meminta pengguna memasukkan sebuah kalimat.
2. Membuat histogram (dalam bentuk dictionary) yang menghitung frekuensi 
   setiap kata (bukan huruf) dalam kalimat tersebut.
3. Cetak dictionary histogram tersebut.
   Petunjuk: Gunakan metode .split() untuk mengubah kalimat menjadi list
   kata-kata terlebih dahulu. Abaikan huruf besar/kecil dengan mengubah 
   seluruh kalimat menjadi lowercase di awal
"""

kalimat = input("kalimat apa aja: ")

baris_bersih = kalimat.replace(",", "").replace(".", "").lower()
kata_kata = baris_bersih.split()
kata_list = kalimat.lower().split()

histogram = {}

for kata in kata_list:
    histogram[kata] = histogram.get(kata, 0) + 1

print(histogram)