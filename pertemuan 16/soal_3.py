"""
Latihan 3: Nested Dictionary
Buatlah sebuah nested dictionary untuk menyimpan data dua produk di sebuah toko online.
• Key utamanya adalah ID produk (misal: "PROD001", "PROD002").
• Setiap produk harus memiliki key untuk "nama", "harga", dan "stok".
  Setelah membuatnya, tulis kode untuk mencetak nama dan harga dari produk dengan ID "PROD002".
"""

item = {
    "ITEM001": {
        "nama": "Lamborghini",
        "harga": 7500000000000,
        "stok": 5
    },
    "ITEM002": {
        "nama": "Yacht",
        "harga": 3500000000,
        "stok": 10
    }
}

for data in item.values():
    print(f"Nama: {data['nama']}")
    print(f"Harga: Rp {data['harga']:,}")