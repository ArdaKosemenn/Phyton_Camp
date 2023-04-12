#LİSTELERİN HATA YAKALAMA YÖNTEMİYLE HESAPLANMASI

import sys#sys koddaki hatanın ne olduğunu gösteren bir kütüphane
#örneğin listeden veriler geliyor istatistiksel bir çalısma yapacağız gelen elemanları bire böleceğiz.
#ama gelen listede bazıları str bazıları int.

#burda eğer try ve except kullamnasaydık program komple hata verirdi.Kullandığımız için 
#listedeki sayısal işlemşleri hesaplayacak, hesaplayanamanları da hata yakalama yöntemi kullandığımız
#için hata olan yerlerde bize gösterecek.


liste=[7,"arda",0,3,"6"]
for x in liste:
    try:
        print("Sayı: " + str(x)) 
        sonuc=1/int(x)
        print("Sonuç : "+ str(sonuc))
    except ValueError:
        print(str(x)+"Bir sayı değil.")
    except ZeroDivisionError:
        print(str(x)+"İçin sıfıra bölme hatası")
    except:
        print(str(x)+"Hesaplanamadı")
        print("Sistem diyor ki " + str(sys.exc_info()[0]))
    