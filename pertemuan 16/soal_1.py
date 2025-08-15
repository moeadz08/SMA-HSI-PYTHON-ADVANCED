"""
Latihan 1: Iterasi dan Kalkulasi
Diberikan dictionary harga buah: harga_buah = {"apel": 5000, "jeruk": 8500, 
"mangga": 7800, "pisang": 3000}.
Gunakan for loop dan .items() untuk mencetak setiap buah dan harganya dalam 
format "Harga 1 kg [nama buah] adalah Rp [harga]". Di akhir, hitung 
dan cetak total harga semua buah.
"""

# make items
harga_item = {
    "bawang": 4000, 
    "ubi": 5000, 
    "daun": 100000
}

total_harga = 0

for item, harga in harga_item.items():
    print(f"Harga 1 kg {item} adalah Rp {harga:,}")
    total_harga += harga

print(f"Jadi, total semua item adalah Rp {total_harga:,}")
