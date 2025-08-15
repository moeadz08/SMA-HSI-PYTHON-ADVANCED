"""
Latihan 3: Penggunaan .get()
1. Masih dengan dictionary biodata.
2. Coba akses key "pekerjaan" menggunakan bracket notation [].
   Apa yang terjadi? (Beri komentar pada baris ini agar tidak error).
3. Sekarang, akses key "pekerjaan" menggunakan metode .get(). Cetak hasilnya.
4. Akses lagi key "pekerjaan" menggunakan .get(), tapi kali ini berikan 
   nilai default "Pelajar". Cetak hasilnya.
"""

biodata = {
    "nama": "Mu'adz Jundyurrahman",
    "umur": 17,
    "hobi": ['Mancing', 'Ngaji', 'Lari'],
    "sudah_menikah": False
}

print(biodata.get("pekerjaan"))

print(biodata.get("pekerjaan", "Pelajar"))