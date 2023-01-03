
import array as arr
stok_tahu = [10,10,10,10,10,10,10,10,10,10]
# stok_tahu = arr.array('i',[10,10,10,10,10,10,10,10,10,10])
harga = 1000
uang = int(input('berapa uang yang akan di bayarkan: '))
banyak_tahu_dibeli = int(input('berapa tahu yang akan di beli: '))


for d in range(banyak_tahu_dibeli):
    if banyak_tahu_dibeli >= 10:
        stok_tahu[0] -= 1
    elif banyak_tahu_dibeli >= 20:
        stok_tahu[0:1] -= 1
    elif banyak_tahu_dibeli >= 30:
        stok_tahu[0:2] -= 1
    elif banyak_tahu_dibeli >= 40:
        stok_tahu[0:4] -= 1
    elif banyak_tahu_dibeli >= 50:
        stok_tahu[0:5] -= 1
    elif banyak_tahu_dibeli >= 60:
        stok_tahu[0:6] -= 1
    elif banyak_tahu_dibeli >= 70:
        stok_tahu[0:7] -= 1
    elif banyak_tahu_dibeli >= 80:
        stok_tahu[0:8] -= 1
    elif banyak_tahu_dibeli >= 90:
        stok_tahu[0:9] -= 1
    else:
        stok_tahu[9] -= 1

        
total_bayar = banyak_tahu_dibeli*harga

#output
print("Total harga yang dibeli",total_bayar)
print("Uang kembali",uang - total_bayar)
print("Sisa Tahu",sum(stok_tahu))
print("Posisi akhir rak : ",stok_tahu)

