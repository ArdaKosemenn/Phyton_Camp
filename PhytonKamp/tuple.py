#Tuple liste ile benzerdir.Tek farkı listelerde elemanları değiştirebiliyorken,tuple'da değiştirmek 
#söz konusu değildir.
#Bu veri yapısı performanslı bir data sağlar.

# tupleListe=()#Tuple kullanımı.
# liste=[]#Liste kullanımı.
tupleListe=(2,3,4,"Ankara",(5,6,7),[])
liste=[2,3,5,"Ankara",[5,6,7,],()]
#Tuple'ın içinde liste,Listenin içinde tuple ekleyebiliriz

liste[0]=6#Listede veri değiştirirken
# tupleListe[0]=6#Tuple da veri değiştiremeyiz.!!!

tupleDeger=("Arda")
print(type(tupleDeger))

tupleDeger=("Arda",)
print(type(tupleDeger))
#NOT!!:üstte yazmış olduğum kodda tupleListe (3,) , listede ise[3] gösterir.nedeni:tuple veriyi string olarak anlama
#tuple olarak anla diye yanına virgül koyar.

print(tupleListe[1:2])
print(liste[1:2])

#NOT!!:üstte yazmış olduğum kodda tupleListe (3,) , listede ise[3] gösterir.nedeni:tuple veriyi string olarak anlama
#tuple olarak anla diye yanına virgül koyar.

print(tupleListe[-2])#sondan ikici veriyi göster
print(liste[-2])#sondan ikici veriyi göster
print(type(tupleListe))
print(type(liste))
print(tupleListe)
print(liste)
print(len(tupleListe))
print(len(liste))