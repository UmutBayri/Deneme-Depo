import base64
from tkinter import Tk, Text, Frame, Entry, Button, Label, mainloop, X, Y, END

pencere = Tk()
pencere.title("Şifreleyici")

çerçeve1 = Frame(pencere)
çerçeve2 = Frame(pencere)

def şifrele():
    try :
        sifre_veri = girdi.get()
        sifre_veri_byte = sifre_veri.encode("UTF-8")
        sifre64 = base64.b64encode(sifre_veri_byte)
        çıktı.insert(1.0, sifre64)
    except :
        pass

def deşifre():
    try :
        deşifre_veri = girdi.get()
        deşifre_veri_byte = deşifre_veri.encode("UTF-8")
        deşifre64 = base64.b64decode(deşifre_veri_byte)
        çıktı.insert(1.0, deşifre64)
    except :
        pass

def temizle():
    girdi.delete(0, END)
    çıktı.delete(1.0, END)

girdi = Entry(
    çerçeve1,
    font = ("Times", 12),
    width = 60
)

çıktı = Text(
    çerçeve2,
    font = ("Times", 12)
)

girdi_lbl = Label(
    çerçeve1,
    text = "Girdi :",
    font = ("Times", 14)
)

şifrele_btn = Button(
    çerçeve1,
    text = "ŞİFRELE",
    width = 15,
    font = ("Times", 10),
    command = şifrele
)

deşifre_btn = Button(
    çerçeve1,
    text = "DEŞİFRE ET",
    width = 15,
    font = ("Times", 10),
    command = deşifre
)

temizle_btn = Button(
    çerçeve1,
    width = 15,
    text = "TEMİZLE",
    font = ("Times", 10),
    command = temizle
)

çerçeve1.pack(fill = X)
çerçeve2.pack()

girdi_lbl.grid(
    row = 0, column = 0, rowspan = 3, 
    sticky = "w", padx = 10, pady = 10
)

girdi.grid(
    row = 0, column = 1, rowspan = 3, 
    sticky = "w"
)

çıktı.grid(
    row = 1, columnspan = 2, padx = 20,
    pady = 20, sticky = "nsew"
)

şifrele_btn.grid(
    row = 0, column = 2, sticky = "e", 
    padx = 10, pady = 2
)

deşifre_btn.grid(
    row = 1, column = 2, sticky = "en", 
    padx = 10, pady = 2
)

temizle_btn.grid(
    row = 2, column = 2, sticky = "e", 
    padx = 10, pady = 2
)

mainloop()
