#Nomer 5
# Mengambil input nilai n dari pengguna dan mengonversinya ke tipe integer
n = int(input("Masukkan nilai n: "))

# Menggunakan loop untuk mencetak baris dari 1 hingga n
for i in range(1, n + 1):
    # Loop untuk mencetak angka i sebanyak i kali
    for j in range(i):
        print(i, end=" ")  # Mencetak angka i dengan spasi di antara angka-angka
    
    # Mencetak baris baru setelah selesai mencetak angka untuk baris saat ini
    print()