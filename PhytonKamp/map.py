#map() bir diziyi alıp başka bir diziye dönüştürüyor.


sayilar=[1,2,3,4,5]
#map komutu
sayilarKareli=list(map(lambda sayi:sayi**2,sayilar))

#map komutu olmadan yazılan prog.
#for sayi in sayilar:
#    sayilarKareli.append(sayi*sayi)

#Filtreleme
sayilarFiltreli = list(map(lambda sayi:sayi>2,sayilar))
#sayilar listesindeki herr bir sayı için sayı ikiden büyük ise listeye ekle.
print(sayilarKareli)
print(sayilarFiltreli)

#Reduce=Reduce bir liste üzerine bazı hesaplamaları
#gerçekleştirmek ve bir sonuç döndürmek için çok kullanışlı bir fonksiyondur
from functools import reduce 
#reducu üsteki gibi import etmemiz lazım.
sayilarFaktöriyel = reduce(lambda x,y:x*y,sayilar)
print(sayilarFaktöriyel)