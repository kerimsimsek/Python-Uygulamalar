#5 ve 121 sayıları arasındaki 2 ve 3 e tam bölünen sayıların bulunması
for i in range(5,122):
    if i % 2 == 0 and i % 3 == 0:
        print(i)