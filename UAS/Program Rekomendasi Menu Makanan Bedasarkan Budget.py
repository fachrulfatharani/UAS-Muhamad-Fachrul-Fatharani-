#Rekomendasi Paket makanan Bedasarkan budget

print('=================================================================')
print('==     Selamat datang di Restoran Kami!                        ==')
print('==     Bingung mau makan apa?                                  ==')
print('==     pengen yang sesuai budget?                              ==')
print('==     tuliskan budget mu di bawah, biar kami yang beri saran! ==')
print('=================================================================')

#menentukan budget yang di bawa untuk makan

budget = int(input('Rp :'))

#jika budget di atas Rp. 100.000

if budget > 100000:    
    print('oops! Budget kamu kebesaran.. cukup seratus ribu kebawah aja ya :)')

#jika budget di bawah atau sama dengan Rp. W

elif budget >= 80000:
    print('1. Paket Ayam betutu')
    print('2. Paket Udang bakar')
    print('3. Paket Kepiting Racaca')
    print('Silahkan di pilih! :)')

#jika budget di bawah atau sama dengan Rp. 60.000

elif budget >= 60000:
    print('1. Paket Cumi Goreng tepung')
    print('2. Paket Udang Bakar')
    print('3. Paket kerang Bale')

#jika budget di bawah atau sama dengan Rp. 40.000

elif budget >= 40000:
    print('1. Paket Ayam Bakar Madu')
    print('2. Paket Lele Bakar Madura')
    print('3. Paket Kerang Asam Manis')

#jika budget di bawah atau sama dengan Rp. 20.000

elif budget >= 20000:
    print('1. Paket Ca Sayuran')
    print('2. Paket Capcay seafood')
    print('3. Paket Soto')

#jika budget di bawah atau sama dengan Rp. 10.000

elif budget >= 10000:
    print('1. Paket Sayur Asem')
    print('2. Paket Cah kangkung')
    print('3. Paket Sayur Sop')

#jika budget di bawah Rp. 10.000

else:
    print('Yah.. Budget kamu masih kurang untuk menu kita :(')