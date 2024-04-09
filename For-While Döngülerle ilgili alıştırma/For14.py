#Klavyeden girilen sayı kadar ekrana “Türkiye” Yazılması
a = input("Bir yazı gir : ")
b = int(input("Kaç defa yazdırılsın : "))
c = 0
for i in range(b):
    c += 1
    print(f"{c} - {a}")