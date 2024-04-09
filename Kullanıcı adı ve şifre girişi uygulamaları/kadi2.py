print("""
***************************
Kullanıcı Girişi
***************************
""")

kadi = "fatih"
parola = "1453"

kadii = input("Kullanıcı Adınızı Giriniz :")
parolaa = input("Parolanızı Giriniz :")

if (kadii == kadi and parolaa != parola):
    print("Parola yanlış")

elif (kadii != kadi and parolaa == parola):
    print("Kullanıcı adı yanlış")

elif (kadii != kadi and parolaa != parola):
    print("Kullanıcı adı ve Parola yanlış")

else:
    print("Sisteme Giriş Yaptınız")