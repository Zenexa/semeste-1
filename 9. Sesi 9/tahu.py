import array as arr
# stok_tahu = [10,10,10,10,10,10,10,10,10,10]
stok_tahu = arr.array('i',[10,10,10,10,10,10,10,10,10,10])
harga = 1000
uang = int(input('berapa uang yang akan di bayarkan: '))
banyak_tahu_dibeli = int(input('berapa tahu yang akan di beli: '))

for d in range(banyak_tahu_dibeli):
    if d < 10:
        stok_tahu[0] -= 1
    elif d <= 20:
        stok_tahu[1] -= 1
    elif d < 30:
        stok_tahu[2] -= 1
    elif d < 40:
        stok_tahu[3] -= 1
    elif d < 50:
        stok_tahu[4] -= 1
    elif d < 60:
        stok_tahu[5] -= 1
    elif d < 70:
        stok_tahu[6] -= 1
    elif d < 80:
        stok_tahu[7] -= 1
    elif d < 90:
        stok_tahu[8] -= 1
    else:
        stok_tahu[9] -= 1
        
total_bayar = banyak_tahu_dibeli*harga

#output
print("Total harga yang dibeli",total_bayar)
print("Uang kembali",uang - total_bayar)
print("Sisa Tahu",sum(stok_tahu))
print("Posisi akhir rak : ",list(stok_tahu))