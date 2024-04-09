"""
BEN YAZDIM

print("Asansör'e bindiniz.")

asansör_no = 0
hedef_konum = 0

while True:
    yon = input("Yukarı mı Aşağa mı gitmek istiyorsunuz?(Y/A) : ")
    asansör_no = input("Şuan giriş kattasınız kaçıncı kata çıkmak istiyorsunuz? : ")
    yon=yon.lower()
    if asansör_no == "0":
        print("Zaten giriş kattasınız.")
        
    elif asansör_no == "1" and yon == "y":
        print("1. Kata çıkılıyor.")

        print("Şuan 1. Kattasınız.")

    elif asansör_no == "1" and yon == "a":
        print("1. Kata iniyorsunuz.")

        print("Şuan 1. Kattasınız.")

    elif asansör_no == "2" and yon == "y":
        print("2. Kata çıkılıyor.")

        print("Şuan 2. Kattasınız.")
    
    elif asansör_no == "2" and yon == "a":
        print("2. Kata iniyorsunuz.")

        print("Şuan 2. Kattasınız.")

    elif asansör_no == "3":
        print("3. Kata çıkılıyor.")

        print("Şuan 3. Kattasınız.")

    elif asansör_no == "3" and yon == "a":
        print("3. Kata iniyorsunuz.")

        print("Şuan 3. Kattasınız.")
        
"""

"""
CHATGPT YAZDI

class Asansor:
    def __init__(self, toplam_kat_sayisi):
        self.toplam_kat_sayisi = toplam_kat_sayisi
        self.mevcut_kat = 1

    def hareket_et(self, hedef_kat):
        if 1 <= hedef_kat <= self.toplam_kat_sayisi:
            self.mevcut_kat = hedef_kat
            print(f"Asansör {self.mevcut_kat}. kata gitti.")
        else:
            print("Geçersiz kat numarası.")

def main():
    kat_sayisi = int(input("Asansörün olduğu toplam kat sayısını girin: "))
    asansor = Asansor(kat_sayisi)

    while True:
        print("\nMevcut kat:", asansor.mevcut_kat)
        hedef_kat = int(input("Gitmek istediğiniz kata bir sayıyla belirtin (Çıkış için '0' girin): "))

        if hedef_kat == 0:
            print("Çıkış yapılıyor. İyi günler!")
            break

        asansor.hareket_et(hedef_kat)

if __name__ == "__main__":
    main()
"""

#HOCA YAZDI

bulunduğu_konum = 0

while True:
    print(f"Bulunduğunuz kat {bulunduğu_konum}. kat")
    hedef_konum = int(input("Hedef katı giriniz (Çıkmak için '0' girin): "))

    if hedef_konum == 0:
        print("Çıkış yapılıyor. İyi günler!")
        break
    
    if hedef_konum == bulunduğu_konum:
        print("Zaten bu kattasınız.")
    
    elif hedef_konum > bulunduğu_konum:
        print("Asansör yukarı çıkıyor.")
        bulunduğu_konum = hedef_konum
    
    elif hedef_konum < bulunduğu_konum:
        print("Asansör aşağı iniyor.")
        bulunduğu_konum = hedef_konum
