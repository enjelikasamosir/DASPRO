
hargabarang=input("harga barang : ")
jumlahbarang=input("jumlah barang : ")
diskonbarang=input("diskon : ")

hargabarang=int(hargabarang)
jumlahbarang=int(jumlahbarang)
diskonbarang=int(diskonbarang)
#total diskon

a=hargabarang*jumlahbarang
b=a*(diskonbarang/100)
hasil=a-b

print(hasil)



