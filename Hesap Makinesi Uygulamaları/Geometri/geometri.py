print("""
--------------------------------------------------
Üçgen Oluşturmak için 1. tuşlayınız.
Dörtgenin tipini öğrenmek için 2'yi tuşlayınız.
Üçgen tipini öğrenmek için 3'ü tuşlayınız.
--------------------------------------------------
""")

işlem = input("Hangi şeklin tipini öğrenmek istiyorsunuz? :")

if işlem == "1":
    ucgen1 = int(input("A Kenarını giriniz :"))
    ucgen2 = int(input("B Kenarını giriniz :"))
    ucgen3 = int(input("C Kenarını giriniz :"))
    if abs(ucgen1-ucgen2)<ucgen3<abs(ucgen1+ucgen2):
        print("Üçgen Oluşturuldu")

    elif abs(ucgen1-ucgen3)<ucgen2<abs(ucgen1+ucgen3):
        print("Üçgen Oluşturuldu")

    elif abs(ucgen3-ucgen2)<ucgen1<abs(ucgen3+ucgen2):
        print("Üçgen Oluşturuldu")

    else:
        print("Üçgen olmaz")

elif işlem == "2":
    dortgen1 = int(input("A Kenarını giriniz :"))
    dortgen2 = int(input("B Kenarını giriniz :"))
    if dortgen1 == dortgen2 :
        print("GİRDİĞİNİZ SAYILAR KAREYİ OLUŞTURDU")
    elif dortgen1 > dortgen2 or dortgen2 > dortgen1:
        print("GİRDİĞİNİZ SAYILAR DİKDÖRTGEN OLUŞTURDU")

elif (işlem == "3"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz İşlem Numarası Girdiniz.")