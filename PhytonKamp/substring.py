# YAZILARI BÖLME(SUBSTRİNG)

mesaj="Merhaba Dünya"

print(mesaj[2])#merhaba dünya yazısındaki "r" yi gösterir.
print(mesaj[2:5])#ikici indexden 5e kadar gösterir.5 dahil değil!!

yeniMesaj=(mesaj[2:5])##bir değeri bir değişkene aktarma
yeniMesaj=(mesaj[12:13])
print(yeniMesaj[2:])#2 dem sonra her şeyi göster.
print(yeniMesaj[:2])#baştan 2 ye kadar 2 dahil değil.

#Len fonksiyonu indexin uzunluğunu verir
print(len (mesaj))

yeniMesaj2=mesaj [len(mesaj)-1:len(mesaj)] #en son karaktere ulaşmak için -1 verdik
print(yeniMesaj2)

# Lower Upper:Bir metnin karakterlerini küçültme veya büyültmeye yarar.
print(mesaj.upper())#Büyük
print(mesaj.lower())#Küçük

#Replace:Karakterin harfini değiştirir.
print(mesaj.replace("ü","u"))

#Not:replace"i kullandğımız zaman sadece o kod da karakteri değiştirir.Komple kodda çıktısı hep "u"olsun diyorsanız
#atama yapmak zorundayız.

mesaj=mesaj.replace("ü","u")
#Split:gelen veriyi kelime kelime parçaya ayırıyor. liste gibi ayırır.
#Strip:cümlenin başındaki sonundaki v.s Boşlukları kaldırıyor
bilgi= "                 Arda; Kösemen; 33; Malatya               ".strip()
print(bilgi.split())
print("Adı :"+ bilgi.split  (";")[0])#noktalı virgüle göre ayır. ayır ve 0.elemanı yazdır.Arda'yı yazdırır

#İnput:Kullanıcıdan bilgi almak için kullanılır.
ad = input("Adınız ?")

sayi1 =input("Sayı 1:")
sayi2 =input("Sayı 2:")
print(sayi1+sayi2)#böyle yazdığınız zaman sayıları bile string okudğu için toplamaz yanyana yazar.
print(int(sayi1) + int(sayi2))#sayısal işlem yapar.