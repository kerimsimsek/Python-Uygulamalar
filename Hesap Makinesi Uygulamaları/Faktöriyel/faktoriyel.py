print("""\n ***************** Faktöriyel Bulma *****************\n\nÇıkmak için q'ya basınız\n """)

while True:
    sayı = input("Sayı girin :")
    if sayı == "q":
        print("Programdan Çıkış Yaptınız")
        break

    else :
        sayı = int(sayı)

        faktoriyel = 1

        for i in range (2,sayı+1):
            
            print("Faktöriyel :",faktoriyel,"i :",i)
            faktoriyel *= i

        print("Faktöriyel :",faktoriyel)