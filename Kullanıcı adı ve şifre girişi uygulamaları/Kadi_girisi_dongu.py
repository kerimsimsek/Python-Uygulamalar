print("""
****************************************
Cafcaflı Kullanıcı Girişine Hoşgeldiniz
****************************************
""")
sys_kadi = "Şerafettin"
sys_parola = "1907"

giris_hakki = 3

while True:
    kadi = input("Kullanıcı Adını Gir Reis :")
    parola = input("Parolanı Gir Reis :")

    if kadi != sys_kadi and parola == sys_parola:
        print("Kullanıcı Adını Yanlış Girdin Reis")
        giris_hakki -= 1
   
    elif kadi == sys_kadi and parola != sys_parola:
        print("Parolanı Yanlış Girdin Reis")
        giris_hakki -= 1

    elif kadi != sys_kadi and parola != sys_parola:
        print("Kullanıcı Adını ve Parolanı Yanlış Girdin Reis")
        giris_hakki -= 1
    
    else:
        print("Sisteme Giriş Yaptın Reis")
        break

    if giris_hakki == 0:
        print("Baktın Olmuyor Zorlamayacaksın Reis")
        break