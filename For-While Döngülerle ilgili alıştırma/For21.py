#Bir kişinin maaşı her seferinde yüzde 20 arttırılarak 5 kez alındığında, toplam zam miktarını hesaplamak
maas = 1000
for i in range(5):
    maas += maas * 0.20
print("5. ayının sonunda kişinin maaşı:", maas)