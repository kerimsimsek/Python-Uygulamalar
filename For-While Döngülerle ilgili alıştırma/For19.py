#Bir metin dizisindeki harfleri tersten ekrana yazdırmak için nasıl bir for döngüsü kullanılır?
metin = "CUMHURİYET"
ters_metin = ""
for karakter in reversed(metin):
    ters_metin += karakter
print(ters_metin)