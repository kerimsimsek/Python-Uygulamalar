#Dinamik diziye veri ekleme ve ekrana yazdırılma
# Boş bir liste oluştur
dinamik_dizi = []

# Kullanıcıdan veri al ve dinamik diziye ekle
while True:
    veri = input("Dinamik diziye eklemek için bir veri girin (Çıkmak için 'q' tuşuna basın): ")
    
    if veri.lower() == 'q':
        break
    
    dinamik_dizi.append(veri)

# Eklenen verileri ekrana yazdır
print("Dinamik Dizi:", dinamik_dizi)
