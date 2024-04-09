print("""*******************************
NOT ORTALAMASI
*******************************
""")
a = float(input("Birinci Vize Notunuzu Giriniz : "))
b = float(input("İkinci Vize Notunuzu Giriniz  : "))
c = float(input("Final Notunuzu Giriniz        : "))

vize1 = a / 100 * 30
vize2 = b / 100 * 30
final = c / 100 * 40

sonuc = vize1 + vize2 + final

if sonuc >= 90:
    print("Sayı ile : {}\nRakam ile : AA\nDurum : Geçti".format(sonuc))

elif sonuc >= 85:
    print("Sayı ile : {}\nRakam ile : BA\nDurum : Geçti".format(sonuc))

elif sonuc >= 80:
    print("Sayı ile : {}\nRakam ile : BB\nDurum : Geçti".format(sonuc))

elif sonuc >= 75:
    print("Sayı ile : {}\nRakam ile : CB\nDurum : Geçti".format(sonuc))

elif sonuc >= 70:
    print("Sayı ile : {}\nRakam ile : C\nDurum : GeçtiC".format(sonuc))

elif sonuc >= 65:
    print("Sayı ile : {}\nRakam ile : DC\nDurum : Geçti".format(sonuc))

elif sonuc >= 60:
    print("Sayı ile : {}\nRakam ile : DD\nDurum : Geçti".format(sonuc))

elif sonuc >= 55:
    print("Sayı ile : {}\nRakam ile : FD\nDurum : Geçti".format(sonuc))

elif sonuc < 50:
    print("Sayı ile : {}\nRakam ile : FF\nDurum : Kaldı".format(sonuc))