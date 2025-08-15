"""
Latihan 1: Membuat dan Mengakses
1. Buat sebuah dictionary bernama biodata untuk merepresentasikan dirimu. 
   Isinya harus memiliki key: "nama", "umur", "hobi" 
   (hobi bisa berupa list dari beberapa string), dan "sudah_menikah" (berisi boolean).
2. Cetak seluruh dictionary.
3. Cetak hanya value dari key "nama".
4. Cetak hobi pertamamu dari list hobi.
"""

biodata = {
    "nama": "Mu'adz Jundyurrahman",
    "umur": 17,
    "hobi": ['Mancing','Ngaji','Lari'],
    "sudah_menikah": True
}

print(biodata)
nama_gue = biodata["nama"]
print(f"Nama saiya adalah: {nama_gue}")

hobi_gue = biodata["hobi"]
print(f"Hobi pertama saiya: {hobi_gue[0]}")