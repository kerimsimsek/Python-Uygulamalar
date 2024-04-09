top_alisveris = 0

print("ALIŞVERİŞ UYGULAMASINA HOŞGELDİNİZ")
while True:
    ürün_fiyatı = input("Ürün fiyatını giriniz: ")
    top_alisveris += int(ürün_fiyatı)
    if ürün_fiyatı =="0":
        break

kdv_ücreti = top_alisveris+top_alisveris*0.18
print("Toplam alışveriş tutarınız :",top_alisveris)
print("Kdv'li fiyat : ",kdv_ücreti)
print("KDV ücreti",top_alisveris*0.18)