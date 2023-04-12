
from multiprocessing import connection
import sqlite3

def selectOperasyonlari():
    connection = sqlite3.connect("chinook/chinook.db")

    #cursor=connection.execute("select * from customers")
    #customers tablosundaki tüm veri seç(*tümünü seçer, getirir.)
    #cursor=connection.execute("select FirstName,LastName from customers where city='Prague'")
    #customers tablosunun city klasorundeki praglı olanların adı soyadı
    #cursor=connection.execute("select FirstName,LastName from customers order by FirstName")
    #order by =alfabetik olarak sıralar.

    #for row in cursor:
    #    print("First Name="+row[0])#satırın ikinci kolonunu getir demek.ikinci kolonda first name var
    #    print("Last Name="+row[1])
    #    print("******************")

    #GROUP BY VE HAVING

    #cursor=connection.execute("select city,count(*) from customers group by city having count(*)>1 order by count(*) desc" )
    #order by her zaman sorgunun sonuna yazılır çünkü bu komutta ilk önce gruplama yapması lazım
    #Desc=sondan başa yazdırmayı sağlar .
    #for row in cursor:
    #    print("City="+row[0])
    #    print("Count="+ str(row[1]))
    #    print("*********")


    #LİKE Komutu=Örneğin ismin içinde a ve b olanlar vs gibi komutlarda kullanılır.
    cursor=connection.execute("select FirstName from customers where FirstName like'%a'")
    #%a%= yüzde işaretleri başında ve sonunda demek. içinde a harfi olanları yazdır.
    #a%=ismin ilk harfi yani başında a olanları yazdır.
    #%a=ismi a olanla bitenler demek.
    for row in cursor:
        print("LastName="+row[0] )
        print("********")

    connection.close()                                        

#selectOperasyonlari()

##İNSERT OPERAYSONU (VERİ EKLEME)

def insertOperasyolari():
    connection=sqlite3.connect("chinook/chinook.db")
    connection.execute("""insert into customers (FirstName,LastName,City,email) 
                       values('Arda','Kösemen','Malatya','ardakosemen1905@gmail.com')""")
#İlk önce nereye veri eklememiz gerekecekse ilk o tablonun ismi yazılır. Daha sonra hangi değerleri eklemek istiyorsak
#sırasıyla valuesin içine yazılır.
    connection.commit() #Commit=işlemek demek.
    connection.close()
    
#insertOperasyolari()
#şu anda bilgileri veri tabanına kaydetti db browser sqllite ı açarak bakabiliriz


#GÜNCELLEME OPERASYONU(VERİ TABANINDAKİ BAZI BİLGİLERİ GÜNCELLEME)

def updateOperasyonlari():
    connection=sqlite3.connect("chinook/chinook.db")
    connection.execute("update customers set city='Ankara' where city='Malatya'")
    
    connection.commit()
    connection.close()
    
#updateOperasyonlari()

#şu anda malatya olan city veri tabanı ankara oldu.

#DELETE OPERASYONU

def deleteOperasyonlari():
    connection=sqlite3.connect("chinook/chinook.db")
    connection.execute("delete from customers where customerid=60")
    
    connection.commit()
    connection.close()
    
#deleteOperasyonlari()

#customers tablosundaki customerid bölümünün 60.sıradaki id yi sildi

#JOİN OPERASYONU: iki ilişkili tablouyu,üç ilişkili tabloyu ,daha fazla da olabilir biribirine joın etmek 
#için kullanılır.
#Mesela kullandığım veri tabanında albulms ve artıst tablosundaki ismi ve şarkıları bir arada kullanabiliriz.


def joinOperasyonlari():
    connection=sqlite3.connect("chinook/chinook.db")
    cursor=connection.execute("""select albums.Title,artists.Name from artists inner join
                            albums on artists.ArtistId = albums.ArtistId""")
    for row in cursor:
        print("Title =" + row[0])
        print("Name = " + row[1])
        print("**************")
        
    connection.close()
    
joinOperasyonlari()
        
        
        
        
        
        
        