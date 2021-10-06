"""
Metin belgesi yazıp kaydetme, metin belgesi açma ve düzenleme,
tema seçenekleri, yazı seçenekleri
"""
from tkinter import *
import webbrowser

# Pencere


pencere = Tk()
pencere.title("Not Defterim🖋️")
pencere.resizable(False, False)
pencere.rowconfigure(
        0,
        minsize = 500,
        weight = 1
)

pencere.columnconfigure(
        1,
        minsize = 500,
        weight = 1
)

# Fonksiyonlar

def iletişim_link_aç() :
        webbrowser.open("https://akademi.icerikbulutu.com/blog/hakkimizda-sayfasi-nasil-yazilir/")        

def tema_değiştir_prenses() :
        bg = "#EDD3CD"
        metin_bg = "#EBDFDC"
        pass

# Çerçeveler

çerçeve1 = Frame(pencere,
        bg = "#EDD3CD")
çerçeve2 = Frame(pencere,
        bg = "#EDD3CD")


### Menu
# Menu barı

menubar = Menu(pencere)
pencere.config(menu = menubar)

seçenekler = Menu(tearoff = False)
hakkında = Menu(tearoff = False)

menubar.add_cascade(
        label = "Seçenekler",
        menu = seçenekler
)

menubar.add_cascade(
        label = "Hakkında",
        menu = hakkında
)

hakkında.add_command(
        label = "İletişim",
        command = iletişim_link_aç
)
## Seçenekler listesi
# Tema

tema_sçnk = Menu(seçenekler, tearoff = 0)

tema_sçnk.add_command(
        label = "Standart",
        # command = 
)

tema_sçnk.add_command(
        label = "Koyu"
)

tema_sçnk.add_command(
        label = "Mr. Robot",
        font = ("Terminal", 9)
)

tema_sçnk.add_command(
        label = "Prenses",
        font = ("Candara")
)




# Yazı Seçenekleri
#- Fontlar
yazı_sçnk = Menu(seçenekler, tearoff = 0)

font_sçnk = Menu(yazı_sçnk, tearoff = 0)

yazı_sçnk.add_cascade(
        label = "Font",
        menu = font_sçnk
)

font_sçnk.add_command(
        label = "Standart (Arial)",
        font = ("Arial", 8)
)

font_sçnk.add_command(
        label = "Font2"
)

font_sçnk.add_command(
        label = "Font3"
)

#- Yazı Boyutu

yazı_sçnk.add_command(
        label = "Boyut"
)

# Menu Yerleştirme

seçenekler.add_cascade(
        label = "Metin",
        menu = yazı_sçnk
)

seçenekler.add_cascade(
        label = "Tema",
        menu = tema_sçnk
)
seçenekler.add_separator() # Seçenekler arası çizgi çeker.

seçenekler.add_command(
        label = "Çıkış",
        command = pencere.destroy
)






# Metin

metin = Text(çerçeve2,
        relief = SUNKEN,
        bg = "#EBDFDC",
        font = ("Terminal", 15)
)






# Butonlar

kaydet_btn = Button(
        çerçeve1,
        width = 13,
        bg = "#EDD3CD",
        text = "Kaydet",
        activebackground = "#EDD9CD", 
        bd = 1,
        # command = kaydet        
)

aç_btn = Button(
        çerçeve1,
        width = 13,
        bg = "#EDD3CD",
        activebackground = "#EDD9CD", 
        text = "Aç",
        bd = 1
)

# İmza
imza_mtn = \
"""Dostlar
Yapım✨"""
imza = Label(
        çerçeve1,
        text = imza_mtn,
        bg = "#EDD3CD",
        font = ("Courier", 12)
)
imza.pack(side = BOTTOM
)
# Yerleştirme
 
çerçeve1.pack(side = LEFT,
                fill = Y,
        )
çerçeve2.pack(side = RIGHT,
                fill = BOTH
        )

kaydet_btn.pack(
        padx = 20,
        pady = 15
        )

aç_btn.pack(
        padx = 20
        )


metin.pack(
        fill = BOTH,
        expand = True,
        padx = 5,
        pady = 5  
)

pencere.mainloop()