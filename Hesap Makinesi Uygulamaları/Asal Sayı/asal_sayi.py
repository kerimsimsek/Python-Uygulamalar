def asalmi (sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range (2,sayi):
            if sayi % i == 0:
                return False
        return True
while True:
    sayi = input("Sayı gir :")
    if sayi == "q":
        break

    else:
        sayi = int(sayi)
        if asalmi(sayi):
            print("Sayı asaldır.")
        
        else:
            print("Sayı asal değildir.")