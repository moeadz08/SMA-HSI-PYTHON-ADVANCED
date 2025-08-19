"""
Latihan 4: Dictionary dengan Tuple Key
Buatlah sebuah dictionary bernama papan_catur. Gunakan tuple (baris, kolom) sebagai key
untuk menyimpan nama bidak catur. Contoh:
• papan_catur[(1, 'a')] = "Benteng Putih"
• papan_catur[(8, 'h')] = "Benteng Hitam"
Isi beberapa posisi, lalu akses dan cetak bidak yang ada di posisi (1, 'a').
"""

papan_cetar = {}

papan_cetar[(2, "b")] = "pensil"
papan_cetar[(1, "k")] = "seribu"
papan_cetar[(9, "ten")] = "sepatu"

print(papan_cetar[(2, "b")])