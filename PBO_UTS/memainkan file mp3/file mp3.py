import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame

def play_music():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            status_label.config(text=f"Now playing: {file_path}")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Music stopped")

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Pemutar MP3")
root.geometry("500x200")

# Membuat tombol untuk memilih file MP3
tombol_browse = ttk.Button(root, text="Pilih playlist kesukaan mu",command=play_music)
tombol_browse.pack(pady=10)

# Membuat tombol untuk menghentikan pemutaran
tombol_stop = ttk.Button(root, text="Stop",command=stop_music)
tombol_stop.pack(pady=10)

# Label untuk menampilkan status
status_label = ttk.Label(root, text="")
status_label.pack(pady=10)


# Menjalankan aplikasi Tkinter
root.mainloop()


