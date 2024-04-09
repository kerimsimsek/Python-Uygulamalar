print("1 - SİNEMA \n2 - TİYATRO SEÇİN")
bakiye = 1000
sinema_bileti = 15
tiyatro_bileti = 10
while True:
    i = input("İzlemek istediğinizi seçin: ")
    ogrenci = str(input("Öğrenci misiniz?(E/H) : "))
    if i == "1" and(ogrenci == "E" or ogrenci == "e"):
        sinema_bileti = sinema_bileti * 0.5
        bakiye -= sinema_bileti
        print("Bilet ücreti : {} TL Kalan bakiye {} TL'dir".format(sinema_bileti,bakiye))
        break

    elif i == "1" and(ogrenci == "H" or ogrenci == "h"):
        bakiye -= sinema_bileti
        print("Bilet ücreti : {} TL Kalan bakiye {} TL'dir".format(sinema_bileti,bakiye))
        break
    
    elif i == "2" and(ogrenci == "E" or ogrenci == "e"):
        tiyatro_bileti = tiyatro_bileti * 0.5
        bakiye -= tiyatro_bileti
        print("Bilet ücreti : {} TL Kalan bakiye {} TL'dir".format(tiyatro_bileti,bakiye))
        break

    elif i == "2" and(ogrenci == "H" or ogrenci == "h"):
        bakiye -= tiyatro_bileti
        print("Bilet ücreti : {} TL Kalan bakiye {} TL'dir".format(tiyatro_bileti,bakiye))
        break
    else:
        print("Yanlış bir tuşa bastınız.")
            