"""
Latihan 2: Immutability
Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple 
baru bernama koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah 
koordinat_awal secara langsung.
"""

nomer_awal = (10,20,30,40)
nomer_baru = nomer_awal[0:1] + (25,) + nomer_awal[2:]
print(nomer_baru)