import random
import time

class kumanda():

    def __init__(self,tv_durum = "kapalı",tv_ses = 0,kanal_listesi = ["TRT"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac (self):
        if self.tv_durum == "açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "açık"
    
    def tv_kapat (self):
        if self.tv_durum == "kapalı":
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum = "kapalı"

    def tv_ses_ayarlari (self):
        while True:
            cevap = input("Sesi arttırmak için : '+'\nSesi azaltmak için : '-'\nÇıkış için : Çıkış")
            if cevap == "-":
                if self.tv_ses != 0:
                    self.tv_ses -=1
                    print("Ses :",self.tv_ses)
                
            elif cevap == "+":
                if self.tv_ses != 20:
                    self.tv_ses += 1
                    print("Ses :",self.tv_ses)
            else:
                print("Ses güncellendi :",self.tv_ses)
                break

    def kanal_ekle (self,kanal_ismi):
        print("Kanal ekleniyor...",kanal_ismi)
        time.sleep(1)
        print("Kanal eklendi")
        self.kanal_listesi.append(kanal_ismi)
        

    def rastgele_kanal (self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal :",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv durumu :{}\n Ses seviyesi :{}\nKanal Listesi :{}\nŞu anki Kanal :{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
Kumanda = kumanda()
print(""" 
---------------------
TELEVİZYON UYGULAMASI 
---------------------

1. TV AÇ

2. TV KAPAT

3. SES AYARLARI

4. KANAL EKLE

5. KANAL SAYISINI ÖĞRENME

6. RASTGELE KANALA GEÇME

7. TELEVİZYON BİLGİLERİ

ÇIKMAK İÇİN 0'I TUŞLAYINIZ

""")
while True:

    islem = int(input("İşlem seçiniz :"))

    if islem == 0:
        print("Uygulamadan çıkılıyor...")
        time.sleep(1)
        print("Çıkış Yapıldı.")
        break

    elif islem == 1:
        Kumanda.tv_ac()

    elif islem == 2:
        Kumanda.tv_kapat()

    elif islem == 3:
        Kumanda.tv_ses_ayarlari()

    elif islem == 4:
        kanal_isimleri = input("Kanal isimlerini ',' ayırarak giriniz :")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            Kumanda.kanal_ekle(eklenecekler)

    elif islem == 5:
        print("Kanal sayısı :",len(Kumanda))

    elif islem == 6:
        Kumanda.rastgele_kanal()

    elif islem == 7:
        print(Kumanda)
    else:
        print("Geçersiz işlem")