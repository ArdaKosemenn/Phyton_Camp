#UNION: İki settedeki dataları tek bir kere yazarak bir araya getirir.
#Örnek:İki sette 3 indexi varsa sadece bir tane 3 indexi yazar.

setA={1,2,3,4,5}
setB={1,3,4,6,7,8}

#1. Yöntem
print(setA | setB)# Pipe: AltGr+virgülün yanındaki tuş ile yapılıyor.
#2.Yöntem
print(setA.union(setB))#Tam tersini de yapabilirsin.