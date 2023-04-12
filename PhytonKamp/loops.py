#DÖNGÜLER

#FOR DÖNGÜSÜ
sehirler =["Ankara","İstanbul","İzmir"]

##Üste yazmış oldğumuz "#%%" kodu sadece seçdiğim kodu çalıştırır.
for sehir in sehirler:
   if sehir =="İstanbul":
      break #Break:Bağlı olduğu döngü için Döngüyü bitirir.
   continue #dögünün o anki dönme durumunu iptal eder ama sonra devam eder.
#Örneğin ankara istanbula eşit mi ?Değil yazdırır.İstanbul istanbula eşit mi?eşit bu kodu yazdırmaz.
#izmir istanbula eşit mi ?değil yazdırır. 
   print(sehir + " için kod=" + sehir[0:3])
   print("*********")




for sayi in range(0,10,2): # 0: başlangıç değeri, 10:yazdığımız yasıya kadar 2:sayı arttırma 
   print(sayi)  #RANGE:-e kadar  demek.


