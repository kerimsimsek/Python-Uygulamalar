sayı1 = int (input("Kilonuzu Giriniz :"))
sayı2 = float (input("Boyunuzu Giriniz :"))
indeks = sayı1 / (sayı2 ** 2)

if indeks <= 18.5:
    print("Beden Kitle İndeksi : {}\n Sonuç: Zayıfsınız".format(indeks))

elif indeks <= 25:
    print("Beden Kitle İndeksi : {}\n Sonuç: Normalsiniz".format(indeks))

elif indeks <= 30:
    print("Beden Kitle İndeksi : {}\n Sonuç: Fazla Kilolusunuz".format(indeks))

else:
    print("Beden Kitle İndeksi : {}\n Sonuç: Obezsiniz".format(indeks))