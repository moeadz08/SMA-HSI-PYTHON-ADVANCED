"""
Latihan 2: Manajemen Kontak
Buat program manajemen kontak sederhana:
1. Buat dictionary kosong bernama kontak.
2. Tambahkan tiga kontak (misal: "Ibu", "Ayah", "Teman") beserta nomor teleponnya.
3. Ubah nomor telepon "Ibu".
4. Gunakan .pop() untuk menghapus "Teman".
5. Cetak dictionary kontak akhir
"""

kontak = {}

kontak["Nenek"] = 628888880000
kontak["Cucu"] = 628000000888
kontak["Paman"] = 628000000000

kontak["Cucu"] = 447129800987

kontak.pop("Paman")

for nama, nomor in kontak.items():
    print(f"{nama}: {nomor:}")