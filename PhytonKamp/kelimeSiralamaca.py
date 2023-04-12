
cumle="Bugün Hava Çok Güzel"

kelimeler=cumle.split()#split() metodu listeyi belirtilen ayıracı kullanarak yeniden döndürür. yani split() karakter dizilerini istenen şekilde böler. 
#-ayırıcı diye tanımladığımız ilk parametre, karakter dizisinin nereden bölüneceğini seçer. eğer ayırıcı tanımlanmazsa karakter dizisi her boşluk gördüğünde ayırır.
kelimeler.sort()

print(kelimeler)

for kelime in kelimeler:
    print(kelime)
