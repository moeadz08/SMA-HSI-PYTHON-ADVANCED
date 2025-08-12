"""
Latihan 3: Traversing dan Modifikasi
1. Buat sebuah list berisi angka: nilai_mentah = [55, 63, 72, 81, 90].
2. Buatlah sebuah for loop yang menggunakan range(len(nilai_mentah)) untuk mengunjungi
   setiap elemen.
3. Di dalam loop, tambahkan 5 poin ke setiap nilai sebagai "nilai bonus".
4. Setelah loop selesai, cetak list nilai_mentah yang sudah berisi nilai-nilai baru.
"""

nilai_mentah = [55, 63, 72, 81, 90] 
print('Nilai asal:',nilai_mentah)
for i in range(len(nilai_mentah)):
    print(f'\nMenambahkan 5 poin di index {i}...')
    nilai_mentah [i] += 5
    print('Setelah ditambah 5:',nilai_mentah)