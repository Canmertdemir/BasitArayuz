import tkinter as tk
from tkinter import messagebox

def quiz_ortalama_hesaplama():
    try:
        q1 = float(entry_quiz1.get())
        q2 = float(entry_quiz2.get())
        q3 = float(entry_quiz3.get())
        q4 = float(entry_quiz4.get())

        quiz_ortalama = (q1 + q2 + q3 + q4) / 4
        label_sonuc.config(text=f"Quiz Ortalaması: {quiz_ortalama:.2f}")
        return quiz_ortalama
    except ValueError:
        messagebox.showerror("Hata", "Lütfen tüm quiz kutucuklarına geçerli bir sayı girin.")
        return None

def genel_ortalama_hesapla():
    try:
        quiz_ort = quiz_ortalama_hesaplama()
        if quiz_ort is None:
            return

        vize = float(entry_vize.get())
        final = float(entry_final.get())
        genel_ortalama = (quiz_ort * 0.4) + (vize * 0.3) + (final * 0.3)
        label_sonuc_genel_ortalama.config(text=f"Genel Ortalama: {genel_ortalama:.2f}")
        harf_notu_hesapla(genel_ortalama)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen vize ve final kutucuklarına geçerli bir sayı girin.")

def harf_notu_hesapla(genel_ortalama):
    if genel_ortalama >= 90:
        harf = "AA"
    elif genel_ortalama >= 85:
        harf = "BA"
    elif genel_ortalama >= 80:
        harf = "BB"
    elif genel_ortalama >= 75:
        harf = "CB"
    elif genel_ortalama >= 70:
        harf = "CC"
    elif genel_ortalama >= 65:
        harf = "DC"
    elif genel_ortalama >= 60:
        harf = "DD"
    else:
        harf = "FF"
    label_sonuc_harf_notu.config(text=f"Harf Notu: {harf}")

def ders_saati_hesapla():
    try:
        uygulamali_mi = entry_uygulamali_mi.get().strip() == "1"
        haftalik_sayi = int(entry_ders_haftası_sayisi.get())
        teorik = int(entry_teorik_haftalil_ders_saatleri.get())
        uygulama = int(entry_uygulama_haftalil_ders_saatleri.get())
        devamsizlik = int(entry_devamsizlik_suresi.get())

        if uygulamali_mi:
            toplam = uygulama * haftalik_sayi
            devam_zorunlu = toplam * 0.80
        else:
            toplam = teorik * haftalik_sayi
            devam_zorunlu = toplam * 0.70

        if devamsizlik > devam_zorunlu:
            label_sonuc_devamsizlik.config(text="Devamsızlık süresi aşıldı!", fg="red")
        else:
            label_sonuc_devamsizlik.config(text="Devamsızlık süresi aşılmadı.", fg="green")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")

def temizle():
    for entry in [entry_quiz1, entry_quiz2, entry_quiz3, entry_quiz4,
                  entry_ders_haftası_sayisi, entry_teorik_haftalil_ders_saatleri,
                  entry_uygulama_haftalil_ders_saatleri, entry_devamsizlik_suresi,
                  entry_vize, entry_final, entry_uygulamali_mi]:
        entry.delete(0, tk.END)

    label_sonuc.config(text="Quiz Ortalaması:")
    label_sonuc_genel_ortalama.config(text="Genel Ortalama:")
    label_sonuc_devamsizlik.config(text="Devam Durumu:")
    label_sonuc_harf_notu.config(text="Harf Notu:")

pencere = tk.Tk()
pencere.title("Quiz Ortalama Hesaplayıcı")
pencere.geometry("400x650")

row_num = 0

def add_labeled_entry(label_text):
    global row_num
    label = tk.Label(pencere, text=label_text)
    label.grid(row=row_num, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(pencere)
    entry.grid(row=row_num, column=1, padx=5, pady=5)
    row_num += 1
    return entry

entry_quiz1 = add_labeled_entry("Quiz 1:")
entry_quiz2 = add_labeled_entry("Quiz 2:")
entry_quiz3 = add_labeled_entry("Quiz 3:")
entry_quiz4 = add_labeled_entry("Quiz 4:")
entry_vize = add_labeled_entry("Vize:")
entry_final = add_labeled_entry("Final:")
entry_ders_haftası_sayisi = add_labeled_entry("Ders Haftası Sayısı:")
entry_teorik_haftalil_ders_saatleri = add_labeled_entry("Teorik Haftalık Ders Saati:")
entry_uygulama_haftalil_ders_saatleri = add_labeled_entry("Uygulama Haftalık Ders Saati:")
entry_uygulamali_mi = add_labeled_entry("Uygulamalı mı? (1/0):")
entry_devamsizlik_suresi = add_labeled_entry("Devamsızlık Süresi:")

tk.Button(pencere, text="Quiz Ortalaması Hesapla", command=quiz_ortalama_hesaplama).grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

tk.Button(pencere, text="Genel Ortalamayı Hesapla", command=genel_ortalama_hesapla).grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

tk.Button(pencere, text="Devam Durumu Hesapla", command=ders_saati_hesapla).grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

tk.Button(pencere, text="Temizle", command=temizle).grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

label_sonuc = tk.Label(pencere, text="Quiz Ortalaması: -", font=("Arial", 12, "bold"))
label_sonuc.grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

label_sonuc_harf_notu = tk.Label(pencere, text="Harf Notu: -", font=("Arial", 12, "bold"))
label_sonuc_harf_notu.grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

label_sonuc_genel_ortalama = tk.Label(pencere, text="Genel Ortalama: -", font=("Arial", 12, "bold"))
label_sonuc_genel_ortalama.grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

label_sonuc_devamsizlik = tk.Label(pencere, text="Devam Durumu: -", font=("Arial", 12, "bold"))
label_sonuc_devamsizlik.grid(row=row_num, column=0, columnspan=2, pady=10)
row_num += 1

pencere.mainloop()
