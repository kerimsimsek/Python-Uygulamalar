def tambolenler (a):
    tambolen = []
    for i in range(2,a):
        if a % i == 0:
            tambolen.append(i)
    return tambolen

while True:
    sayi = input("Sayı gir :")
    if sayi == "q":
        print("Çıkış yaptınız")
        break

    else:
        sayi = int(sayi)
        print(tambolenler(sayi))