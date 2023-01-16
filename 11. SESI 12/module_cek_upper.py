def cek_uppercase(ceknya):
    banyaknya_upper = 0
    for i in ceknya:
        if i.isupper():
            banyaknya_upper += 1
    return banyaknya_upper