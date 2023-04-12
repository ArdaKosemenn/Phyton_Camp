#HESAP MAKİNESİ
# Kullanıcıdan 1 ile 4 arasında sayı istenecek
#1 = toplama
#2=çıkarma
#3 carpma
#4 bolme
#bu sayılardan birini seçtiklten sonra kullanııcdan 2 sayı isteyerek sonucu bulacağız.

def topla(sayi1,sayi2):
    return sayi1+sayi2

def cikar(sayi1,sayi2):
    return sayi1-sayi2

def carp(sayi1,sayi2):
    return sayi1*sayi2

def bol(sayi1,sayi2):
    return sayi1/sayi2

print("OPERASYON")
print("1:Toplama")
print("2:Çıkarma")
print("3:Çarpma")
print("4:Bölme")

secenek=input("Operasyon Seçiniz..")

sayi1 =int(input("Birinci Sayıyı Giriniz: "))
sayi2 =int(input("İkinci Sayıyı Giriniz: "))

if secenek=="1":
    print("Toplam =" + str(topla(sayi1,sayi2)))
    
elif secenek=="2":
    print("Çıkarma =" + str(cikar(sayi1,sayi2)))
elif secenek=="3":
    print("Carpma =" + str(carp(sayi1,sayi2)))
elif secenek=="4":
    print("Bölme =" + str(bol(sayi1,sayi2)))    

else:
    print("Operasyon Seçimi Hatalıdır!!")





