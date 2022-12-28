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
menit = int(input('masukan berapa menit olahraga = '))
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
    