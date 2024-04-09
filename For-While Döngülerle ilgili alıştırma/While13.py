#Klavyeden 15 girilene kadar sayıları toplayıp sonucu ekrana yazdırılması
toplam = 0

while True:
    sayi = int(input("Bir sayı girin (Çıkmak için '15' tuşuna basın): "))

    toplam += sayi

    if sayi == 15:
        break

print("Girilen sayıların toplamı:", toplam)
