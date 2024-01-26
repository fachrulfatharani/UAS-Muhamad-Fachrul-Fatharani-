# Program Manajemen Daftar Orang

# Inisialisasi daftar orang
daftar_orang = []

# Fungsi untuk menampilkan daftar orang
def tampilkan_daftar():
    print("Daftar Orang:")
    for orang in daftar_orang:
        print(f"Nama: {orang['nama']}, Usia: {orang['usia']}, Alamat: {orang['alamat']}")

# Fungsi untuk menambahkan orang baru
def tambah_orang(nama, usia, alamat):
    orang_baru = {'nama': nama, 'usia': usia, 'alamat': alamat}
    daftar_orang.append(orang_baru)
    print(f"{nama} berhasil ditambahkan ke daftar.")

# Fungsi untuk menghapus orang dari daftar
def hapus_orang(nama):
    for orang in daftar_orang:
        if orang['nama'] == nama:
            daftar_orang.remove(orang)
            print(f"{nama} berhasil dihapus dari daftar.")
            return
    print(f"{nama} tidak ditemukan dalam daftar.")

# Memulai program
while True:
    print("\nMenu:")
    print("1. Tampilkan Daftar")
    print("2. Tambah Orang")
    print("3. Hapus Orang")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        tampilkan_daftar()
    elif pilihan == "2":
        nama = input("Masukkan nama: ")
        usia = int(input("Masukkan usia: "))
        alamat = input("Masukkan alamat: ")
        tambah_orang(nama, usia, alamat)
    elif pilihan == "3":
        nama = input("Masukkan nama orang yang ingin dihapus: ")
        hapus_orang(nama)
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
