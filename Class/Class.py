class Aile:
    def __init__(self, adı, soyadı,yaş,meslek,medeni_hali,çocuk_sayısı):
        self.adı = adı
        self.soyadı = soyadı
        self.yaş = yaş
        self.meslek = meslek
        self.medeni_hali = medeni_hali
        self.çocuk_sayısı = çocuk_sayısı
Anne = Aile("Ayşe","Korkmaz","55","Ev Hanımı","Evli","3")
print(Anne.adı)