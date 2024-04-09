#Klavyeden girilen 5 sayının toplamının bulunması
b = 1
top = 0
for i in range(5):
    a = int(input(f"{b}. Sayı gir : "))
    b += 1
    top += a
print(top)
