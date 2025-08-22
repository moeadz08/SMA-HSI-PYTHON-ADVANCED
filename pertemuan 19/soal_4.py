"""Latihan 4: Menemukan Kata dengan Pola
Diberikan kalimat: kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan.".
Gunakan re.findall() untuk menemukan semua kata yang diakhiri dengan huruf 'g'.
"""

import re

kalimat = "Anda, Anda, dan Anda adalah very good pet of mine"

pola_akhir = r'a$'
semua_kata = re.findall(r'\w+a\b', kalimat)
print(f"Semua kata yang ditemukan: '{semua_kata}")