import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class BankaUygulamasi(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Banka Uygulaması")
        self.bakiye = 500
        self.faturalar = {"su": {"miktar": 100, "odendi": False},
                          "elektrik": {"miktar": 150, "odendi": False},
                          "doğalgaz": {"miktar": 120, "odendi": False},
                          "internet": {"miktar": 80, "odendi": False},
                          "telefon": {"miktar": 50, "odendi": False}}

        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(expand=1, fill="both")

        self.para_gonder_tab = ttk.Frame(self.tabControl)
        self.para_cek_tab = ttk.Frame(self.tabControl)
        self.para_yatir_tab = ttk.Frame(self.tabControl)
        self.fatura_ode_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.para_gonder_tab, text="Para Gönder")
        self.tabControl.add(self.para_cek_tab, text="Para Çek")
        self.tabControl.add(self.para_yatir_tab, text="Para Yatır")
        self.tabControl.add(self.fatura_ode_tab, text="Fatura Öde")

        self.tabControl.pack(expand=1, fill="both")

        self.create_para_gonder_tab()
        self.create_para_cek_tab()
        self.create_para_yatir_tab()
        self.create_fatura_ode_tab()

    def input_al(self, prompt):
        while True:
            deger = simpledialog.askinteger("Giriş", prompt)
            if deger is None:  # Kullanıcı iptal etti
                return None
            if deger >= 0:
                return deger
            else:
                messagebox.showerror("Hata", "Geçersiz miktar")

    def bakiye_guncelle(self):
        self.label_bakiye.config(text="Bakiye: %d₺" % self.bakiye)

    def create_para_gonder_tab(self):
        frame = tk.Frame(self.para_gonder_tab)
        frame.pack(padx=20, pady=20)

        label = tk.Label(frame, text="Para Gönder", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        button = tk.Button(frame, text="Para Gönder", command=self.para_gonder, bg="#4CAF50", fg="white", padx=10, pady=5, font=("Helvetica", 12))
        button.pack()

    def create_para_cek_tab(self):
        frame = tk.Frame(self.para_cek_tab)
        frame.pack(padx=20, pady=20)

        label = tk.Label(frame, text="Para Çek", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        button = tk.Button(frame, text="Para Çek", command=self.para_cek, bg="#FF5733", fg="white", padx=10, pady=5, font=("Helvetica", 12))
        button.pack()

    def create_para_yatir_tab(self):
        frame = tk.Frame(self.para_yatir_tab)
        frame.pack(padx=20, pady=20)

        label = tk.Label(frame, text="Para Yatır", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        button = tk.Button(frame, text="Para Yatır", command=self.para_yatir, bg="#4287f5", fg="white", padx=10, pady=5, font=("Helvetica", 12))
        button.pack()

    def create_fatura_ode_tab(self):
        frame = tk.Frame(self.fatura_ode_tab)
        frame.pack(padx=20, pady=20)

        label = tk.Label(frame, text="Fatura Öde", font=("Helvetica", 16, "bold"))
        label.pack(pady=10)

        for fatura, bilgi in self.faturalar.items():
            label = tk.Label(frame, text=f"{fatura.capitalize()}: {bilgi['miktar']}₺", font=("Helvetica", 12))
            label.pack()

            bilgi["label"] = tk.Label(frame, text="Ödenmedi", font=("Helvetica", 10), fg="red")
            bilgi["label"].pack()

        button = tk.Button(frame, text="Fatura Öde", command=self.fatura_ode, bg="#E67E22", fg="white", padx=10, pady=5, font=("Helvetica", 12))
        button.pack()

    def para_gonder(self):
        miktar = self.input_al("Göndermek istediğiniz miktarı giriniz:")
        if miktar is not None:
            if self.bakiye - miktar >= 0:
                self.bakiye -= miktar
                messagebox.showinfo("Başarılı", "Para gönderildi. Yeni bakiyeniz: %d₺" % self.bakiye)
            else:
                messagebox.showerror("Hata", "Yetersiz bakiye")
            self.bakiye_guncelle()

    def para_cek(self):
        miktar = self.input_al("Çekmek istediğiniz miktarı giriniz:")
        if miktar is not None:
            if self.bakiye - miktar >= 0:
                self.bakiye -= miktar
                messagebox.showinfo("Başarılı", "Para çekildi. Yeni bakiyeniz: %d₺" % self.bakiye)
            else:
                messagebox.showerror("Hata", "Yetersiz bakiye")
            self.bakiye_guncelle()

    def para_yatir(self):
        miktar = self.input_al("Yatırmak istediğiniz miktarı giriniz:")
        if miktar is not None:
            self.bakiye += miktar
            messagebox.showinfo("Başarılı", "Para yatırıldı. Yeni bakiyeniz: %d₺" % self.bakiye)
            self.bakiye_guncelle()

    def fatura_ode(self):
        fatura_secenekleri = list(self.faturalar.keys())
        secilen_fatura = simpledialog.askstring("Fatura Ödeme", "Ödemek istediğiniz faturayı seçin:", initialvalue=fatura_secenekleri[0])
        if secilen_fatura:
            secilen_fatura = secilen_fatura.lower()
            fatura_bilgi = self.faturalar.get(secilen_fatura)
            if not fatura_bilgi["odendi"]:
                miktar = fatura_bilgi["miktar"]
                if self.bakiye - miktar >= 0:
                    self.bakiye -= miktar
                    fatura_bilgi["odendi"] = True
                    fatura_bilgi["label"].config(text="Ödendi", fg="green")
                    messagebox.showinfo("Başarılı", f"{secilen_fatura.capitalize()} faturası ödendi. Yeni bakiyeniz: %d₺" % self.bakiye)
                else:
                    messagebox.showerror("Hata", "Yetersiz bakiye")
            else:
                messagebox.showwarning("Uyarı", f"{secilen_fatura.capitalize()} faturası zaten ödenmiş.")
            self.bakiye_guncelle()

uygulama = BankaUygulamasi()
uygulama.mainloop()