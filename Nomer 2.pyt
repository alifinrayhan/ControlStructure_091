#Nomer 2
a = int(input("masukkan Angka Pertama:"))
b = int(input("Masukkan Angka Kedua:"))
c = int(input("Masukka Angka Ketiga:"))

if a >= b and a >= c:
    AngkaTerbesar = a
elif b >= a and b >= c:
    AngkaTerbesar = b
else:
    AngkaTerbesar = c


print("Angka Terbesar:",AngkaTerbesar)