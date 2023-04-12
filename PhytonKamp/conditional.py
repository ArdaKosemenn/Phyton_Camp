#Örnek:Bankadan 100bin almak için hesabında en az 10bin olması lazım.

istenenkredi = 100000
hesap = 9555
minimumolmasıgerekenhesap = 10000

if hesap>=minimumolmasıgerekenhesap: #İf Else de birden fazla şart varsa Elif kullanılır.
    print ("Kredi Verilebilir")#İNDENTETİON:BOŞLUK BIRAKMA DEMEK.YANİ BİR CLASS OLUŞTURDUĞUMUZDA KODUN BİR ALTINA OTO BOŞLUK BIRAKIR.
    print ("Ödemeler Hesaplandı")
elif hesap>=9000 and hesap<=9500:#eşittir kullanmak için;"==" olarak kullanılırız.
    print("Müdüre Sorulacak")    
elif hesap>=9501 and hesap<=9999:
    print("Genel Müdüre Sorulacak")  
else:
    print("Kredi Almak İçin Bakiyeniz Yetersiz!!")
