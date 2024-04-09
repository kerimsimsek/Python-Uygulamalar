"""

arabanın yakıtı 100 km 5 litre yakıyor.

arabanın deposu 50 litre 

depoyu 5 litre ile böl

çıkan sonuç 10 bu sonucuda 100 km ile çarptığımda 1000 km yapıyor.

yani bu araba full depo ile 1000 km yol yapıyor.

ben 1400 kilometre yol gidecek isem 1400 - 1000 = 400 km yol kalıyor ve tekrar benzin almam gerekiyor.

bir kez daha benzini ful dolduruyorum. ve 400 km bittiğinde 600 km'lik benzinimin kaldığını buluyorum.

benzin fiyatı 40 tl olduğundan iki kez benzini fullediğim için 40*depo(50) =2000 tl.*2 = 4000 tl.

yani 1400 km yol için 4000tl benzin masrafım var.

"""

# Kullanıcı girdileri
yakit_tuketimi_100km = float(input("Araba 100 km'de ne kadar yakıyor? : "))  # 100 km başına yakıt tüketimi (litre)
depo_kapasitesi = int(input("Arabanın depo kapasitesini giriniz : "))  # Depo kapasitesi (litre)
yol_uzunlugu = int(input("Gidilecek yol uzunlugunu giriniz (km olarak): "))  # Yol uzunluğu (km)
benzin_fiyati = float(input("Benzinin fiyatını giriniz : "))  # Benzin fiyatı (TL)

# Full depo ile gidilebilecek mesafe
full_depo_ile_mesafe = (depo_kapasitesi / yakit_tuketimi_100km) * 100

# Toplam benzin alım sayısı
benzin_alim_sayisi = yol_uzunlugu // full_depo_ile_mesafe
if yol_uzunlugu % full_depo_ile_mesafe > 0:
    benzin_alim_sayisi += 1

# Yolculuk sonunda kalan benzin miktarı
kalan_benzin = benzin_alim_sayisi * depo_kapasitesi - (yol_uzunlugu / 100 * yakit_tuketimi_100km)

# Toplam maliyet hesaplama
toplam_maliyet = benzin_alim_sayisi * depo_kapasitesi * benzin_fiyati

# Arabayı full benzin ile bırakmam için almam gereken litre ve maliyeti
ekstra_benzin = depo_kapasitesi - (kalan_benzin % depo_kapasitesi)
ekstra_maliyet = ekstra_benzin * benzin_fiyati

# Sonuçları yazdır
print(f"Bu yolculuk için toplam {benzin_alim_sayisi} kez benzin alınacak.")
print(f"Yolculuğun sonunda {kalan_benzin:.2f} litre benzin kalacak.")
print(f"Toplam benzin masrafı: {toplam_maliyet:.2f} TL olacak.")
print(f"Arabayı full benzin ile bırakmak için {ekstra_benzin:.2f} litre benzin alınmalı ve bu {ekstra_maliyet:.2f} TL maliyet oluşturacaktır.")
