
##BİRİNCİ YÖNTEM
#import matematikModule

#matematikModule.carp(4,8)
#matematikModule.topla(4,8)

#İKİNCİ YÖNTEM

import matematikModule as mm
mm.carp(4,8)
mm.topla(4,8)

print(mm.customer["lastName"])

#SADECE BİR FONKSİYON ÇAĞIRMAK İSTEDİĞİMİZ ZAMAN İSE 

from matematikModule import topla

topla(2,4)

from matematikModule import customer
print(customer["firstName"])
