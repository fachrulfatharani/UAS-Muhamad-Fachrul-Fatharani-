print('===============================')
print('=permainan gunting kertas batu=')
print('===============================')

# Fungsi untuk menentukan pemenang
def tentukan_pemenang(pilihan_pengguna, pilihan_komputer):
    if pilihan_pengguna == pilihan_komputer:
        return "Seri"
    elif (
        (pilihan_pengguna == "batu" and pilihan_komputer == "gunting") or
        (pilihan_pengguna == "gunting" and pilihan_komputer == "kertas") or
        (pilihan_pengguna == "kertas" and pilihan_komputer == "batu")
    ):
        return "selamat Anda Menang"
    else:
        return "yahh kamu kalah"

# Meminta pengguna memilih batu, gunting, atau kertas
    
pilihan_pengguna = input("Pilih batu, gunting, atau kertas: ").lower()

# Komputer secara acak memilih batu, gunting, atau kertas

import random
pilihan_komputer = random.choice(["batu", "gunting", "kertas"])

# Menampilkan hasil permainan

print(f"kamu memilih {pilihan_pengguna}")
print(f"Komputer memilih {pilihan_komputer}")
print(tentukan_pemenang(pilihan_pengguna, pilihan_komputer))
