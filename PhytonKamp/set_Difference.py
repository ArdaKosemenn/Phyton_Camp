#DİFFERENCE:
#A da olup Bde olmayan,ya da B de olup A da olmayanı gösterir.

setA={1,2,3,4,5}
setB={1,3,4,6,7,8}

#1.YÖNTEM
print(setA - setB)

#2.YÖNTEM
print(setA.difference(setB))
print(setB.difference(setA))

#SYMEMTRİC DİFFERENCE: A da olup Bde olmayan,ya da B de olup A da olmayanı tek bir kodda gösterir. gösterir.

#1.YÖNTEM
print(setA ^ setB)

#2.YÖNTEM
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))