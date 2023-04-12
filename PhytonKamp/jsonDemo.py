#JSON DOSYASINI OKUMAK

import json

with open("users.json") as users:#Burda verdiğin isim fark emtez(users yani as ın sağındaki)
    data=json.load(users) #dosyayı okuma
    print(data[0]["username"]) # sıfırıncı datanın sadece ismini bulamk için.
    print(data[0]["email"])# sıfırıncı datanın sadece e-mailini bulamk için.
    print(data[0]["address"]["street"])# 0. datanın adresinin sokağı
    print(data[0]["address"]["street"]["geo"]["lat"])

#For döngüsü ile ilk 5 datanın üsteki bilgilerini almak için

for x in range(5):
    print(data[x]["username"]) # sıfırıncı datanın sadece ismini bulamk için.
    print(data[x]["email"])# sıfırıncı datanın sadece e-mailini bulamk için.
    print(data[x]["address"]["street"])
    print(data[x]["address"]["street"]["geo"]["lat"])


