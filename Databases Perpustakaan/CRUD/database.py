from . import operasi

DBNAME = "data.txt"
DBTEMPLATE = {
"pk" : "XXXXXX",
"date_add" : "yyyy-mm-dd",
"judul" : 255*" ",
"penulis" : 255*" ",
"tahun" : "yyyy"
}

def CheckDatabase():
    try:
        with open(DBNAME,'r') as file:
            print("Database Ditemukan")
            
    except:
        with open(DBNAME,'w',encoding="utf-8") as file :
            print("Database Tidak Ditemukan, Silahkan membuat baru")
            operasi.createfirstdata()