class Matematik: #Class:O rtak operasyonları bir arada tutmak için kullanılır.
    def __init__(self,sayi1,sayi2):#contructor  -yapıcı blok init ile başlatıyorsun.(BURADA SELF ASLINDA MATEMATİK CLASSININ
        #KENDİSİDİR
        #PYTHON DA CLASS KULLANIRKEN SELF KULLANMAK ZORUNLU MATEMATİK İLE 
        # İLGİLKİ KENDİN İŞLEM YAPMAK İSTEYEBİLİRSİN DİYE SELFİ ZORUNLU KILIYOR.
        self.s1=sayi1 #burdaki selflerin anlamı aslında 
        self.s2=sayi2
        print("Matematik başladı(referans oluşturdu)") # bu koda yapıcı blok denir. Örneğin Matematik() kodundaki parantezin aslında bu blok çalışıyor.
    def topla(self,):
        return self.s1+self.s2
    def cikar(self,):
        return self.s1-self.s2
    def bol(self,):
        return self.s1/self.s2
    def carp(self,):
        return self.s1*self.s2
    
matematik= Matematik(6,7) #BİR TANE REFERANS ADRESİ OLUŞTUR DEMEK
sonuc= matematik.bol()

print("Sonuc : " + str(sonuc))

#İNDENTETİON:BOŞLUK BIRAKMA DEMEK.YANİ BİR CLASS OLUŞTURDUĞUMUZDA KODUN BİR ALTINA OTO BOŞLUK BIRAKIR.
class İstatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
        def varyansHesaplama(self):
            return self.s1*self.s2 
    
##İNHERİTANCE  ARAŞTIR!!  MİRAS ALMA
#NOT!! MİRAS ALMA 1 SINIFTAN 1 MİRAS ALABİLİR
    
İstatistik=İstatistik(5,8)