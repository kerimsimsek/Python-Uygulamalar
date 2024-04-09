#Kullanıcı Adı ve Şifre girişi
kullanıcı_adı = ["istanbul"]
sifre = ["123","456","789","765","098"]

sifre1 = input("şifreyi gir: ")
for i in range(0,4):
    if sifre1 == sifre[1]:
        print("şifre başarılı")
        break
    else:
        print("Şifre yanlış")
        sifre1 = (input("Şifre gir: "))
        if i == 3:
            print("Şifre bloke oldu")
            break