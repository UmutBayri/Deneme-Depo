from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename

import pygame
import webbrowser
import os

# Pencere

pencere = Tk()
pencere.title("Not Defterim")
pencere.resizable(False, False)
pencere.geometry("800x500+200+200")
not_defteri = r"C:\Users\Administrator\Desktop\resimler\not defteri.ico"
pencere.iconbitmap(not_defteri)

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
- Optimizasyon seçenekleri(öğrenirsem)
- Seçilen müzik dosyalarını hatırlama

Müzikçaları kullanmak için
müzik dosyalarının olduğu klasörü 
en sağdaki tuşla içe aktarın."""

def rehber_aç() :
    messagebox.showinfo(
    title = "Nasıl Kullanılır ?",
    message = hakkında_yazısı, 
    icon = "question",
)

def iletişim_link_aç() :
    webbrowser.open("https://github.com/UmutBayri")        

# Fonk Kaydetme Açma
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
    çerçeve3.config(bg = "#f0f0f0")
    çerçeve4.config(bg = "#f0f0f0")
    çerçeve5.config(bg = "#f0f0f0")

    metin.config(bg = "#F5F1F0", fg = "#000000", bd = 1, font = ("Arial", 12), insertbackground = "#000000")
    imza.config(bg = "#f0f0f0", fg = "#000000", font = ("Courier"))
    oynatma_listesi.config(bg = "#F5F1F0", fg = "#000000")
    el_btn.config(bg = "#f0f0f0")
    müzik_çalar.config(bg = "#f0f0f0", fg = "#000000", font = ("Arial"))


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
    çerçeve3.config(bg = "#2C2E31")
    çerçeve4.config(bg = "#2C2E31")
    çerçeve5.config(bg = "#2C2E31")

    metin.config(bg = "#232629", fg = "#FFFFFF", bd = 3, font = ("Tİmes", 12), 
    insertbackground = "#FFFFFF")
    imza.config(bg = "#2C2E31", fg = "#FFFFFF", font = ("Courier"))
    oynatma_listesi.config(bg = "#2C2E31", fg = "#FFFFFF")
    el_btn.config(bg = "#2C2E31")
    müzik_çalar.config(bg = "#2C2E31", fg = "#FFFFFF", font = ("Courier"))

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
    çerçeve3.config(bg = "#4B926F")
    çerçeve4.config(bg = "#4B926F")
    çerçeve5.config(bg = "#4B926F")

    metin.config(bg = "#000000", 
        fg = "#48823F", 
        bd = 0, 
        font = ("Terminal", 12), 
        insertbackground = "green")
    imza.config(bg = "#4B926F", fg = "#000000", font = ("Terminal", 12))
    oynatma_listesi.config(bg = "#4B926F", fg = "#000000")
    el_btn.config(bg = "#4B926F")
    müzik_çalar.config(bg = "#4B926F", fg = "#000000", font = ("Terminal", 10))


    kaydet_btn.config(
        bg = "#4B926F",
        fg = "#000000",
        activebackground = "#6FE5AA", 
        font = ("Terminal", 11)
        )
    aç_btn.config(
        bg = "#4B926F",
        fg = "#000000",
        activebackground = "#6FE5AA",
        font = ("Terminal", 11)
        )
def tema_değiştir_prenses() :
    çerçeve1.config(bg = "#EDD3CD")
    çerçeve2.config(bg = "#EDD3CD")
    çerçeve3.config(bg = "#EDD3CD")
    çerçeve4.config(bg = "#EDD3CD")
    çerçeve5.config(bg = "#EDD3CD")

    metin.config(bg = "#EBDFDC", fg = "#000000", bd = 0, font = ("Candara", 12), 
    insertbackground = "#000000")
    imza.config(bg = "#EDD3CD", fg = "#000000", font = ("Courier"))
    oynatma_listesi.config(bg = "#EDD3CD", fg = "#000000")
    el_btn.config(bg = "#EDD3CD")
    müzik_çalar.config(bg = "#EDD3CD", fg = "#000000", font = ("Candara"))

    kaydet_btn.config(
        bg = "#EDD3CD",
        fg = "#000000",
        activebackground = "#EDD9CD", 
        font = ("Candara")
        )
    aç_btn.config(
        bg = "#EDD3CD",
        fg = "#000000",
        activebackground = "#EDD9CD",
        font = ("Candara")
        ) 

# Çerçeveler
temel_çerçeve1 = Frame(pencere)
temel_çerçeve2 = Frame(pencere)


çerçeve1 = Frame(temel_çerçeve1)
çerçeve2 = Frame(temel_çerçeve2)
çerçeve3 = Frame(temel_çerçeve1, relief = GROOVE, bd = 2)
çerçeve4 = Frame(temel_çerçeve1, relief = GROOVE, bd = 4)
çerçeve5 = Frame(temel_çerçeve1)

### Müzik
başlat_resim = PhotoImage(file = r"C:\Users\Administrator\Desktop\resimler\başlat.png")
bd_resim = PhotoImage(file = r"C:\Users\Administrator\Desktop\resimler\bd.png")
bitir_resim = PhotoImage(file = r"C:\Users\Administrator\Desktop\resimler\bitir.png")
içe_aktar_resim = PhotoImage(file = r"C:\Users\Administrator\Desktop\resimler\içe aktar.png")

müzik_çalar = Label(
        çerçeve4,
        bg = "#f0f0f0", fg = "#000000", font = ("Arial"),
        text = "Müzikçalar"
)

oynatma_listesi = Listbox(
        çerçeve4,
        bg = "#F5F1F0",
        height = 12,
        selectmode = SINGLE,
) 

pygame.init()
pygame.mixer.init()

def içe_aktar():
    directory = askdirectory()
    os.chdir(directory)
    şarkı_listesi = os.listdir()
    for şarkı in şarkı_listesi :
        if şarkı[-4:] == ".mp3" :
            sıra = 0
            oynatma_listesi.insert(sıra, şarkı)
        else:
            pass

def oynat():
    pygame.mixer.music.load(oynatma_listesi.get(ACTIVE))
    pygame.mixer.music.play(-1)

def bitir():
    pygame.mixer.music.stop()

def durdur():
    pygame.mixer.music.pause()
    durdurma_btn.config(command = devam_et)

def devam_et():
    pygame.mixer.music.unpause()
    durdurma_btn.config(command = durdur)





başlatma_btn = Button(
        çerçeve3,
        image = başlat_resim,
        command = oynat
)

durdurma_btn = Button(
        çerçeve3,
        image = bd_resim,
        command = durdur
)

bitirme_btn = Button(
    çerçeve3,
    image = bitir_resim,
    command = bitir
)

içe_aktar_btn = Button(
    çerçeve3,
    image = içe_aktar_resim,
    command = içe_aktar
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

def font_değiş_standart() :
    metin.config(font = ("Arial"))

def font_değiş_times() :
    metin.config(font = ("Times"))

def font_değiş_verdana() :
    metin.config(font = ("Verdana"))


yazı_sçnk = Menu(seçenekler, tearoff = 0)

font_sçnk = Menu(yazı_sçnk, tearoff = 0)

yazı_sçnk.add_cascade(
        label = "Font",
        menu = font_sçnk
)

font_sçnk.add_command(
        label = "Standart (Arial)",
        font = ("Arial", 8),
        command = font_değiş_standart
)

font_sçnk.add_command(
        label = "Times",
        command = font_değiş_times
)

font_sçnk.add_command(
        label = "Verdana",
        command = font_değiş_verdana
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
        relief = GROOVE,
        bd = 1,
        bg = "#F5F1F0",
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
        çerçeve5,
        text = imza_mtn,
        font = ("Courier", 12)
)


def gizli_kapı_sol():
    temel_çerçeve1.pack(side = RIGHT, fill = BOTH)
    temel_çerçeve2.pack(side = LEFT, fill = Y)
    el_btn.config(command = gizli_kapı_sağ)

def gizli_kapı_sağ():
    temel_çerçeve1.pack(side = LEFT, fill = Y)
    temel_çerçeve2.pack(side = RIGHT, fill = BOTH)
    el_btn.config(command = gizli_kapı_sol)

el_resim1 = PhotoImage(file = r"C:\Users\Administrator\Desktop\resimler\magic.png")
el_resim = el_resim1.subsample(1 ,1)

el_btn = Button(
        çerçeve5,
        bd = 0,
        image = el_resim,
        command = gizli_kapı_sol
)


### Yerleştirme
## Çerçeveler
temel_çerçeve1.pack(side = LEFT, fill = Y)
temel_çerçeve2.pack(side = RIGHT, fill = BOTH)

çerçeve1.pack(fill = BOTH, expand = True)
çerçeve5.pack(side = BOTTOM, fill = X)
çerçeve3.pack(side = BOTTOM, fill = X)
çerçeve4.pack(side = BOTTOM, fill = X)

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
başlatma_btn.grid(row = 0, column = 0)
durdurma_btn.grid(row = 0, column = 1)
bitirme_btn.grid(row = 0, column = 2)
içe_aktar_btn.grid(row = 0, column = 3, ipadx = 5)

#Çerçeve4
müzik_çalar.pack(side = TOP)
oynatma_listesi.pack(
    fill = X,
    expand = True
)

# Çerçeve5
imza.pack(side = LEFT, pady = 10)
el_btn.pack(side = RIGHT)



pencere.mainloop()
