"""
Latihan 3: re.search() vs. re.findall()
Diberikan string teks = "python adalah bahasa yang menyenangkan, python mudah
dipelajari.".
1. Gunakan re.search('python', teks). Apa yang dikembalikannya? Cetak .group()-nya.
2. Gunakan re.findall('python', teks). Apa yang dikembalikannya? Cetak hasilnya.
3. Jelaskan perbedaan output keduanya.
"""
import re

teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

match = re.search('python', teks)
piton = re.findall('python', teks)

print(match) # span = nyari indeksnya, match = ada apa engga si 'python-nya'
print(match.group()) # nampilin isinya which is 'pyhton'
print(piton) # nampilin list python, berapapun jumlahnya