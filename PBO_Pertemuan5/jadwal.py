import tkinter as tk
from tkinter import font,messagebox
import subprocess

def simpan_jadwal():
    nama_file = str(entry_nama_file.get())
    if not nama_file.endswith('.txt'):
        nama_file += '.txt'
    try:
        with open(nama_file, "a") as file:
            data_jadwal = f"{entry_hari.get()} - {entry_mata_kuliah.get()} - {entry_Dosen.get()} - {entry_SKS.get()} - {entry_waktu.get()}\n"
            file.write(data_jadwal)
        messagebox.showinfo("Sukses", "Jadwal berhasil Tersimpan!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

import subprocess

def tampilkan_jadwal():
    nama_file = str(entry_nama_file.get())
    if not nama_file.endswith('.txt'):
        nama_file += '.txt'
    try:
        subprocess.Popen([nama_file], shell=True)
    except FileNotFoundError:
        messagebox.showinfo("Info", "File jadwal tidak ditemukan.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")


# Membuat GUI
app = tk.Tk()
app.title("Jadwal Kuliah")
app.geometry("450x430")
app.configure(bg="#D0011B")

#nama
custom_font = font.Font(family="Piston Pressure")
label_nama = tk.Label(app, text="Muhammad Abdan Syakuran",fg="yellow",bg="#D0011B",font=custom_font)
label_nama.grid(row=10, column=0, padx=10, pady=10, sticky='e')
custom_font = font.Font(family="Berlin Sans FB Demi")
label_nama = tk.Label(app, text="Jadwal Perkuliahan Semester 3",fg="yellow",bg="#D0011B",font=custom_font)
label_nama.grid(row=1, column=0, padx=10, pady=10, sticky='e')

# Label dan Entry untuk data
custom_font = font.Font(family="Berlin Sans FB Demi")
label_hari = tk.Label(app, text="Hari:",fg="white",bg="#D0011B",font=custom_font)
label_hari.grid(row=3, column=0, padx=10, pady=10)
entry_hari = tk.Entry(app)
entry_hari.grid(row=4, column=0, padx=10, pady=10)

custom_font = font.Font(family="Berlin Sans FB Demi")
label_mata_kuliah = tk.Label(app, text="Mata Kuliah:",fg="white",bg="#D0011B",font=custom_font)
label_mata_kuliah.grid(row=3, column=1, padx=10, pady=10)
entry_mata_kuliah = tk.Entry(app)
entry_mata_kuliah.grid(row=4, column=1, padx=10, pady=10)

custom_font = font.Font(family="Berlin Sans FB Demi")
label_Dosen = tk.Label(app, text="Dosen Pengampu:",fg="white",bg="#D0011B",font=custom_font)
label_Dosen.grid(row=5, column=0, padx=10, pady=10)
entry_Dosen = tk.Entry(app)
entry_Dosen.grid(row=6, column=0, padx=10, pady=10)

custom_font = font.Font(family="Berlin Sans FB Demi")
label_SKS = tk.Label(app, text="Jumlah SKS:",fg="white",bg="#D0011B",font=custom_font)
label_SKS.grid(row=5, column=1, padx=10, pady=10)
entry_SKS = tk.Entry(app)
entry_SKS.grid(row=6, column=1, padx=10, pady=10)

custom_font = font.Font(family="Berlin Sans FB Demi")
label_waktu = tk.Label(app, text="Waktu:",fg="white",bg="#D0011B",font=custom_font)
label_waktu.grid(row=7, column=0, padx=10, pady=10)
entry_waktu = tk.Entry(app)
entry_waktu.grid(row=8, column=0, padx=10, pady=10)

custom_font = font.Font(family="Berlin Sans FB Demi")
label_file = tk.Label(app, text="Masukan Nama File",fg="white",bg="#D0011B",font=custom_font)
label_file.grid(row=7, column=1, padx=10, pady=10)
entry_nama_file = tk.Entry(app)
entry_nama_file.grid(row=8, column=1, padx=10, pady=10)

# Tombol Simpan Jadwal
button_simpan = tk.Button(app, text="Simpan Jadwal",fg="white",background="#03045e",command=simpan_jadwal)
button_simpan.grid(row=9, column=0, pady=10)

# Tombol Tampilkan Jadwal
button_tampilkan = tk.Button(app, text="Tampilkan Jadwal",fg="white",background="#03045e",command=tampilkan_jadwal)
button_tampilkan.grid(row=9, column=1, pady=10)

# Menjalankan aplikasi
app.mainloop()