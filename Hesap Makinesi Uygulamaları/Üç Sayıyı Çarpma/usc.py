#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
sayı1 = int ( input ("Birinci Sayıyı Giriniz :"))
sayı2 = int ( input ("İkinci Sayıyı Giriniz :"))
sayı3 = int ( input ("Üçüncü Sayıyı Giriniz :"))
çarpma = sayı1*sayı2*sayı3
print(" {} x {} x {} = {}".format(sayı1,sayı2,sayı3,çarpma))