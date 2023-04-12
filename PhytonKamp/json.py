##JSON NEDİR?
#JSON sistemi veri depolamak için kullanılan ve çoğunlukla bir sunucu ile istemci arasında olan formata verilen isimdir. 
# JSON dosyaları, XML dosyalarının çok daha basit ve hafif alternatifleri olarak bilinir. 
# Bu format depolanmış olan verinin eş zamansız bir şekilde yüklenmesi adına uyumlu olarak çalışmaktadır.


import json
data='{"firstName":"Arda","lastName":"Kösemen"}'

y=json.loads(data)     #datayı jsona çeviriyoruz.
print(y["firstName"])
print(y["lastName"])

customer={
    "firstName":"arda",
    "e-mail":"ardakosemen@gmail.com"
    }

customerJson=json.dumps(customer)#üsteki sözlüğü jsona çevirmek. pyton nesnelerini jsona çevirmek için dumps kullanır.
print(customer)

print(json.dumps("Arda"))