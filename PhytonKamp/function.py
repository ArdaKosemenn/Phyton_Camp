#Fonsiyonları mesela bir e ticaret sitedesinden sepete ekle butonunu anasayfada ürünün altında e postalarda
#aynı kodlar bulunuyor.bunları teker teker yazmak yerine "def" kodu ile tanımlarsak üç kere yazmak yerine bir defa yazarız. 
def kredileriListele():
    krediler=["Hızlı Kredi","Maaşını Haklbank'tan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]
    for kredi in krediler:
        print(kredi)#Bu kodları tanım olarak düşün
        
        
kredileriListele()#Bu kodu ise çağırmak olarak düşün.
