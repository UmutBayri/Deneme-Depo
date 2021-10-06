"""
Metin belgesi yazıp kaydetme, metin belgesi açma ve düzenleme,
tema seçenekleri, yazı seçenekleri
"""
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

import webbrowser

# Pencere


pencere = Tk()
pencere.title("Not Defterim🖋️")
pencere.resizable(False, False)
pencere.geometry("800x500")
# Fonksiyonlar

def iletişim_link_aç() :
    webbrowser.open("https://github.com/UmutBayri")        


def dosya_aç():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    metin.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        metin.insert(END, text)
    pencere.title(f"Simple Text Editor - {filepath}")

def dosya_kaydet():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = metin.get(1.0, END)
        output_file.write(text)
    pencere.title(f"Simple Text Editor - {filepath}")


# Fonk Tema

def tema_değiştir_standart() :
    
    çerçeve1.config(bg = "#f0f0f0")
    çerçeve2.config(bg = "#f0f0f0")
    metin.config(bg = "#FFFFFF", bd = 0, font = ("Arial", 12), 
    insertbackground = "#000000")
    imza.config(bg = "#f0f0f0", fg = "#000000", font = ("Arial"))
    kaydet_btn.config(
        bg = "#f0f0f0",
        fg = "#000000",
        activebackground = "#F5F1F0", 
        font = ("Arial")
        )
    aç_btn.config(
        bg = "#f0f0f0",
        fg = "#000000",
        activebackground = "#F5F1F0",
        font = ("Arial")
        )
def tema_değiştir_koyu() :
        
    çerçeve1.config(bg = "#2C2E31")
    çerçeve2.config(bg = "#2C2E31")
    metin.config(bg = "#232629", fg = "#FFFFFF", bd = 3, font = ("Tİmes", 12), 
    insertbackground = "#FFFFFF")
    imza.config(bg = "#2C2E31", fg = "#FFFFFF", font = ("Times"))
    kaydet_btn.config(
        bg = "#AF689A",
        activebackground = "#A47D98", 
        fg = "#FFFFFF",
        font = ("Times")
        )
    aç_btn.config(
        bg = "#AF689A",
        fg = "#FFFFFF",
        activebackground = "#A47D98",
        font = ("Times")
        )
def tema_değiştir_mrrobot() :
    
    çerçeve1.config(bg = "#4B926F")
    çerçeve2.config(bg = "#4B926F")
    metin.config(bg = "#000000", 
        fg = "#48823F", 
        bd = 0, 
        font = ("Terminal", 12), 
        insertbackground = "#FFFFFF")
    imza.config(bg = "#4B926F", fg = "#000000", font = ("Terminal"))
    kaydet_btn.config(
        bg = "#4B926F",
        fg = "#000000",
        activebackground = "#6FE5AA", 
        font = ("Terminal")
        )
    aç_btn.config(
        bg = "#4B926F",
        fg = "#000000",
        activebackground = "#6FE5AA",
        font = ("Terminal")
        )
def tema_değiştir_prenses() :
    çerçeve1.config(bg = "#EDD3CD")
    çerçeve2.config(bg = "#EDD3CD")
    metin.config(bg = "#EBDFDC", bd = 0, font = ("Candara", 12), 
    insertbackground = "#000000")
    imza.config(bg = "#EDD3CD", font = ("Candara"))
    kaydet_btn.config(
        bg = "#EDD3CD",
        activebackground = "#EDD9CD", 
        font = ("Candara")
        )
    aç_btn.config(
        bg = "#EDD3CD",
        activebackground = "#EDD9CD",
        font = ("Candara")
        ) 

# Çerçeveler

çerçeve1 = Frame(pencere)
çerçeve2 = Frame(pencere)


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
        command = tema_değiştir_standart
)

tema_sçnk.add_command(
        label = "Koyu",
        font = ("Georgia", 9, "bold"),
        command = tema_değiştir_koyu
)

tema_sçnk.add_command(
        label = "Mr. Robot",
        font = ("Terminal", 9),
        command = tema_değiştir_mrrobot
)

tema_sçnk.add_command(
        label = "Prenses",
        font = ("Candara"),
        command = tema_değiştir_prenses
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
        font = (11)
)

# Butonlar

kaydet_btn = Button(
        çerçeve1,
        width = 13,
        text = "Kaydet",
        bd = 1,
        command = dosya_kaydet        
)

aç_btn = Button(
        çerçeve1,
        width = 13,
        text = "Aç",
        bd = 1,
        command = dosya_aç
)

# İmza
imza_mtn = \
"""Dostlar
Yapım✨"""
imza = Label(
        çerçeve1,
        text = imza_mtn,
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
