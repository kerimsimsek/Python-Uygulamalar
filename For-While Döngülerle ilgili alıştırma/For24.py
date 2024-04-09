#Vize ve Final notunun ortalamasının alınması
vize = []
final = []

for i in range(3):
    vize.append(int(input("{}. öğrencinin vize notunu girin: ".format(i+1))))
    final.append(int(input("{}. öğrencinin final notunu girin: ".format(i+1))))

for i in range(3):
    ortalama =(vize[i]*0.4)+(final[i]*0.6)
    print("{}. öğrencinin ortalama notu: {}".format(i+1,ortalama))


