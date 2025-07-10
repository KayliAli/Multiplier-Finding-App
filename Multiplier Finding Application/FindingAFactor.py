import math
import tkinter as tk
from tkinter import messagebox

pencere = tk.Tk()
pencere.title("ÇARPAN BULMA UYGULAMASI")
pencere.geometry("500x500+500+150")
pencere.resizable(width=False, height=False)

# Temizle fonksiyonu
def temizle():
    sayi1.delete(0, tk.END)
    ekran.config(state=tk.NORMAL)
    ekran.delete('1.0', tk.END)
    ekran.config(state=tk.DISABLED)
    hesapla_button.config(state=tk.DISABLED)  # Temizleme işlemi sonrası buton pasif olur
    temizle_button.config(state=tk.DISABLED)  # Temizle butonunu pasif et

# Hesapla fonksiyonu
def Hesapla():
    try:
        # Sayıyı al
        s1 = int(sayi1.get())
        
        negatif = s1 < 0
        
        # Pozitif sayı kontrolü
        if s1 == 0:
            messagebox.showerror("Geçersiz Giriş", "Lütfen Sıfır Dışında Bir Sayı Giriniz.")
            return

        ekran.config(state=tk.NORMAL)
        ekran.delete('1.0', tk.END)  # Önceki çıktıları temizle
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
        ekran.insert(tk.END, "Girilen Sayı: ", "turuncu")  # Başlık turuncu renkte
        ekran.insert(tk.END, f"{s1}\n", "siyah")  # Sayı koyu siyah renkte
        
        ekran.insert(tk.END, "Çarpanlar: ", "turuncu")  # Başlık turuncu renkte
        ekran.insert(tk.END, f"{', '.join(map(str, carpanlar))}\n", "siyah")  # Çarpanlar koyu siyah renkte
        
        # Negatif sayılar için özel mesaj ekle
        if negatif:
            ekran.insert(tk.END, "Negatif Çarpanlar: ", "mavi")  # "Negatif Çarpanlar:" mavi renkte
            ekran.insert(tk.END, f"{', '.join(map(str, carpanlar_negatif))}\n", "siyah")  # Negatif çarpanlar koyu siyah renkte
        
        ekran.config(state=tk.DISABLED)
    
    except ValueError:
        messagebox.showerror("Geçersiz Giriş", "Lütfen Geçerli Bir sayı Giriniz!")
        
# Kullanıcı Girişi: Sayı girildiğinde Hesapla butonunu aktif et
def sayi_girildi(event=None):
    if sayi1.get().strip() != "":  # Eğer giriş yapılmışsa
        hesapla_button.config(state=tk.NORMAL)  # Hesapla butonunu aktif et
        temizle_button.config(state=tk.NORMAL)  # Temizle butonunu aktif et
    else:  # Eğer giriş yapılmamışsa
        hesapla_button.config(state=tk.DISABLED)  # Hesapla butonunu pasif et
        temizle_button.config(state=tk.DISABLED)  # Temizle butonunu pasif et


# Arka planı değiştirme
pencere.configure(bg="lightblue")

# Etiketler ve diğer bileşenler
etiket1 = tk.Label(pencere, text="HOŞGELDİNİZ", fg="black", font=("Arial", 12))
etiket1.place(x=185,y=3)

etiket2 = tk.Label(pencere, text="Sayı Giriniz:", fg="black", bg="#CCFFFF",font=("Arial",10 ))
etiket2.place(x=50, y=57)

etiket3 = tk.Label(pencere, text="Sayının Çarpanları :", fg="black", bg="orange")
etiket3.place(x=150, y=127)

etiket4 = tk.Label(pencere, text="Lütfen Çarpanlarını Bulmak İstediğiniz Sayıyı Giriniz;", fg="red", bg="#f8f8ff")
etiket4.place(x=50, y=30)

# Kullanıcı Girişi
sayi1 = tk.Entry(pencere, font=14, width=10)
sayi1.place(x=130, y=55)
sayi1.bind("<KeyRelease>", sayi_girildi)  # Kullanıcı her tuşa bastığında kontrol et

# Çıktı Ekranı
ekran = tk.Text(pencere, height=14, width=28, bg="#f0f8ff", fg="black")
ekran.place(x=140, y=150)
ekran.config(state=tk.DISABLED)

# Metin rengi için tag oluştur
ekran.tag_config("turuncu", foreground="orange", font=("Arial", 12))
ekran.tag_config("mavi", foreground="blue")
ekran.tag_config("siyah", foreground="black", font=("Arial", 12, "bold"))

# Butonlar
temizle_button = tk.Button(pencere, text="Temizle", bg="orange", command=temizle, state=tk.DISABLED)
temizle_button.place(x=305, y=55)

hesapla_button = tk.Button(pencere, text="Hesapla", fg="black", bg="#32cd32", command=Hesapla, state=tk.DISABLED)
hesapla_button.place(x=250, y=55)

cikis_button = tk.Button(pencere, text="Çıkış", fg="black", bg="#FF3333", activebackground="red", bd=4, pady=2, padx=7, command=pencere.quit)
cikis_button.place(x=446, y=450)

pencere.mainloop()

