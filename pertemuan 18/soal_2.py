"""
Latihan 2: Class RekeningBank
Buatlah sebuah class bernama RekeningBank untuk mensimulasikan rekening bank sederhana.
1. Buat constructor __init__() yang menerima dua parameter: nomor_rekening dan
   nama_pemilik. Ia juga harus menginisialisasi atribut self.saldo dengan nilai awal 0.
2. Buat method lihat_saldo() yang mencetak saldo saat ini.
3. Buat method setor(jumlah) yang menambahkan jumlah ke self.saldo dan mencetak pesan
   konfirmasi.
4. Buat method tarik(jumlah) yang mengurangi jumlah dari self.saldo. Tambahkan logika if di
   dalamnya: jika jumlah yang ditarik lebih besar dari saldo, cetak pesan "Saldo tidak mencukupi" dan
   jangan ubah saldo. Jika tidak, kurangi saldo dan cetak pesan konfirmasi.
5. Buat sebuah objek rekening_budi, lalu coba panggil semua method-nya: setor beberapa kali, tarik,
   dan lihat saldo.
"""

class RekeningBank:
   def __init__(self, nomor_rekening, nama_pemilik):
      self.saldo = 0
        
   def lihat_saldo(self):
      print(f"saldo sekarang: {self.saldo}")   
        
   def setor(self, jumlah):
      self.saldo += jumlah
      print(f"saldo setor: {jumlah:,}")
    
   def tarik(self, jumlah):
      print(f"proses penarikan sebesar {jumlah:,} ...")
      if self.saldo < jumlah:
         print("Mon mangap, masih bokek jangan mimpi")
      else:
         self.saldo -= jumlah
         print(f"saldo ditarik: {jumlah:,}") 
        
Rekening_Pepeng= RekeningBank(344432, "Pepeng Gepeng")
Rekening_Pepeng.lihat_saldo()
Rekening_Pepeng.setor(10000)
Rekening_Pepeng.tarik(10000)