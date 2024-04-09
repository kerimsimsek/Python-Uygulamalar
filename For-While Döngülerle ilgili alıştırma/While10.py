#Saat yazılınca şuan ki saatin gösterilmesi
import datetime

while True:
    komut = input("Saat bilgisini görmek için 'saat' yazın (Çıkmak için 'q' tuşuna basın): ")

    if komut.lower() == 'q':
        break

    if komut.lower() == 'saat':
        suanki_saat = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Şu anki saat: {suanki_saat}")
    else:
        print("Geçersiz komut. 'saat' yazarak saat bilgisini görebilirsiniz.")