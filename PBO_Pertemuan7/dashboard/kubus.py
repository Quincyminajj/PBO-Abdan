import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END

class kubus:
    def __init__(self, master):
        self.master = master
        master.title("KALKULATOR LUAS DAN VOLUME KUBUS")

        self.frame = Frame(master)
        self.frame.pack(padx=40, pady=40)

        self.nama = Label(self.frame, text="MUHAMMAD ABDAN SYAKURAN")
        self.nama.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.sisi_label = Label(self.frame, text="Sisi:")
        self.sisi_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        self.txt_sisi = Entry(self.frame)
        self.txt_sisi.grid(row=1, column=1)

        self.hitung_button = Button(self.frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        self.luas_label = Label(self.frame, text="Luas :")
        self.luas_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        self.volume_label = Label(self.frame, text="Volume :")
        self.volume_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        self.txt_luas = Entry(self.frame)
        self.txt_luas.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        self.txt_volume = Entry(self.frame)
        self.txt_volume.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    def hitung_luas(self):
        try:
            s = float(self.txt_sisi.get())
            if s <= 0:
                raise ValueError("Sisi must be a positive number.")
            L = round((6 * s**2), 2)
            self.txt_luas.delete(0, END)
            self.txt_luas.insert(END, L)
        except ValueError as e:
            print(f"Error: {e}")

    def hitung_volume(self):
        try:
            s = float(self.txt_sisi.get())
            if s <= 0:
                raise ValueError("Sisi must be a positive number.")
            V = round((s**3), 2)
            self.txt_volume.delete(0, END)
            self.txt_volume.insert(END, V)
        except ValueError as e:
            print(f"Error: {e}")

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

if __name__ == "__main__":
    root = tk.Tk()
    app = kubus(root)
    root.mainloop()
