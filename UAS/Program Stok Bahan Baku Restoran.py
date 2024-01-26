# Program Database Stok Bahan Baku Restoran

# Inisialisasi database stok bahan baku
stok_bahan_baku = {}

# Fungsi untuk menampilkan stok bahan baku
def tampilkan_stok():
    print("Stok Bahan Baku:")
    for bahan, jumlah in stok_bahan_baku.items():
        print(f"{bahan}: {jumlah} unit")

# Fungsi untuk menambahkan stok bahan baku
def tambah_stok(bahan, jumlah):
    if bahan in stok_bahan_baku:
        stok_bahan_baku[bahan] += jumlah
    else:
        stok_bahan_baku[bahan] = jumlah
    print(f"{jumlah} unit {bahan} berhasil ditambahkan.")

# Fungsi untuk mengupdate stok bahan baku
def update_stok(bahan, jumlah):
    if bahan in stok_bahan_baku:
        stok_bahan_baku[bahan] = jumlah
        print(f"Stok {bahan} berhasil diupdate menjadi {jumlah} unit.")
    else:
        print(f"{bahan} tidak ditemukan dalam stok.")

# Memulai program
while True:
    print("\nMenu:")
    print("1. Tampilkan Stok")
    print("2. Tambah Stok")
    print("3. Update Stok")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        tampilkan_stok()
    elif pilihan == "2":
        bahan = input("Masukkan nama bahan baku: ")
        jumlah = int(input("Masukkan jumlah yang ingin ditambahkan: "))
        tambah_stok(bahan, jumlah)
    elif pilihan == "3":
        bahan = input("Masukkan nama bahan baku yang ingin diupdate: ")
        jumlah = int(input("Masukkan jumlah baru: "))
        update_stok(bahan, jumlah)
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
