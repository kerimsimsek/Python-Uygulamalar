#1′den 100′e kadar olan çift sayıların toplamının bulunması 
toplam = 0
sayi = 1

while sayi <= 100:
    if sayi % 2 == 0:
        toplam += sayi
    sayi += 1

print("1'den 100'e kadar olan çift sayıların toplamı:", toplam)