def cek_uppercase(ceknya):
    a = list(ceknya)
    banyaknya_upper = 0
    for i in a:
        if i == i.upper():
            banyaknya_upper += 1
    return banyaknya_upper
        

    
    