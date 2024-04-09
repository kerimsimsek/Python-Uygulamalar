print("""
*************************************************************
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
*************************************************************
""")

sayı1 = int(input("Sayı Girin :"))
sayı2 = int(input("Sayı Girin :"))
işlem = input("İşlem Numarasını Girin :")

if işlem == "1":
    print("{} + {} = {}".format(sayı1,sayı2,sayı1+sayı2))

elif işlem == "2":
    print("{} - {} = {}".format(sayı1,sayı2,sayı1-sayı2))

elif işlem == "3":
    print("{} * {} = {}".format(sayı1,sayı2,sayı1*sayı2))

elif işlem == "4":
    print("{} / {} = {}".format(sayı1,sayı2,sayı1/sayı2))

else:
    print("Geçersiz İşlem Girdiniz")