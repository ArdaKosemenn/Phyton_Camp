import sqlite3
from sqlite3.dbapi2 import Cursor  #veritabanı 

def listele():
    baglanti= sqlite3.connect("chinook/chinook.db") # bu kodu yazarak veri tabanına bağlarız.Parantez içine
    #veri tabanının ait olduğu adresi yazarız.
    cursor = baglanti.execute("select FirstName,LastName from customers ")  #sorgu yazmak için cursor komutu kullanılır.
    #bağlantı için yani chinook.db parantez içindeki sorguyu çalıştır    #execute:çalıştır demek
    for satir in cursor:  #cursor daki her satiri gez 
        print(satir[1]) # o satırın birinci elemanını
        
    baglanti.close()#bağlantıyı kapat.
    
listele()# bura listeyi çağırıyoruz.