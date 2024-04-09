#Girilen 5 sayının toplamının bulunması
toplam = 0
sayac = 0

while sayac < 5:
    sayi = int(input("Bir sayı girin: "))
    toplam += sayi
    sayac += 1

print("Girilen 5 sayının toplamı:", toplam)
