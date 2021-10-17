from tkinter import Button, OptionMenu, StringVar, TclError, Tk, Label, Text
from tkinter.constants import SUNKEN

from deep_translator import GoogleTranslator

pencere = Tk()
pencere.title("Çeviri")

def çevir() :
    seçili_dil = değer.get().lower()

    try :
        girdi = girdi_ent.get("1.0", "end-1c")
        çıktı = GoogleTranslator(source = "auto", target = seçili_dil).translate(girdi)
        çıktı_lbl.config(text = çıktı)

    except :
        pass

# dil_listesi = GoogleTranslator.get_supported_languages()
dil_listesi = ["English", "Turkish", "French", "Arabic", "Chinese", "German", "Italian"]
dil_listesi.sort()

değer = StringVar()
değer.set("English")

dil_seçenekleri = OptionMenu(
    pencere,
    değer,
    *dil_listesi
)

girdi_ent  = Text(
    pencere,
    font = ("Times", 12),
    bd = 2,
    height = 10,
    width = 34
)

çıktı_lbl = Label(
    pencere,
    bg = "grey",
    font = ("Times", 12),
    relief = SUNKEN,
    width = 30,
    height = 10,
    text = ""
)

dil_seçenekleri.pack()
girdi_ent.pack(padx = 10)
çıktı_lbl.pack(padx = 10, pady = 5)


while True :
    try :
        çevir()
        pencere.update()
    except TclError as tcl :
        print("Döngü sonlandırıldı!")
        break