email = ["alunsujjada@gmailcom","alunsujjada@gmail.com","alun.sujjada@gmail.com","alunsujjada.gmail.com","alun.sujjada@gmailcom"]


for i in email:
    if i == "alunsujjada@gmail.com":
        print(i, "alunsujjada@gmail.com" == "alunsujjada@gmail.com")
    else:
        print(i,"alunsujjada@gmail.com" == i)
    


# import re

# # Fungsi untuk mengecek validitas email
# def cek_email(email):
#     # Menggunakan regex untuk mengecek apakah email memenuhi format yang benar
#     if re.match(r'[^@]+@[^@]+\.[^@]+', email):
#         return True
#     else:
#         return False

# # Contoh test case
# print(cek_email("alunsujjada@gmailcom"))  # False
# print(cek_email("alunsujjada@gmail.com"))  # True
# print(cek_email("alun.sujjada@gmail.com"))  # True
# print(cek_email("alunsujjada.gmail.com"))  # False
# print(cek_email("alun.sujjada@gmailcom"))  # False


    