#Metotlarla “5” e basana kadar çarpma / toplama işlemi yapılması
def toplama_islemi():
    toplam = 0
    while True:
        sayi = input("Bir sayı girin (Çıkmak için '5' tuşuna basın): ")

        # '5' tuşuna basıldığında döngüyü sonlandır
        if sayi == '5':
            break

        # Girilen sayıyı toplama işlemine ekle
        toplam += int(sayi)

    return toplam

def carpma_islemi():
    carpim = 1
    while True:
        sayi = input("Bir sayı girin (Çıkmak için '5' tuşuna basın): ")

        # '5' tuşuna basıldığında döngüyü sonlandır
        if sayi == '5':
            break

        # Girilen sayıyı çarpma işlemine ekle
        carpim *= int(sayi)

    return carpim

# Toplama işlemi için
toplam_sonuc = toplama_islemi()
print(f"Toplam: {toplam_sonuc}")

# Çarpma işlemi için
carpim_sonuc = carpma_islemi()
print(f"Çarpım: {carpim_sonuc}")
