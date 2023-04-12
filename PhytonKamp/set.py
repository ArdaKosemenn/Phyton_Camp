#SETLERLE ÇALIŞMAK.
#Listelere benzerdir.
#En önemli özelliği indeksiz ve sırasız elemanlardan oluşmasıdır.
#Performanslı data sağlar.
#Veri tekrarı söz kousu değildir.
#Setlerle indexler sıralı değildir.Kendi algoritmasına göre sıralar.

studentsSet= {"Arda","Ali","Mehmet"}#1.Kullanımı
# studentsSet2 =set("asdsa","asdas","asdas")#2.Kullanımı
print(studentsSet)

for students in studentsSet:
    print(students)#Seti döndürme
    
    print("Derin" in studentsSet)#Set'in içinde eleman arama(True -False olarak verir.)
print(studentsSet)

if "Derin" in studentsSet:
    print("Listede var.")
    
studentsSet.add("Ahmet")#Set'e yeni eleman ekleme.(Not!!Setlerde eleman silinemez)
print(studentsSet)

studentsSet.update(["Mert","Ayşe","Özge"])#Birden fazla index eklmek için kullanılır.
print(studentsSet)

print(len(studentsSet))#Setin uzunluğu

#DİSCARD=Eğer silinecek elemanı bulamadıysa error(hata)vermesini engeler.
studentsSet.discard("sadas")

print(studentsSet.clear())#Setdeki bütün elemanları(indexleri)siler.
print(len(studentsSet))

del studentsSet #Seti komple siler
print(studentsSet)