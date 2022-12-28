'''1.Sebuah wahana bermain 'Disney Island' akan memberikan tarif sesuai dengan tinggi dan umur anak dengan ketentuan sebagai berikut:
Umur kurang dari 2 tahun: Tampilkan 'Dilarang masuk'
Umur kurang dari 4 tahun: Rp 30.000. Jika tinggi anak umur 2-3 tahun melebihi 70 cm maka tarif akan bertambah 10.000
Umur kurang dari 7 tahun: Rp 40.000. Jika tinggi anak umur 4-6 tahun melebih 120 cm maka tarif akan bertambah 15.000
Umur kurang dari 10 tahun: Rp 50.000. Jika tinggi anak umur 8-9 tahun melebih 150 cm maka tarif akan bertambah 20.000
Umur 10 tahun keatas: Rp 80.000
Buatlah program untuk menampilkan tarif harga sesuai umur dan tinggi seorang anak!
'''

umur = int(input('Masukan umur = '))

if umur <= 2 :
    print ('dilarang masuk')

elif umur <= 4 :
    tinggi_badan = int(input('Masukan tinggi badan = '))
    harga = 30000
    if tinggi_badan >= 70:
        print("total bayar kamu Rp.",harga + 10000)
    else:
        print("total bayar kamu",harga)

elif umur <= 7 :
    tinggi_badan = int(input('Masukan tinggi badan = '))
    harga = 40000
    if tinggi_badan >= 120:
        print("total bayar kamu Rp.",harga + 15000)
    else:
        print("total bayar kamu",harga)

elif umur <= 10 :
    tinggi_badan = int(input('Masukan tinggi badan = '))
    harga = 40000
    if tinggi_badan >= 150:
        print("total bayar kamu Rp.",harga + 20000)
    else:
        print("total bayar kamu",harga)

else:
    harga = 80000
    print("total bayar kamu",harga)


'''2.Terdapat sebuah jurnal yang menuliskan teorinya bahwa olahraga dapat membakar kalori yang terkandung dalam tubuh manusia. Hal tersebut berbanding lurus dengan lama waktu yang dilakukan. Berikut ini adalah beberapa teori tersebut:
Olahraga lari membakar 60 kalori setiap 5 menit.
Olahraga push-up membakar 200 kalori setiap 30 menit
Olahraga plank membakar 5 kalori selama 1 menit
Buatlah program berdasarkan uraian tersebut untuk menghitung berapa jumlah kalori yang terbakar setelah melakukan aktivitas olahraga tersebut dengan ketentuan setiap orang boleh melakukan aktivitasnya lebih dari 1 (satu).
'''

print('''
      1. push_up
      2. lari
      3. plank
      4. push_up dan lari
      5. push_up dan plank
      6. push_up,lari, dan plank
      7. lari dan plank 
      ''')

olahraga_apa = input('olah raga apa ?')
menit = float(input('masukan berapa menit olahraga = '))
lari = 12
push_up = 6.6
plank = 5


if olahraga_apa == '1':
    TotalBakarKalori = push_up * menit
    print(f'total kalori yang di dapat adalah {TotalBakarKalori} kalori')

elif olahraga_apa == '2':
    TotalBakarKalori = lari * menit
    print(f'total kalori yang di dapat adalah {TotalBakarKalori} kalori')

elif olahraga_apa == '3':
    TotalBakarKalori = plank * menit
    print(f'total kalori yang di dapat adalah {TotalBakarKalori} kalori')

elif olahraga_apa == '4': 
    TotalBakarKalori = (push_up + lari ) * menit
    print(f'total kalori yang di dapat adalah {TotalBakarKalori} kalori')

elif olahraga_apa == '5':
    TotalBakarKalori = (push_up + plank ) * menit
    print(f'total kalori yang di dapat adalah {TotalBakarKalori} kalori')

elif olahraga_apa == '6':
    TotalBakarKalori = (push_up + plank + lari) * menit
    print(f'total kalori yang di dapat adalah {TotalBakarKalori} kalori') 

elif olahraga_apa == '7':
    TotalBakarKalori = (lari + plank) * menit
    print(f'total kalori yang di dapat adalah {TotalBakarKalori} kalori')

else:
    print('masukan menu yang valid')