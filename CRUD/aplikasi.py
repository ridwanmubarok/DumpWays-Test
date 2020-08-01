import mysql.connector

def main():
    database = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="wikigames"
    )
    print('---++CRUD++---')
    print('1 = INSERT DUMMY TABLE TYPE')
    print('2 = INSERT DUMMY TABLE HEROES')
    print('------SHOW------')
    print('3 = TAMPILKAN TABLE TYPE')
    print('4 = TAMPILKAN TABLE HEROES')
    print('------FILTER------')
    print('5 = PENCARIAN HERO')
    print('---++DELETE AND UPDATE HEROES++---')
    print('6 = DELETE HERO')
    print('7 = UDPATE HERO')


    Menu = int(input("Pilih Menu : "))
    cek(Menu,database)


def cek(Menu,database):
    if Menu == 1:
        insertType(database)
    if Menu == 2:
        insertHeroes(database)
    if Menu == 3:
        showType(database)
    if Menu == 4:
        showHeroes(database)
    if Menu == 5:
        showFromType(database)
    if Menu == 6:
        hapushero(database)
    if Menu == 7:
        updateHero(database)


def insertType(database):
    Name = input("Masukan Nama Tipe : ")
    koneksis = database.cursor()
    val = Name
    sql = "Insert into type_tb (name) VALUES ('%s')"
    koneksis.execute(sql, (val))
    database.commit()
    print("{} data Type Berhasil disimpan".format(koneksis.rowcount))

def insertHeroes(database):
    Name = str(input("Masukan Nama Hero : "))
    showType(database)
    Type = (input("Masukan Type ID : "))
    koneksis = database.cursor()
    val = (Name,Type)
    sql = "Insert into heroes_tb (name,type_id) VALUES (%s,%s)"
    koneksis.execute(sql,val)
    database.commit()
    print("{} data Type Berhasil disimpan".format(koneksis.rowcount))

def showType(database):
    koneksis = database.cursor()
    sql = "Select * From type_tb"
    koneksis.execute(sql)
    hasil = koneksis.fetchall()
    if koneksis.rowcount == 0:
        print('Data Kosong atau Tidak ada')
    else:
        for data in hasil:
            print("----++-----")
            print(data[0],".",data[1])
            print("----++-----")
                
    
def showHeroes(database):
    koneksis = database.cursor()
    sql = "Select * From heroes_tb"
    koneksis.execute(sql)
    hasil = koneksis.fetchall()
    if koneksis.rowcount == 0:
        print("Data Tdak Ada")
        return main()
    else:
        for data in hasil:
            print("----++-----")
            print(data[0],'.',data[1])
            print("----++-----")
     
def showFromType(database):
    showType(database)
    print('Kosongkan jika pencarian lewat nama')
    type_id = input("Masukan Type ID : ")
    nama    = input("Masukan Nama : ")
    koneksis = database.cursor()
    val = (type_id,nama)
    sql = "Select * From heroes_tb where type_id LIKE %s or name LIKE %s"
    koneksis.execute(sql,val)
    hasil = koneksis.fetchall()
    if koneksis.rowcount == 0:
        print("Data Tdak Ada")
        return main()
    else:
        for data in hasil:
            print("----++-----")
            print(data[1])
            print("----++-----")


def hapushero(database):
    cursor = database.cursor()
    showHeroes(database)
    hero_id = input("pilih ID HEROES : ")
    sql = "DELETE FROM heroes_tb WHERE id=%s"
    val = (hero_id,)
    cursor.execute(sql,val)
    database.commit()
    print("{} data Hero berhasil dihapus".format(cursor.rowcount))

def updateHero(database):
    cursor = database.cursor()
    showHeroes(database)
    hero_id = input("pilih ID HEROES : ")
    name = input("Nama Hero : ")
    sql = "UPDATE heroes_tb SET name=%s WHERE id=%s"
    val = (name,hero_id,)
    cursor.execute(sql,val)
    database.commit()
    print("{} data Hero berhasil Diperbaharui".format(cursor.rowcount))


main()