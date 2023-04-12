#FAKTÖRİYEL HESAPLAMA

sayi=int(input("Kaçıncı Faktöriyeli Hesaplayayım? :"))

fakt=1
for i in range (sayi):
      fakt = fakt * (i+1)
print("Faktöriyel:",fakt)

# ##FARKLI YÖNTEMİ

sayi=int(input("Kaçıncı Faktöriyeli Hesaplayayım? :"))

faktöriyel=1

if sayi<0:
    print("Negatif Sayıların Faktöriyeli Hesaplanamaz")
elif sayi==0:
    print("Sonuç : 1")
else:
    for i in range(1,sayi+1):
        faktöriyel=faktöriyel*i
    print("Sonuç: ",faktöriyel)