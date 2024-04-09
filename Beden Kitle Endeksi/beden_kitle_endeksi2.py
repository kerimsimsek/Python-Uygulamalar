"""Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) """

sayı1 = int (input("Kilonuzu Giriniz :"))
sayı2 = float (input("Boyunuzu Giriniz :"))
indeks = sayı1 / (sayı2 ** 2)
print("Beden Kitle İndeksi :",indeks)