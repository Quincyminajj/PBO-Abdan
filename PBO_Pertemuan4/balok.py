import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W,font


def hitung_volume():
    panjang = float(txt_panjang.get())
    lebar = float(txt_lebar.get())
    tinggi = float(txt_tinggi.get())
    
    V = round(panjang * lebar * tinggi, 2)
    
    txt_volume.delete(0, END)
    txt_volume.insert(END, V)

def hitung_luas_permukaan():
    panjang = float(txt_panjang.get())
    lebar = float(txt_lebar.get())
    tinggi = float(txt_tinggi.get())
    
    lp = round(2 * (panjang * lebar + panjang * tinggi + lebar * tinggi), 2)
    
    txt_luas_permukaan.delete(0, END)
    txt_luas_permukaan.insert(END, lp)

def hitung():
    hitung_volume()
    hitung_luas_permukaan()

app = tk.Tk()
app.title("Menghitung volume dan luas permukaan Balok")
app.configure(bg="blue")

Frame = Frame(app)
Frame.pack(padx=40, pady=40)

nama = tk.Label(Frame, text='Menghitung Balok: ')
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

panjang = Label(Frame, text='Panjang: ')
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

lebar = Label(Frame, text='Lebar: ')
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

tinggi = Label(Frame, text='Tinggi: ')
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

volume = Label(Frame, text='Volume: ')
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

luas_permukaan = Label(Frame, text='Luas Permukaan: ')
luas_permukaan.grid(row=6, column=0, sticky=W, padx=5, pady=5)

hitung_volume_button = Button(Frame, text="Hitung Volume",background="orange",command=hitung_volume)
hitung_volume_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

hitung_luas_permukaan_button = Button(Frame, text="Hitung Luas Permukaan",background="orange" ,command=hitung_luas_permukaan)
hitung_luas_permukaan_button.grid(row=8, column=1, sticky=W, padx=5, pady=5)

txt_panjang = Entry(Frame)
txt_panjang.grid(row=1, column=1)

txt_lebar = Entry(Frame)
txt_lebar.grid(row=2, column=1)

txt_tinggi = Entry(Frame)
txt_tinggi.grid(row=3, column=1)

txt_volume = Entry(Frame)
txt_volume.grid(row=5, column=1)

txt_luas_permukaan = Entry(Frame)
txt_luas_permukaan.grid(row=6, column=1)


nama = Label(Frame, text=' ')
nama.grid(row=7, column=0, sticky=W, padx=5, pady=5)

custom_font = font.Font(family="ARIAL")
nama = tk.Label(Frame, text='MUHAMMAD ABDAN SYAKURAN',font=custom_font)
nama.grid(row=10, column=1, sticky=W, padx=3, pady=3)


app.mainloop()