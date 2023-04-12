#FONKİSYONLAR
#Bir kodu bir çok yerde kullananmamız gerekiyorsa , her yere tekrar tekrar yazmamızı engeller

#def greet(name):
    #"""This function greets to the person passed in as 
    #paramater"""
    #print("Hello,",name + "Good Morning")
    
def selamVer(isim =" ziyaterçi"):#eğer sen bana parametre yani isim vermezsen ben default olarak (otomatik) ziyaterçi yazacam
    print("Merhaba"+" "+ isim)
    
selamVer()
selamVer("mehmet")
selamVer("Cevdet")
selamVer("Salih")
    
def selamVer2(isim, soyİsim="arkadaş"):
    print("Merhaba " + isim + " " + soyİsim)
    
selamVer2("arda")
selamVer2("ARDA","KÖSEMEN")
    
def dikUcgenAlaniHesapla(a,b):
    return a*b/2
alan=dikUcgenAlaniHesapla(2,3)
print(alan)


#Lambda fonksiyonu= tek bir satırda return yapmak için kullanılır.
dikUcgenAlaniHesapla2 =lambda a,b :a*b/2
print(dikUcgenAlaniHesapla2(4,8))


x=dikUcgenAlaniHesapla2