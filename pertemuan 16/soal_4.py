"""
Latihan 4: Frekuensi Hari
Tulis program yang membaca file mbox-short.txt. Bangun histogram menggunakan 
dictionary untuk menghitung berapa banyak pesan yang dikirim pada setiap 
hari dalam seminggu. (Lihat baris yang dimulai dengan "From ", kata 
ketiganya adalah hari). Cetak dictionary hasilnya.
"""

with open("mbox-short.txt") as file:
    histogram = {}

    for baris in file:

        if baris.startswith("From "):
            kata = baris.split()
            hari = kata[2]  
            histogram[hari] = histogram.get(hari, 0) + 1

print(histogram)
