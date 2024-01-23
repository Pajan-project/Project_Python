import time
from . import database
from . import util
import os

def delete(no_buku):
    try:
        with open(database.DBNAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    os.rename("data_temp.txt",database.DBNAME)


def update(no_buku,pk,date_add,tahun,judul,penulis):
    templatedata = database.DBTEMPLATE.copy()
    
    templatedata["pk"] = pk
    templatedata["date_add"] = date_add
    templatedata["judul"] = judul + database.DBTEMPLATE["judul"][len(judul):]
    templatedata["penulis"] = penulis + database.DBTEMPLATE["penulis"][len(penulis):]
    templatedata["tahun"] = str(tahun) 
    
    data_str = f'{templatedata["pk"]},{templatedata["date_add"]},{templatedata["judul"]},{templatedata["penulis"]},{templatedata["tahun"]}\n'

    panjang_data = len(data_str)
    try:
        with open(database.DBNAME,'r+',encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
            
    except:
        print("Data gagal di update")



def create_data(judul,penulis,tahun):
    
    templatedata = database.DBTEMPLATE.copy()
    
    templatedata["pk"] = util.pk(5)
    templatedata["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    templatedata["judul"] = judul + database.DBTEMPLATE["judul"][len(judul):]
    templatedata["penulis"] = penulis + database.DBTEMPLATE["penulis"][len(penulis):]
    templatedata["tahun"] = str(tahun) 
    
    data_str = f'{templatedata["pk"]},{templatedata["date_add"]},{templatedata["judul"]},{templatedata["penulis"]},{templatedata["tahun"]}\n'
    try:
        with open(database.DBNAME,'a',encoding="utf-8") as file:
            file.write(data_str)
            
    except:
        print("Data gagal di buat")
    


def createfirstdata():
    
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

    
    templatedata = database.DBTEMPLATE.copy()
    
    templatedata["pk"] = util.pk(5)
    templatedata["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    templatedata["judul"] = judul + database.DBTEMPLATE["judul"][len(judul):]
    templatedata["penulis"] = penulis + database.DBTEMPLATE["penulis"][len(penulis):]
    templatedata["tahun"] = tahun 
    
    data_str = f'{templatedata["pk"]},{templatedata["date_add"]},{templatedata["judul"]},{templatedata["penulis"]},{templatedata["tahun"]}\n'
    try:
        with open(database.DBNAME,'w',encoding="utf-8") as file:
            file.write(data_str)
            
    except:
        print("Data gagal di buat")
    
    
# Read Data
def read(**kwargs):
    try:
        with open(database.DBNAME,'r') as file:
            data = file.readlines()
            jumlah_buku = len(data)
            if "INDEX" in kwargs:
                index_buku = kwargs["INDEX"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return data[index_buku]
            else:
                return data
    except:
        print("Data gagal di baca")
        return False