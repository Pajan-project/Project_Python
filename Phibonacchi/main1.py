f_n_1, f_n_2, f_n = 0,1,1

n = int(input("Masukkan Fibonachi yang dicari :"))

i = 1
for _ in range(i,n):
    print("Nilai Fibonachi ke {} adalah {}".format(i,f_n))
    f_n = f_n_2 + f_n_1
    f_n_1 = f_n_2
    f_n_2 = f_n
    
    i += 1