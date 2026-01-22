import math
import tkinter as tk
from tkinter import messagebox
import os,sys

class Application:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.title("ÇARPAN BULMA UYGULAMASI")
        self.pencere.geometry("500x500+500+150")
        self.pencere.resizable(width=False, height=False)

        if getattr(sys, 'frozen', False):
            BASE_DIR = sys._MEIPASS
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        self.pencere.iconbitmap(os.path.join(BASE_DIR, "Files", "logo.ico"))

        # Arka planı değiştirme
        self.pencere.configure(bg="lightblue")

        # Etiketler ve diğer bileşenler
        self.etiket1 = tk.Label(self.pencere, text="HOŞGELDİNİZ", fg="black", font=("Arial", 12))
        self.etiket1.place(x=185,y=3)

        self.etiket2 = tk.Label(self.pencere, text="Sayı Giriniz:", fg="black", bg="#CCFFFF",font=("Arial",10 ))
        self.etiket2.place(x=50, y=57)

        self.etiket3 = tk.Label(self.pencere, text="Sayının Çarpanları :", fg="black", bg="orange")
        self.etiket3.place(x=150, y=127)

        self.etiket4 = tk.Label(self.pencere, text="Lütfen Çarpanlarını Bulmak İstediğiniz Sayıyı Giriniz;", fg="red", bg="#f8f8ff")
        self.etiket4.place(x=50, y=30)

        # Kullanıcı Girişi
        self.sayi1 = tk.Entry(self.pencere, font=14, width=10)
        self.sayi1.place(x=130, y=55)
        self.sayi1.bind("<KeyRelease>", self.sayi_girildi)  # Kullanıcı her tuşa bastığında kontrol et

        # Çıktı Ekranı
        self.ekran = tk.Text(self.pencere, height=14, width=28, bg="#f0f8ff", fg="black")
        self.ekran.place(x=140, y=150)
        self.ekran.config(state=tk.DISABLED)

        # Metin rengi için tag oluştur
        self.ekran.tag_config("turuncu", foreground="orange", font=("Arial", 12))
        self.ekran.tag_config("mavi", foreground="blue")
        self.ekran.tag_config("siyah", foreground="black", font=("Arial", 12, "bold"))

        # Butonlar
        self.temizle_button = tk.Button(self.pencere, text="Temizle", bg="orange",
                                        command=self.temizle, state=tk.DISABLED,cursor="hand2")
        self.temizle_button.place(x=305, y=55)

        self.hesapla_button = tk.Button(self.pencere, text="Hesapla", fg="black", bg="#32cd32",
                                        command=self.Hesapla, state=tk.DISABLED,cursor="hand2")
        self.hesapla_button.place(x=250, y=55)

        self.cikis_button = tk.Button(self.pencere, text="Çıkış", fg="black", bg="#FF3333",
                                      activebackground="red", bd=4, pady=2, padx=7,
                                      command=self.pencere.quit,cursor="hand2")
        self.cikis_button.place(x=446, y=450)

        self.pencere.mainloop()

    # Temizle fonksiyonu
    def temizle(self):
        self.sayi1.delete(0, tk.END)
        self.ekran.config(state=tk.NORMAL)
        self.ekran.delete('1.0', tk.END)
        self.ekran.config(state=tk.DISABLED)
        self.hesapla_button.config(state=tk.DISABLED)  # Temizleme işlemi sonrası buton pasif olur
        self.temizle_button.config(state=tk.DISABLED)  # Temizle butonunu pasif et

    # Hesapla fonksiyonu
    def Hesapla(self):
        try:
            # Sayıyı al
            s1 = int(self.sayi1.get())

            negatif = s1 < 0

            # Pozitif sayı kontrolü
            if s1 == 0:
                messagebox.showerror("Geçersiz Giriş", "Lütfen Sıfır Dışında Bir Sayı Giriniz.")
                return

            self.ekran.config(state=tk.NORMAL)
            self.ekran.delete('1.0', tk.END)  # Önceki çıktıları temizle
            carpanlar = []

            # Pozitif sayılar için çarpanları hesapla
            for i in range(1, int(math.sqrt(abs(s1))) + 1):
                if abs(s1) % i == 0:
                    carpanlar.append(i)
                    if i != abs(s1) // i:
                        carpanlar.append(abs(s1) // i)

            # Negatif sayılar için çarpanları hesapla
            if negatif:
                carpanlar_negatif = [-x for x in carpanlar]
                carpanlar = sorted(carpanlar + carpanlar_negatif)

            # Sonuçları ekrana yazdır
            self.ekran.insert(tk.END, "Girilen Sayı: ", "turuncu")  # Başlık turuncu renkte
            self.ekran.insert(tk.END, f"{s1}\n", "siyah")  # Sayı koyu siyah renkte

            self.ekran.insert(tk.END, "Çarpanlar: ", "turuncu")  # Başlık turuncu renkte
            self.ekran.insert(tk.END, f"{', '.join(map(str, carpanlar))}\n", "siyah")  # Çarpanlar koyu siyah renkte

            # Negatif sayılar için özel mesaj ekle
            if negatif:
                self.ekran.insert(tk.END, "Negatif Çarpanlar: ", "mavi")  # "Negatif Çarpanlar:" mavi renkte
                self.ekran.insert(tk.END, f"{', '.join(map(str, carpanlar_negatif))}\n", "siyah")  # Negatif çarpanlar koyu siyah renkte

            self.ekran.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Geçersiz Giriş", "Lütfen Geçerli Bir sayı Giriniz!")

    # Kullanıcı Girişi: Sayı girildiğinde Hesapla butonunu aktif et
    def sayi_girildi(self, event=None):
        if self.sayi1.get().strip() != "":  # Eğer giriş yapılmışsa
            self.hesapla_button.config(state=tk.NORMAL)  # Hesapla butonunu aktif et
            self.temizle_button.config(state=tk.NORMAL)  # Temizle butonunu aktif et
        else:  # Eğer giriş yapılmamışsa
            self.hesapla_button.config(state=tk.DISABLED)  # Hesapla butonunu pasif et
            self.temizle_button.config(state=tk.DISABLED)  # Temizle butonunu pasif et
