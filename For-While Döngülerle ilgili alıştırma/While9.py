#Negatif sayı girince sonlanan döngüdeki sayıların toplamının bulunması

toplam = 0

while True:
    sayi = int(input("Bir sayı girin (Negatif sayı girerek çıkış yapabilirsiniz): "))

    if sayi < 0:
        break

    toplam += sayi

print("Girilen sayıların toplamı:", toplam)
