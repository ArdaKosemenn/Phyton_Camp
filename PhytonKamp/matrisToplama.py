#Elde iki matris var bu iki matrisi toplayarak sonuc olarak yazdıran program.(1.sütün+ 2.matris 1. sütun topamı 4)
#MATRİS 1
#1 3 5 
#2 4 1 
#1 5 7 
#MATRİS 2
#3 3 4
#2 4 1 
#3 5 4

#TOPLAMI:
#4 6 9 
#4 8 2 
#4 10 11  

x = [[1,3,5],[2,4,1],[1,5,7]]
y = [[3,3,4],[2,4,1],[3,5,4]]

sonuc=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j]+y[i][j]
print(sonuc)