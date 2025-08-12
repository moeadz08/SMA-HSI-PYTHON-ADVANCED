nilai_mentah = [55, 63, 72, 81, 90]
print('Nilai asal:',nilai_mentah)
for i in range(len(nilai_mentah)):
    print(f'\nMenambahkan 5 poin di index {i}...')
    nilai_mentah [i] += 5
    print('Setelah ditambah 5:',nilai_mentah)