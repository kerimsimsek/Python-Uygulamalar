#Klavyeden çift sayı girildiği sürece sayıları toplayan,  tek sayı girilir ise döngüyü sonlandırarak sonucu ekrana yazılması
toplam = 0

while True:
    sayi = int(input("Bir sayı girin (Çift sayı girerek toplamaya devam edebilirsiniz, tek sayı girerek çıkabilirsiniz): "))

    if sayi % 2 == 0:
        toplam += sayi
    else:
        print("Tek sayı girdiniz. Döngü sona eriyor.")
        break

print("Girilen çift sayıların toplamı:", toplam)
