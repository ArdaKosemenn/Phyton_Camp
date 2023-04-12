#SAYILARIN YERİNİ DEĞİŞTİRME

x=10
y=20



#1.YÖNTEM(SADECE PHYTON UYGULAMASI İÇİN GEÇERLİDİR)

temp=x #Temp:Geçici değer tutmak anlamına gelir. #tempin değeri 10
x=y # x'in değeri 20 oldu
y=temp #y ise tempin aldığı değer yani 10 oldu.
#2.YÖNTEM
x,y=y,x
print("x =" +str(x))
print("y =" + str(y))