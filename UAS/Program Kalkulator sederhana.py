# Program kalkulator sederhana

# Fungsi untuk penjumlahan

def tambah(a, b):
    return a + b

# Fungsi untuk pengurangan

def kurang(a, b):
    return a - b

# Fungsi untuk perkalian

def kali(a, b):
    return a * b

# Fungsi untuk pembagian

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol tidak diizinkan."

# Menampilkan menu operasi kalkulator
    
print("Kalkulator Sederhana")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta pengguna memilih operasi

pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

# Meminta pengguna memasukkan dua angka

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Memilih operasi berdasarkan pilihan pengguna

if pilihan == "1":
    hasil = tambah(angka1, angka2)
    operasi = "Penjumlahan"
elif pilihan == "2":
    hasil = kurang(angka1, angka2)
    operasi = "Pengurangan"
elif pilihan == "3":
    hasil = kali(angka1, angka2)
    operasi = "Perkalian"
elif pilihan == "4":
    hasil = bagi(angka1, angka2)
    operasi = "Pembagian"
else:
    hasil = "Error: Pilihan operasi tidak valid."
    operasi = ""

# Menampilkan hasil operasi
    
if operasi:
    print(f"Hasil {operasi}: {hasil}")
else:
    print(hasil)
