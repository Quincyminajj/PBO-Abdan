import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

def extract_text():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)

            # Update hasil ke TextBox
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)
    except Exception as e:
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, f"Error: {str(e)}")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Ekstraksi Teks dari Gambar")

# Membuat tombol untuk memilih file gambar
tombol_browse = ttk.Button(root, text="Pilih Gambar", command=extract_text)
tombol_browse.pack(pady=10)

# Menambahkan elemen Canvas untuk menampilkan gambar
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Membuat textbox untuk menampilkan hasil ekstraksi teks
text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
