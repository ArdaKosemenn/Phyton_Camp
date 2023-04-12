#Bir excel txt vb. dosyalara erişerek çalışmak
f= open("müsteriler.txt","r") #R(Read) dosya oluşturur.
#f= open("müsteriler.txt","w") W(write) yani yazdır oluştur demektir. Normalde default olarak R yani oku olarak
#gelir.Böyle bir dosya olmadığı için W yani yazdırmamız lazım.

#f= open("müsteriler.txt","a") A(append) ise dosyayı okuyacam aynı zamanda dosyaya yazacam(ekleme) anlamına gelir.
#f= open("müsteriler.txt","x") X(create) dosya oluşturur aynı dosya var ise hata verir.
#print(f.read(10)) paratez içine 10 yazarsak ilk 10 karakteri yazar


print("***********")

#NOT!! read komutu ile readline komutu aynı andan kullanılmaz .Çünkü read hepsini okduğu için gerek kalmaz.
#print(f.readline()) #Readline ise satır satır yazar kaç tane  readline yazarsan o kadar satır yazdırır.
#print(f.readline())

#Not üste iki tane readline olduğu için for döngüsünde bir daha ilk iki satırı yazdırmaz son iki tane olanı yazdırır.
for l in f:
    print(l)

# Bu üç değişkenden sadece bir tanesini kullanırız.Hnagisini isterseniz.İç içe kullanılmaz.

                ##KURAL##
f.close() # dosyada işin bittiği zaman dosyayı kapat

fileToAppend=open("ogrenciler.txt","a")
fileToAppend.write("Vb")
fileToAppend.write("\n")#/n= enter yani bir satır boşluk bırakır.
fileToAppend.write("Vb Code")

#fileToAppend=open("ogrenciler.txt","w")
#Not: İçinde bilgiler olan dosyada W (write) olarak açarsanız dosyanın üzerine yazar ve bütün veriler gider.

fileToAppend.close()

#Dosyayı silemk için ise metot kullanırız.

import os
os.remove("ogrenciler.txt")

#Uygulama içide bir dosyayının olup oladığını ise if ile öğreniriz.

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.tx")
else:
    print("Böyle bir dosya yok.")

os.rmdir("empty")#Klaörü siler. (empty klasörü oluşturdum,sildim)





