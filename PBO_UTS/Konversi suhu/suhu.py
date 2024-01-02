import tkinter as tk
from tkinter import Frame,font,ttk

def konversi_suhu():
    try:
        suhu_awal = float(entry_suhu.get())
        satuan_awal = combo_suhu_awal.get()
        satuan_hasil = combo_suhu_hasil.get()

        # Konversi suhu
        if satuan_awal == "Celsius":
            suhu_celsius = suhu_awal
        elif satuan_awal == "Fahrenheit":
            suhu_celsius = (suhu_awal - 32) * 5/9
        elif satuan_awal == "Kelvin":
            suhu_celsius = suhu_awal - 273.15
        elif satuan_awal == "Réaumur":
            suhu_celsius = suhu_awal * 5/4

        # Konversi ke satuan hasil
        if satuan_hasil == "Celsius":
            suhu_hasil = suhu_celsius
        elif satuan_hasil == "Fahrenheit":
            suhu_hasil = (suhu_celsius * 9/5) + 32
        elif satuan_hasil == "Kelvin":
            suhu_hasil = suhu_celsius + 273.15
        elif satuan_hasil == "Réaumur":
            suhu_hasil = suhu_celsius * 4/5

        hasil_text = f"Suhu Hasil: {suhu_hasil:.2f} {satuan_hasil}"
        text_box.delete(1.0, tk.END)  # Menghapus teks sebelumnya
        text_box.insert(tk.END, hasil_text)
    except ValueError:
        text_box.delete(1.0, tk.END)  # Menghapus teks sebelumnya
        text_box.insert(tk.END, "Masukkan suhu dalam angka!")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Konversi Suhu")
root.configure(bg="blue")
root.geometry("500x350")

# Membuat label dan entry untuk input suhu
label_suhu = tk.Label(root, text="Masukkan suhu:",fg="white",background="blue")
label_suhu.grid(row=0, column=0, padx=10, pady=10)

entry_suhu = tk.Entry(root)
entry_suhu.grid(row=0, column=1, padx=10, pady=10)

# Membuat Combobox untuk pilihan satuan awal
label_suhu_awal = tk.Label(root, text="Satuan Awal:",fg="white",background="blue")
label_suhu_awal.grid(row=1, column=0, padx=10, pady=10)

satuan_awal_options = ["Celsius", "Fahrenheit", "Kelvin", "Réaumur"]
combo_suhu_awal = ttk.Combobox(root, values=satuan_awal_options, state="readonly")
combo_suhu_awal.set(satuan_awal_options[0])
combo_suhu_awal.grid(row=1, column=1, padx=10, pady=10)

# Membuat Combobox untuk pilihan satuan hasil
label_suhu_hasil = tk.Label(root, text="Satuan Hasil:",fg="white",background="blue")
label_suhu_hasil.grid(row=2, column=0, padx=10, pady=10)

satuan_hasil_options = ["Celsius", "Fahrenheit", "Kelvin", "Réaumur"]
combo_suhu_hasil = ttk.Combobox(root, values=satuan_hasil_options, state="readonly")
combo_suhu_hasil.set(satuan_hasil_options[0])
combo_suhu_hasil.grid(row=2, column=1, padx=10, pady=10)

# Membuat tombol untuk melakukan konversi
tombol_konversi = tk.Button(root, text="Konversi",fg="white",background="green",command=konversi_suhu)
tombol_konversi.grid(row=3, column=0, columnspan=2, pady=10)

# Menambahkan textbox untuk menampilkan hasil konversi
text_box = tk.Text(root, height=4, width=30)
text_box.grid(row=4, column=0, columnspan=2, pady=10)



# Menjalankan aplikasi Tkinter
root.mainloop()

