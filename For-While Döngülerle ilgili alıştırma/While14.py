#Klavyeden H’ye basılmadığı sürece toplama işleminin yapılması
toplam = 0

while True:
    sayi = int(input("Bir sayı girin (Toplamak için, çıkmak için 'H' tuşuna basın): "))

    toplam += sayi

    if input("Devam etmek istiyor musunuz? (Eğer çıkmak istiyorsanız 'H' tuşuna basın): ").upper() == 'H':
        break

print("Girilen sayıların toplamı:", toplam)
