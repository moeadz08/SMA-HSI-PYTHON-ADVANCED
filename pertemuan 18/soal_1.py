"""
Latihan 1: Class Kucing
1. Buatlah sebuah class bernama Kucing.
2. Buat constructor __init__() yang menerima dua parameter: nama dan warna. 
   Constructor ini harus menyimpan nilai-nilai tersebut ke dalam atribut self.nama dan self.warna.
3. Buat sebuah method bernama bersuara() yang tidak memiliki parameter (selain self). 
   Ketika dipanggil, method ini harus mencetak "Meow!".
4. Buat sebuah method bernama perkenalkan_diri() yang mencetak kalimat seperti 
   "Halo, saya kucing bernama [nama] dan warna saya [warna].".
5. Buat dua object (instance) dari class Kucing dengan nama dan warna yang berbeda 
   (misal, "Oren" berwarna "Oranye" dan "Milo" berwarna "Coklat").
6. Panggil method perkenalkan_diri() dan bersuara() dari kedua objek tersebut.
"""

class Gorilla:
   def __init__(self, nama, warna):
      self.nama = nama
      self.warna = warna
        
# Method untuk menambah kecepatan
   def bersuara(self):
      if self.bersuara:
         print("RAWRR!")     
               
   def perkenalkan_diri(self):
      print(f"Hai, Saya {self.nama}, Saya bangga memiliki warna {self.warna}")


mutant_1 = Gorilla("andi", "warni")

mutant_1.perkenalkan_diri()
mutant_1.bersuara()

mutant_2 = Gorilla("ando", "blek")

mutant_2.perkenalkan_diri()
mutant_2.bersuara()