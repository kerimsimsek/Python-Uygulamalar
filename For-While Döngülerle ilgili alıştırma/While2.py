#Dinamik dizi oluşturma, kapasite belirleme, ekrana yazdırılma
kapasite = int(input("Dizi kapasitesini belirleyin: "))
dizi = []

while True:
    deger = int(input("Diziye eklemek için bir değer girin : "))
    dizi.append(deger)

    if len(dizi) == kapasite:
        print("Dizi kapasitesine ulaşıldı. Dizi şu anki hali:", dizi)
        break
print(dizi)