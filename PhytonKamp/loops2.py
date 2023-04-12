krediler=["Hızlı Kredi","Maaşını Haklbank'tan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]

#alias:takma isim alltaki for döngüsündeki "kredi" ismini kendimiz atıyoruz. 
for kredi in krediler:
    print(kredi)
    
for i in range(len(krediler)):#burda ise listedeki değere kadar yazdır demek.
    print(krediler[i])
    
# for sayi in range(10):#0 dan 9 a kadar olan sayıları yazdırır.
#     print(sayi)
    
for sayi in range(3,11):#3 dan 10 a kadar olan sayıları yazdırır.
    print(sayi)    

for sayi in range(0,11,2):#0 dan 10 a kadar çift olan sayıları yazdırır.
    print(sayi)    