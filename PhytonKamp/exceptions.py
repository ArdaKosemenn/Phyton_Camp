#HATA YAKALAMA
#Programı yazdıp bittiği zaman bir hata oluşumunda try ve except kullanarak nerede hata olduğunu anlayabilirz.
#yani programın kırılmasını önler

try:
    sayi=int(input("Bir sayı giriniz:"))
except ValueError:
    print("Tip uyuşmazlığı:Lütfen tekrar deneyiniz.")
except ZeroDivisionError:
    print("Payda sıfır olamaz")
except:
    print("Bir hata oluştu")
    
print("Bitti")