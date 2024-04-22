import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
import sqlite3

class IzlemeTakipUygulamasi(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Film İzleme Takip Uygulaması")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

        self.connection = sqlite3.connect("filmler.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS filmler (id INTEGER PRIMARY KEY, ad TEXT, tür TEXT, izlendi INTEGER)")
        self.connection.commit()

        self.load_filmler()

    def init_ui(self):
        layout = QVBoxLayout()

        self.film_ad_label = QLabel("Film Adı:")
        self.film_ad_input = QLineEdit()
        layout.addWidget(self.film_ad_label)
        layout.addWidget(self.film_ad_input)

        self.film_tür_label = QLabel("Film Türü:")
        self.film_tür_input = QLineEdit()
        layout.addWidget(self.film_tür_label)
        layout.addWidget(self.film_tür_input)

        self.film_ekle_button = QPushButton("Film Ekle")
        self.film_ekle_button.clicked.connect(self.film_ekle)
        layout.addWidget(self.film_ekle_button)

        self.filmler_listwidget = QListWidget()
        layout.addWidget(self.filmler_listwidget)

        self.film_izle_button = QPushButton("İzle")
        self.film_izle_button.clicked.connect(self.film_izle)
        layout.addWidget(self.film_izle_button)

        self.film_sil_button = QPushButton("Sil")
        self.film_sil_button.clicked.connect(self.film_sil)
        layout.addWidget(self.film_sil_button)

        self.setLayout(layout)

    def film_ekle(self):
        film_ad = self.film_ad_input.text().strip()
        film_tür = self.film_tür_input.text().strip()
        if not film_ad or not film_tür:
            QMessageBox.warning(self, "Uyarı", "Film adı ve film türü boş olamaz.")
            return        

        self.cursor.execute("INSERT INTO filmler (ad, tür, izlendi) VALUES (?, ?, 0)", (film_ad, film_tür))
        self.connection.commit()
        self.load_filmler()
        self.film_ad_input.clear()
        self.film_tür_input.clear()

    def film_izle(self):
        secili_film = self.filmler_listwidget.currentItem()
        if secili_film:
            film_ad = secili_film.text().split(" - ")[0]
            self.cursor.execute("UPDATE filmler SET izlendi = 1 WHERE ad = ?", (film_ad,))
            self.connection.commit()
            self.load_filmler()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir film seçin.")

    def film_sil(self):
        secili_film = self.filmler_listwidget.currentItem()
        if secili_film:
            film_ad = secili_film.text().split(" - ")[0]
            self.cursor.execute("DELETE FROM filmler WHERE ad = ?", (film_ad,))
            self.connection.commit()
            self.load_filmler()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir film seçin.")

    def load_filmler(self):
        self.filmler_listwidget.clear()
        self.cursor.execute("SELECT ad, tür, izlendi FROM filmler")
        filmler = self.cursor.fetchall()
        for film in filmler:
            izlendi_durumu = "İzlendi" if film[2] == 1 else "İzlenmedi"
            self.filmler_listwidget.addItem(f"{film[0]} - Tür: {film[1]} - Durum: {izlendi_durumu}")

app = QApplication(sys.argv)
uygulama = IzlemeTakipUygulamasi()
uygulama.show()
sys.exit(app.exec_())
