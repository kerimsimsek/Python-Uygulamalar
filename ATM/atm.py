print("""************************************
Bakiye Sorgulamak İçin 1'i Tuşlayınız.

Para Yatırmak İçin 2'yi Tuşlayınız.

Para Çekmek İçin 3'ü Tuşlayınız.
************************************
""")

bakiye = 1000

while True:
    islem = input("İşlem Numarası Giriniz :")

    if islem == "q":
        print("Yine Bekleriz...")
        break

    elif islem == "1":
        print("Bakiyeniz : {} ₺'dir".format(bakiye))
    
    elif islem == "2":
        miktar = int(input("Miktarı Giriniz :"))
        bakiye = bakiye + miktar
    
    elif islem == "3":
        miktar = int(input("Miktarı Giriniz :"))
        if bakiye - miktar < 0:
            print("Bakiyedeki Miktardan Fazla Miktar Girdiniz")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem Numarası Girdiniz")