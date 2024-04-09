import random

import time

print(""" ***********************************
        Sayı Tahmin Oyunu

1 ve 40 arasında bir sayı girin.
***********************************
""")

rastgalesayi = random.randint(1,40)
tahminhakki = 7
while True:
    tahmin = int(input("Tahmininizi girin :"))

    if tahmin < rastgalesayi:
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin")
        tahminhakki -= 1

    elif tahmin > rastgalesayi:
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin")
        tahminhakki -= 1
    
    else:
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("Tebrikler sayınız :",rastgalesayi)
        break

    if tahminhakki == 0:
        print("Tahmin hakkınız bitti")
        print("Tebrikler sayınız :",rastgalesayi)
        break
       