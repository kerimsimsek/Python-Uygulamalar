def buyuk_harflerle_yazdir(inputDosya, outputDosya):
    try:
        with open(inputDosya, 'r', encoding='utf-8') as f:
            cumleler = f.readlines()

        with open(outputDosya, 'w', encoding='utf-8') as f:
            for cumle in cumleler:
                buyuk_cumle = cumle.upper()
                f.write(buyuk_cumle)

        print("İşlem tamamlandı. Büyük harflerle yazılmış cümleler '{}' adlı dosyaya kaydedildi.".format(outputDosya))

    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")

input_dosya = "giris.txt"  # Giriş dosyasının adını değiştirebilirsiniz
output_dosya = "cikti.txt"  # Çıkış dosyasının adını değiştirebilirsiniz

buyuk_harflerle_yazdir(input_dosya, output_dosya)

#PS C:\Users\gfbke\Desktop\Proje> python metin_buyutme.py giris.txt bu şekilde terminale yaz