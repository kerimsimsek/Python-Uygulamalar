#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
sayı1 = int (input("Birinci Sayıyı Girin :"))
sayı2 = int (input("İkinci Sayıyı Girin :"))
sayı1,sayı2 = sayı2,sayı1
print("Birinci sayı : {} \n İkinci sayı : {}".format(sayı1,sayı2))