import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

class bola:
    def __init__(self, master):
        self.master = master
        master.title("KALKULATOR LUAS DAN VOLUME BOLA")

        self.frame = Frame(master)
        self.frame.pack(padx=40, pady=40)

        self.nama = Label(self.frame, text="MUHAMMAD ABDAN SYAKURAN")
        self.nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.jari_jari_label = Label(self.frame, text="jari jari:")
        self.jari_jari_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.txt_jari_jari = Entry(self.frame)
        self.txt_jari_jari.grid(row=1, column=1)

        self.hitung_button = Button(self.frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        self.luas_label = Label(self.frame, text="Luas :")
        self.luas_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.volume_label = Label(self.frame, text="Volume :")
        self.volume_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txt_luas = Entry(self.frame)
        self.txt_luas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        self.txt_volume = Entry(self.frame)
        self.txt_volume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        try:
            r = float(self.txt_jari_jari.get())
            if r <= 0:
                raise ValueError("Radius must be a positive number.")
            L = round((4 * pi * r**2), 2)
            self.txt_luas.delete(0, END)
            self.txt_luas.insert(END, L)
        except ValueError as e:
            print(f"Error: {e}")

    def hitung_volume(self):
        try:
            r = float(self.txt_jari_jari.get())
            if r <= 0:
                raise ValueError("Radius must be a positive number.")
            V = round((4/3 * pi * r**3), 2)
            self.txt_volume.delete(0, END)
            self.txt_volume.insert(END, V)
        except ValueError as e:
            print(f"Error: {e}")

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

if __name__ == "__main__":
    root = tk.Tk()
    app = bola(root)
    root.mainloop()