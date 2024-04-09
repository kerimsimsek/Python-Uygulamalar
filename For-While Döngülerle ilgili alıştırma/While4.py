#Dinamik diziye veri girilmesi yazdırılması
# Boş bir liste oluştur
dinamik_dizi = []

# Kullanıcıdan veri girişi almak için bir while döngüsü kullan
while True:
    veri = input("Veri girin (Çıkmak için 'q' tuşuna basın): ")

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if veri.lower() == 'q':
        break

    # Girilen veriyi dinamik dizinize ekle
    dinamik_dizi.append(veri)

# Dinamik diziyi yazdır
print("Dinamik Dizi:")
for eleman in dinamik_dizi:
    print(eleman)
