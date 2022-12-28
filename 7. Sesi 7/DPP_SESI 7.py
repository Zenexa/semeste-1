'''
1. Buatlah program untuk membalik sebuah kalimat, misal:
input : “LUPA-LUPA INGAT”
output : “TAGNI APUL-APUL”
'''
#1
text_input = input('masukan text = ')
print(text_input[::-1])




'''
2.Buatlah program untuk menghitung jumlah masing-masing huruf vokal, dengan output seperti berikut ini:
kalimat : “Universitas Nusa Putera”
output :
	Jumlah huruf A = 3
	Jumlah huruf I =  2
	Jumlah huruf U = 3
	Jumlah huruf E = 2
	Jumlah huruf O = 0
	Total jumlah huruf vokal = 10
'''
#2
inputThree = input("Silahkan masukkan input : ")
vokalA = ["a", "A"]
vokalI = ["i", "I"]
vokalU = ["u", "U"]
vokalE = ["e", "E"]
vokalO = ["o", "O"]
totalVokalA = 0
totalVokalI = 0
totalVokalU = 0
totalVokalE = 0
totalVokalO = 0

for i in inputThree:
    if i in vokalA :
        totalVokalA += 1
    if i in vokalI :
        totalVokalI += 1
    if i in vokalU :
        totalVokalU += 1
    if i in vokalE :
        totalVokalE += 1
    if i in vokalO :
        totalVokalO += 1
    
        
print("Jumlah huruf A ",totalVokalA)
print("Jumlah huruf I ",totalVokalI)
print("Jumlah huruf U ",totalVokalU)
print("Jumlah huruf E ",totalVokalE)
print("Jumlah huruf O ",totalVokalO)
print('Total jumlah huruf vokal adalah ',totalVokalA+totalVokalI+totalVokalU+totalVokalE+totalVokalO)

