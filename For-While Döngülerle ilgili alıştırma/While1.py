#While ile dinamik dizi oluşturma, kapasite belirleme, ekrana küçükten büyüğe sıralanma
def sirala_dizi(dizi):
    return sorted(dizi) #sorted küçükten büyüğe sıralı dizi

kapasite = int(input("Dizi kapasitesini belirleyin: "))
dizi = []

while True:
    deger = int(input("Diziye eklemek için bir değer girin : "))
    dizi.append(deger)

    if len(dizi) == kapasite:
        print("Dizi kapasitesine ulaşıldı. Dizi şu anki hali:", dizi)
        break

siralanmis_dizi = sirala_dizi(dizi)
print("Dizi küçükten büyüğe sıralı hali:", siralanmis_dizi)
