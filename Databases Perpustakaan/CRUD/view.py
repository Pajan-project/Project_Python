from . import operasi

def console_update():
    console_view()
    while(True):
        print("Silahkan masukkan no buku yang akan di update :")
        no_buku = int(input("Masukkan No Buku :"))
        data_buku = operasi.read(INDEX=no_buku)
        
        if data_buku:
            break
        else:
            print("Data buku tidak valid, Silahkan masukkan lagi : ")
            
    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break [1]
    judul = data_break [2]
    penulis = data_break [3]
    tahun = data_break [4][:-1]

    while(True):
        print("\n"+"="*100)
        print("Silahkan pilih data yang akan diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1" : judul = input(f"Judul\t:")
            case "2" : penulis = input(f"Judul\t:")
            case "3" :  
                while(True):
                    try:
                        tahun = int(input("Masukkan Tahun :"))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus dalam INT, Dengan format (yyyy)")
                    except:
                            print("Tahun harus dalam INT, Dengan format (yyyy)")
            case _:
                print("Index Tidak Cocok")
        
        print("DATA BARU ANDA")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")        
        is_done = input("Apakah sudah selesai (y/n) ?")
        if is_done == "y" or is_done == "Y":
            break
        
    operasi.update(no_buku,pk,date_add,tahun,judul,penulis)


def console_create():
    penulis = input("Masukkan Penulis: ")
    judul = input("Masukkan Judul :")
    
    while(True):
        try:
            tahun = int(input("Masukkan Tahun :"))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus dalam INT, Dengan format (yyyy)")
        except:
                print("Tahun harus dalam INT, Dengan format (yyyy)")
        
    operasi.create_data(judul,penulis,tahun)
    print("Ini adalah data baru anda !!")
    console_view()






def console_view():
    datafix = operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(datafix):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    # Footer
    print("="*100+"\n")
