# https://towardsdatascience.com/how-to-build-an-mp3-music-player-with-python-619e0c0dcee2 

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

import pygame
import webbrowser
import os

# Pencere

pencere = Tk()
pencere.title("Not Defterim🖋️")
pencere.resizable(False, False)
pencere.geometry("800x500+200+200")

## Fonksiyonlar
hakkında_yazısı = \
"""Farklı temalar ve özellikler
barındıran metin editörü.

Özellikler :
- 4 adet tema
- 3 farklı font seçeneği
- Basit arayüz
Yakında :
- Daha fazla tema
- Optimizasyon seçenekleri
- Müzikçalar
"""

def rehber_aç() :
    messagebox.showinfo("Nasıl Kullanılır ?", hakkında_yazısı)
# Fonk Kaydetme Açma
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
    metin.config(bg = "#FFFFFF", fg = "#000000", bd = 0, font = ("Arial", 12), 
    insertbackground = "#000000")
    imza.config(bg = "#f0f0f0", fg = "#000000", font = ("Courier"))
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
    imza.config(bg = "#2C2E31", fg = "#FFFFFF", font = ("Courier"))
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
        insertbackground = "green")
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
    metin.config(bg = "#EBDFDC", fg = "#000000", bd = 0, font = ("Candara", 12), 
    insertbackground = "#000000")
    imza.config(bg = "#EDD3CD", font = ("Courier"))
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
temel_çerçeve1 = Frame(pencere)
temel_çerçeve2 = Frame(pencere)


çerçeve1 = Frame(temel_çerçeve1)
çerçeve2 = Frame(temel_çerçeve2)
çerçeve3 = Frame(temel_çerçeve1)
çerçeve4 = Frame(temel_çerçeve1)


### Müzik
başlat_resim = PhotoImage(file = "başlat.png")
durdur_resim = PhotoImage(file = "durdur.png")
bitir_resim = PhotoImage(file = "bitir.png")

directory = r"C:\Users\Administrator\Desktop\müzikler"
os.chdir(directory)
şarkı_listesi = os.listdir()

oynatma_listesi = Listbox(
        çerçeve4,
        selectmode = SINGLE,
) 

pygame.init()
pygame.mixer.init()

def oynat():
    pygame.mixer.music.load(oynatma_listesi.get(ACTIVE))
    pygame.mixer.music.play(-1)

def bitir():
    pygame.mixer.music.stop()

def durdur():
    pygame.mixer.music.pause()

def devam_et():
    pygame.mixer.music.unpause()




for şarkı in şarkı_listesi :
        sıra = 0
        oynatma_listesi.insert(sıra, şarkı)

başlatma_btn = Button(
        çerçeve3,
        image = başlat_resim,
        command = oynat
)

durdurma_btn = Button(
        çerçeve3,
        image = durdur_resim,
        command = durdur
)

bitirme_btn = Button(
    çerçeve3,
    image = bitir_resim,
    command = bitir
)

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
        label = "Nasıl Kullanılır?",
        command = rehber_aç
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
        bd = 0,
        font = ("Arial", 12), 
        insertbackground = "#000000",
)

# Butonlar

kaydet_btn = Button(
        çerçeve1,
        width = 13,
        text = "Kaydet",
        bd = 1,
        activebackground = "#F5F1F0", 
        font = ("Arial"),
        command = dosya_kaydet        
)

aç_btn = Button(
        çerçeve1,
        width = 13,
        text = "Aç",
        bd = 1,
        activebackground = "#F5F1F0", 
        font = ("Arial"),
        command = dosya_aç
)

# İmza
imza_mtn = "Dostlar\nYapım✨"
imza = Label(
        çerçeve4,
        text = imza_mtn,
        font = ("Courier", 12)
)
### Yerleştirme
## Çerçeveler
temel_çerçeve1.pack(side = LEFT, fill = Y)
temel_çerçeve2.pack(side = RIGHT, fill = BOTH)

çerçeve1.pack()
çerçeve4.pack(side = BOTTOM, fill = X)

çerçeve3.pack(side = BOTTOM)

çerçeve2.pack(fill = BOTH, expand = True)


# Çerçeve1
kaydet_btn.pack(
        padx = 20,
        pady = 15
        )

aç_btn.pack(
        padx = 20
        )

# Çerçeve2
metin.pack(
        fill = BOTH,
        expand = True,
        padx = 5,
        pady = 5  
)

# Çerçeve3
başlatma_btn.grid(row = 0)
durdurma_btn.grid(row = 0, column=1)
bitirme_btn.grid(row = 0, column = 2)
#Çerçeve4

oynatma_listesi.pack(
    padx = 5,
    fill = X,
    expand = True
)

imza.pack(pady = 10)




pencere.mainloop()
