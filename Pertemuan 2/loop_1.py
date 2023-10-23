# Inisialisasi data penjualan sepatu
data_penjualan = []

while True:
    print("\nAplikasi Manajemen Penjualan Sepatu")
    print("1. Tambah Penjualan")
    print("2. Tampilkan Penjualan")
    print("3. Keluar")
    pilihan = input("Pilih operasi (1/2/3): ")

    if pilihan == '1':
        nama_pembeli = input("Masukkan nama pembeli: ")
        model_sepatu = input("Masukkan model sepatu: ")
        harga = input("Masukkan harga sepatu: ")

        # Membuat entri penjualan dalam bentuk string
        penjualan = f"Nama Pembeli: {nama_pembeli}, Model Sepatu: {model_sepatu}, Harga: {harga}"

        # Menambahkan entri penjualan ke dalam list data_penjualan
        data_penjualan.append(penjualan)
        print("Data penjualan telah ditambahkan.")
    elif pilihan == '2':
        if not data_penjualan:
            print("Belum ada data penjualan.")
        else:
            print("Data Penjualan Sepatu:")
            for i, penjualan in enumerate(data_penjualan, 1):
                print(f"{i}. {penjualan}")
    elif pilihan == '3':
        print("Thanks for your order!.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
  