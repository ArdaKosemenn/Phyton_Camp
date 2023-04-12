

isimler=["Arda","Mehmet","Salih","Ali","Ayşe","Nisa"]

fileToAppend= open("isimler.txt","a")

for isim in isimler:
    fileToAppend.write(isim)
    fileToAppend.write("\n")

fileToAppend.close()

#import os
#os.remove("isim.txt")

