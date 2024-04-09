#Alfabenin yazdırılması
# ASCII kodları kullanarak alfabe oluşturulur
alfabe = ""
# ord komutu harfin sayısal halidir.
for harf in range(ord('A'), ord('Z')+1):
    # chr komutu ile harfi sayısal halinden karakter haline dönüştürüyoruz.
    alfabe += chr(harf)

# Elde edilen alfabe ekrana yazdırılır
print(alfabe)
