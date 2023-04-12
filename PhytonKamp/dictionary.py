#DİCTİONARY:(SÖZLÜK)
#Aynı set gibi sırasız veri tutar.
#Günlük hayatta sözlükler gibi düşünebiliriz.

#KULLANIM ŞEKLİ 1:
sozluk={
    "book":"kitap",
    "chair":"sandalye",
}

#KULLANIM ŞEKLİ 2:
sozluk2=dict(kitap="book",sandalye="chair",mouse="fare")

sozluk["book"]="kitap 1"
sozluk["pencil"]="kalem"
del(sozluk["book"])
print(len(sozluk2))
print(len(sozluk))

