a = int(input("Sayı Girin :"))
b = int(input("Sayı Girin :"))
c = int(input("Sayı Girin :"))

if a >= b and a >= c:
    print("En büyük sayı : {}".format(a))

elif b >= a and b >= c:
    print("En büyük sayı : {}".format(b))

elif c >= a and c >= b:
    print("En büyük sayı : {}".format(c))