#Nomer 4
n = int(input("Masukkan nilai n: "))

# Menggunakan loop untuk mencetak angka ganjil
print("Angka ganjil hingga", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)