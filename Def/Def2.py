def login (kullanıcı_adı,sifre):
    if (kullanıcı_adı == "veri bilimi" and sifre == "12345"):
        print("Giriş başarılı")
    else:
        print("Kullanıcı adı veya şifre hatalı")

login("veri bilimi","12345")

