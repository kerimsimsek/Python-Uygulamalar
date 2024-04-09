#5’e basana kadar kapanmayan programın, Girilen sayı kadar ekrana * yazdırılması 
def yildiz_yazdirma():
    while True:
        sayi = input("Bir sayı girin (Çıkmak için '5' tuşuna basın): ")

        # '5' tuşuna basıldığında döngüyü sonlandır
        if sayi == '5':
            break

        # Girilen sayı kadar yıldız (*) yazdır
        for _ in range(int(sayi)):
            print('*')

# Yıldız yazdırma işlemi için
yildiz_yazdirma()