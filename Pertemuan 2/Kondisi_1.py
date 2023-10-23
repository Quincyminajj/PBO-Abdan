# Daftar Sepatu Dan Harga
daftar_Sepatu = {
    "Airmax 95 OG": 550.0000, 
    "Airmax TN Plus": 995.0000,
    "Nike Cortez Black Gum": 840.0000,
    "Nike SB Dunk Low Pro":790.0000,


}

# Menampilkan daftar sepatu yang tersedia
print("Daftar Sepatu Yang Tersedia")
for Sepatu, harga in daftar_Sepatu.items():
    print(f"{Sepatu}: Rp {harga:,.0f}")

#inisialisasi Variabel Total Harga
total_harga = 0

# Input dari pengguna untuk memilih sepatu
while True:
    pilihan = input ("pilih sepatu yang ingin di beli(Ketik 'selesai' untuk mengakhiri pembelian)")

    if pilihan.lower() == "selesai":
        break
    if pilihan in daftar_Sepatu:
        harga_sepatu = daftar_Sepatu[pilihan]
        total_harga += harga_sepatu
        print(f"{pilihan}Ditambahkan ke keranjang belanja.")
    else:
        print("sepatu tidak valid. silahkan pilih sepatu yang tersedia")

# menampilkan total harga
print(f"Total harga pembelian: Rp {total_harga:,.0f}")


#Terimakasih Telah berbelanja