def fibonacci(n):
    # Inisialisasi nilai awal deret Fibonacci
    f_n_2, f_n_1 ,f_n= 0, 1,1
    # Pengulangan untuk menghitung nilai Fibonacci ke-n
    for _ in range(1, n):
        print("Nilai Fibonacci ke-{} adalah: {}".format(i, f_n))
        f_n = f_n_1 + f_n_2
        f_n_2, f_n_1 = f_n_1, f_n
        
        i+=1
    

# Input dari pengguna
n = int(input("Masukkan nilai n untuk deret Fibonacci: "))

# Memanggil fungsi Fibonacci dan menampilkan hasilnya
hasil_fibonacci = fibonacci(n)

