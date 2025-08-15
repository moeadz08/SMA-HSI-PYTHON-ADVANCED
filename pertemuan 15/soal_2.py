"""
Latihan 2: Modifikasi Dictionary
1. Gunakan dictionary biodata dari Latihan 1.
2. Tambahkan pasangan key-value baru: "kota": "Nama Kotamu".
3. Ubah value dari key "umur" menjadi umurmu tahun depan.
4. Cetak dictionary yang sudah diperbarui.
"""

biodata = {
    "nama": "Mu'adz Jundyurrahman",
    "umur": 17,
    "hobi": ['Mancing','Ngaji','Lari'],
    "sudah_menikah": True
}

# menambahkan key-value baru
biodata["kota"] = "Cirebon"
# mengganti key-value
biodata["umur"] = 18
print("Profil setelah ditambah:", biodata)