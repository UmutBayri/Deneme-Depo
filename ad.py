from tkinter import *

pencere = Tk()
pencere.geometry("200x200")
pencere.title("Ad Gösterici")

def ad_göster():
    ad = kullanıcı_entry.get()
    çıktı_lbl.config(text = f"Senin adın : {ad}")

kullanıcı_entry = Entry(
    pencere
)

dönüştür_btn = Button(
    pencere,
    text = "Adımı Göster",
    command = ad_göster
) 

çıktı_lbl = Label(
    pencere,
    text = ""
)

kullanıcı_entry.pack()
dönüştür_btn.pack()
çıktı_lbl.pack()

pencere.mainloop()