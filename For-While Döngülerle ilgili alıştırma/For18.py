#Bir sözlükteki anahtarları ve değerleri sıralı bir şekilde ekrana yazdırmak için nasıl bir for döngüsü kullanılır?
sözlük = {'anahtar1':'değer1','anahtar2':'değer2','anahtar3':'değer3'}
for anahtar,deger in sözlük.items():
    print(f"{anahtar} : {deger}")