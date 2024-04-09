#1 ile 1000 Arasındaki Sayıların Toplamının Ortalamasının bulunması

toplam = 0
ort = 0

for i in range(1001):
    toplam += i

ort = toplam / 1000

print(f"1OOO'ne kadar olan sayıların toplamı : {toplam}\n1000'ne kadar olan sayıların ortalaması {ort}")