
#1.Buatlah biodata sederhana dengan menggunakan fungsi input(), dan output variabel dengan fungsi format().
nama= input('Nama: ')
kelas= input('Kelas: ')
NIM= int(input('NIM: '))
tmpt_lhr= input('Tempat Lahir: ')
print(f'BIODATANYA {nama},{kelas},{NIM},{tmpt_lhr}')

#2.Jika terdapat kalimat UNIVERSITAS NUSA PUTRA SUKABUMI ,buatlah kode program untuk menampilkan output:

#1
a = "UNIVERSITAS NUSA PUTRA SUKABUMI"
a = a[12:22]
c = a.split()
d = list(c)
d.reverse()
for i in d:
    print(i.lower(),end=' ')


print()
#2
a = "UNIVERSITAS NUSA PUTRA SUKABUMI"
# b = a.split()
# b = list(a)
c = a.replace('U','')
print(c)


#3
a = "UNIVERSITAS NUSA PUTRA SUKABUMI"
b = a.split()
c = list(b)
c.reverse()

for a in c:
    print(a,end=' ')

print()
#4
a = "UNIVERSITAS NUSA PUTRA SUKABUMI"
b = a.split()
c = list(b)
for i in c:
    print(i[0],end='')


print()
# #5 
a = "UNIVERSITAS NUSA PUTRA SUKABUMI"
b = a.split()
c = b[0]
d = b[1]
e = b[2]
f = b[3]
print(c[8:11],f'{d[2:4]}{e[0:2]}',f[4:8])

