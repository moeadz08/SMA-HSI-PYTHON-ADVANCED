"""
Latihan 3: Analisis Kata
Buat program yang:
1. Meminta pengguna memasukkan sebuah kalimat.
2. Gunakan .split() untuk mengubah kalimat tersebut menjadi sebuah list kata-kata.
3. Gunakan len() untuk menghitung dan mencetak jumlah kata dalam kalimat.
4. Gunakan .sort() pada list tersebut untuk mengurutkan kata-kata berdasarkan abjad, lalu cetak
list yang sudah terurut.
"""

bebas = input('What do You think? ')
bebas = bebas.split()
print(len(bebas))
bebas.sort()
print('Arranged well:', bebas)