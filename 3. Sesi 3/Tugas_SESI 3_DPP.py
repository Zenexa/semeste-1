print('''1. Tipe data Python yang pertama adalah integer. Sesuai namanya, integer digunakan untuk
memasukkan nilai bilangan bulat.
Tipe data Python yang selanjutnya adalah float. Kebalikan dari integer, float khusus
digunakan untuk menampung nilai bilangan desimal.
String adalah tipe data Python untuk menampung nilai teks, seperti huruf, tanda baca, dan
karakter spesial lainnya. Ciri-ciri tipe data string adalah diapit tanda petik, baik itu petik satu
('') atau petik dua ("").
Boolean adalah tipe data Python yang hanya bisa diisi oleh dua nilai,
yaitu True dan False. Untuk menulis isian boolean, ada dua aturan yang harus dipatuhi. Yaitu,
pakai kapital untuk huruf pertama dan tanpa tanda petik sama sekali.
Selain tipe data standar, Python juga sebenarnya menyediakan tipe data khusus, yaitu
bilangan kompleks. Tipe data Python yang satu ini bisa Anda manfaatkan untuk
memudahkan perhitungan matematika.''')

#contoh type type data
integer = 10
flo = 10.5
string = 'zenuar'
bol = False

print ('type datanya adalah',type(integer)) 
print ('type datanya adalah',type(flo))
print ('type datanya adalah',type(string))
print ('type datanya adalah',type(bol))


print('2.')

#Khaisa Zenuar
#20220040062
#08952382382


print('3.')
angka_pertama = 5000
angka_kedua = 2000
angka_ketiga = 200

tambah = angka_pertama + 500
tambah2 = angka_kedua + 500
hasil = (tambah + tambah2) - angka_ketiga
print(hasil)


print('4')
print ("Program Keliling lingkaran")
jari_jari = int(input('jari jari'))
k = 2 * (22/7) * 14
print('jari jarinya adalah ',k)

print ("Program Perhitungan Volume Kubus")
sisi = float(input("Masukkan Sisi : "))
hasil = sisi+sisi+sisi
print("Volume Kubus adalah : ",hasil)