#Girilen değer kadar çarpım tablosunun oluşturulması
a = int(input("Sayı girin : "))
b = int(input("Kaça kadar çarpılmasını istiyorsunuz? : "))
for i in range(b+1):
    sonuc = a * i
    print(f"{a} x {i} = {sonuc}")