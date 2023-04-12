#Soru:3 sayıdan hangisi büyükse onu yazdır.

sayi1 =45
sayi2 =55
sayi3 =75

if sayi1>sayi2 and sayi1>sayi3:
    print("En Büyük Sayı"+str(sayi1))
elif sayi2>sayi1 and sayi2>sayi3:
    print("En Büyük Sayı"+str(sayi2))
elif sayi3>sayi1 and sayi3>sayi2: 
    print("En Büyük Sayı"+str(sayi3))
elif sayi1==sayi2==sayi3:
    print("Sayılar Eşittir")
