urunler = ["Laptop","Keyboard","Mouse"]
print(urunler)
#print(type(urunler))
urunler.append("Phone")#append ile listeye yeni eleman ekleyebiliriz.
urunler.remove("Laptop")#remove ile lisetedeki ürünü kaldırırız.
urunler[0]="Masaüstü"# bu kod ile 0. elemanı olan laptop yerine masaüstü elemanı gelir.
print(len(urunler))


ogrenciler1 =["İlker","Cavit","Hasan"]
ogrenciler2 =["Hasan","Halil","Murat"]

ogrenciler1=ogrenciler2
ogrenciler2[0]="Engin"
print(ogrenciler1)
print(ogrenciler2)

#List Constructor:Liste oluşturucu.
sehirler=list(("Ankara","İstanbul","Ankara",))
print(len(sehirler))

#Clear:Liste Temizleme
# print(sehirler.clear())#sehirlerdeki bütün değerleri siler 
# print(sehirler)

#Count:Listedeki elemanın kaç tane olduğunu gösterir.
print("Ankara Sayısı = "+ str(sehirler.count("Ankara")))
print("Ankara Kaçıncı İndexte:"+ str(sehirler.index("Ankara")))#İndex:Listedeki elemanın kaçıncı sırada olduğunu gösteriyor.
#Not:index gördüğü değere kadar alır.yani iki tane ankara varsa ilkinin hangi sırada olduğunu gösterir.
sehirler.pop(1)#listedeki 1. elemanı siler.
sehirler.insert(0,"İstanbul")#İnsert:listenin 0.sıraya istanbulu ekler.
sehirler.reverse()#Listeyi tersten yazdırır.
print(sehirler)

sehirler3=sehirler.copy()
sehirler2=sehirler
#NOT:üsteki kod sehirler listesinin aynısını sehirler2 ye atar.Ama sehiler2'de yapmış olduğun değişiklikler"sehirler"
#listesini de etkiler.Eğer "sehirler"listesinded değişiklik yapmadan kopyasını alamak için "COPY" kodunu kullanırız.
sehirler2[0]="İzmir"
print(sehirler2)    
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)#Extend:sehirler ve sehirler2 deli verileri tek liste haline getitir.yani birleştirir.
sehirler.sort()#Sort:Listeyi alfabetik ya da sayısal olarak sırasıyla yazar.
print(sehirler)
#liste referans bir tiptir.(referans-> list,döngüler,class(sınıflar)) HEAP
#int ise değer bir tiptir.(değer tip-> int) STACK

#NOT!!: Bellekte iki tane kısım var:STACK VE HEAP
#Sayısal değer olan int,float,boolaen,inam gibi sayısal değerler DEĞER TİPLERİDİR.(STACK) 