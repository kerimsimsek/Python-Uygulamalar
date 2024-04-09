#80 ve üzeri not alan öğrencileri ekrana yazdırma
ögrenci_listesi=["ali","melike","burhan","vahdettin","tarkan"]
notlar=[50,60,70,80,90]
for i in range(len(notlar)): #RANGE 5 YAZMAK YERİNE LEN KOMUTU KULLANMAK DAHA AVANTAJLI
    if notlar[i] >=80:
        print("{} notu :{}".format(ögrenci_listesi[i],notlar[i]))