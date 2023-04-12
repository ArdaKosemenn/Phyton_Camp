
number=int(input("Kaç tane sayı olsun ? :"))

star=""#Boş bir değerde yıldız oluşturuyoruz.

for x in range(1,number+1):#kullanıcı 5 girerse 5 i dahil etmez dahil etmesi için +1 yazıyoruz
    star=star+"*"
    print(star)