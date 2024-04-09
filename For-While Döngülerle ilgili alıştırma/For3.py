#100 ile 200 Arasındaki Çift Sayıların Toplamının Ortalamasının bulunması
cifttoplam = 0
adet = 0
for i in range(100,200+1):
    if i % 2 == 0:
        cifttoplam += i
        adet += 1

ortalama = cifttoplam / adet
print(f"Çift 100 ile 200 arasındaki çift sayıların toplamı : {cifttoplam}")
print(f"Çift 100 ile 200 arasındaki çift sayıların ortalaması : {ortalama}")