#Girilen sayıya kadar olan sayılardan çift ve tek olanların toplamını yazdırılması 
tektoplam = 0
cifttoplam = 0
girilen_sayı = int(input("Sayı girin : "))
for i in range(girilen_sayı+1):
    if i % 2 == 1:
        tektoplam += i
    else:
        cifttoplam += i
print(f"Teklerin toplamı : {tektoplam} \n Çiftlerin toplamı : {cifttoplam}")