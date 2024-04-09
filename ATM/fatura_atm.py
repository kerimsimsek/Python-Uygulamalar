import time
print("""------------------------
ŞİMŞEK BANKA HOŞGELDİNİZ
------------------------
 
0.Bakiye
1.Para Yatır 
2.Para Çek
3.Para Gönder
4.Bana Hesabının Bakiyesini Sorgulama
5.Fatura Sorgulama
9.Çıkış""")
bakiye = 1001
bana = 0
su = 75
dogalgaz = 50
elektrik = 200
internet = 104
telefon = 40
while True:
    
    a = input("işlem numarası girin : ")
    
    if a == "0":
        print("\nBakiyeniz :",bakiye)
        
    elif a == "1":
        mik = int(input("Miktar girin : "))
        bakiye += mik
        print("Para yatırıldı.")
        
    elif a == "2":
        tar = int(input("Miktar girin : "))
        if bakiye - tar < 0:
            print("Bakiyedeki paradan fazla para girdiniz")
            continue
        bakiye -= tar
        print("Para çekildi")
        
    elif a == "3":
        nap = int(input("Gönderilecek miktar : "))
        bana = nap
        bakiye -= nap
    
    elif a =="4":
        print("Bana hesabındaki bakiye :",bana)
        
    elif a =="5":
        print("\nSu için ödenecek miktar :",su,"\nDoğalgaz için ödenecek miktar :",dogalgaz,"\nElektrik için ödenecek miktar :",elektrik,"\nİnternet için ödenecek miktar :",internet,"\nTelefon için ödenecek miktar :",telefon)
        print("\nFatura Ödemek için 6'yı tuşlayınız")
    elif a == "6":
        print("\nSu için : 99\nDoğalgaz için : 98\nElektrik için :97\nİnternet için :96\nTelefon için :94")
        fod = input("Ödemek istediğiniz faturanın kodunu giriniz : ")
        if fod == "99":
            miktar = int(input("Faturanızın ödenecek miktarını giriniz : "))
            bakiye -= miktar
            su -= miktar
            time.sleep(1)
            print("Su faturanız ödenmiştir.\nBorç : {}₺".format(su))
        elif fod == "98":
            miktar = int(input("Faturanızın ödenecek miktarını giriniz : "))
            bakiye -= miktar
            dogalgaz -= miktar
            time.sleep(1)
            print("Doğalgaz faturanız ödenmiştir.\nBorç : {}₺".format(dogalgaz))
        elif fod == "97":
            miktar = int(input("Faturanızın ödenecek miktarını giriniz : "))
            bakiye -= miktar
            elektrik -= miktar
            time.sleep(1)
            print("Elektrik faturanız ödenmiştir.\nBorç : {}₺".format(elektrik))
        elif fod == "96":
            miktar = int(input("Faturanızın ödenecek miktarını giriniz : "))
            bakiye -= miktar
            internet -= miktar
            time.sleep(1)
            print("İnternet faturanız ödenmiştir.\nBorç : {}₺".format(internet))
        elif fod == "95":
            miktar = int(input("Faturanızın ödenecek miktarını giriniz : "))
            bakiye -= miktar
            telefon -= miktar
            time.sleep(1)
            print("Telefon faturanız ödenmiştir.\nBorç : {}₺".format(telefon))
    elif a == "9":
        print("\nÇıkış yapılıyor.")
        time.sleep(1)
        print("\nYine bekleriz.")
        break