import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    try:
        suhu_celsius = float(entry_celsius.get())

        if selected_scale.get() == "Kelvin":
            suhu_kelvin = suhu_celsius + 273.15
            label_kelvin.config(text=f"Kelvin: {suhu_kelvin:.2f} K")
        elif selected_scale.get() == "Fahrenheit":
            suhu_fahrenheit = (suhu_celsius * 9/5) + 32
            label_fahrenheit.config(text=f"Fahrenheit: {suhu_fahrenheit:.2f} °F")
        elif selected_scale.get() == "Reamur":
            suhu_reamur = suhu_celsius * 4/5
            label_reamur.config(text=f"Reamur: {suhu_reamur:.2f} °Re")

    except ValueError:
        label_kelvin.config(text="Masukkan suhu dalam angka!")

# Membuat GUI
app = tk.Tk()
app.title("Konversi Suhu Celsius")
app.geometry("400x350")

# Label dan Entry untuk input Celsius
label_celsius = tk.Label(app, text="Masukkan suhu Celsius:")
label_celsius.pack(pady=10)
entry_celsius = tk.Entry(app)
entry_celsius.pack(pady=10)

# ComboBox untuk memilih skala suhu
label_scale = tk.Label(app, text="Pilih Skala Suhu:")
label_scale.pack(pady=5)
scales = ["Kelvin", "Fahrenheit", "Reamur"]
selected_scale = tk.StringVar()
scale_combobox = ttk.Combobox(app, values=scales, textvariable=selected_scale)
scale_combobox.pack(pady=5)
scale_combobox.set(scales[0])  # Set default value

# Tombol untuk konversi suhu
tombol_konversi = tk.Button(app, text="Konversi", command=konversi_suhu)
tombol_konversi.pack(pady=10)

# Label untuk menampilkan hasil konversi
label_kelvin = tk.Label(app, text="Kelvin: ")
label_kelvin.pack()
label_fahrenheit = tk.Label(app, text="Fahrenheit: ")
label_fahrenheit.pack()
label_reamur = tk.Label(app, text="Reamur: ")
label_reamur.pack()

# Menjalankan aplikasi
app.mainloop()
