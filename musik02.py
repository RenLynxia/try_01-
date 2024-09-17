import tkinter as tk
from tkinter import filedialog, messagebox
import os
import glob

class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music App")
        self.current_frame = None
        self.is_playing = False  # Status musik apakah sedang diputar atau tidak
        self.music_files = []  # Daftar file musik yang ditemukan
        self.current_directory = ""  # Direktori saat ini

        # Inisiasi halaman utama
        self.show_main_page()

    def show_main_page(self):
        # Menghapus frame saat ini (jika ada)
        if self.current_frame:
            self.current_frame.destroy()

        # Membuat frame baru untuk halaman utama
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Label halaman utama
        label = tk.Label(self.current_frame, text="Welcome to Music App!", font=("Helvetica", 16))
        label.pack(pady=20)

        # Tombol untuk membuka direktori
        open_directory_button = tk.Button(self.current_frame, text="Open Music Directory", command=self.open_directory)
        open_directory_button.pack(pady=10)

        # Tombol menuju halaman player (hanya aktif jika ada musik yang ditemukan)
        if self.music_files:
            button = tk.Button(self.current_frame, text="Go to Player", command=self.show_player_page)
            button.pack(pady=10)

    def open_directory(self):
        # Membuka dialog untuk memilih direktori
        directory = filedialog.askdirectory()
        if directory:
            self.current_directory = directory
            self.search_music_files(directory)

    def search_music_files(self, directory):
        # Mencari file musik dengan ekstensi .mp3 di direktori yang dipilih
        self.music_files = glob.glob(os.path.join(directory, "*.mp3"))

        if self.music_files:
            messagebox.showinfo("Music Found", f"Found {len(self.music_files)} music files.")
            self.show_main_page()
        else:
            messagebox.showwarning("No Music Found", "No music files found in this directory.")

    def show_player_page(self):
        # Menghapus frame saat ini (jika ada)
        if self.current_frame:
            self.current_frame.destroy()

        # Membuat frame baru untuk halaman player
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        # Label halaman player
        label = tk.Label(self.current_frame, text="Music Player", font=("Helvetica", 16))
        label.pack(pady=20)

        # Tombol Back
        back_button = tk.Button(self.current_frame, text="Back", command=self.show_main_page)
        back_button.pack(pady=10)

        # Tombol Play
        play_button = tk.Button(self.current_frame, text="Play", command=self.play_music)
        play_button.pack(pady=5)

        # Tombol Pause
        pause_button = tk.Button(self.current_frame, text="Pause", command=self.pause_music)
        pause_button.pack(pady=5)

        # Menampilkan daftar lagu yang ditemukan
        music_list_label = tk.Label(self.current_frame, text="Music Files Found:")
        music_list_label.pack(pady=10)

        for idx, music_file in enumerate(self.music_files):
            music_label = tk.Label(self.current_frame, text=f"{idx + 1}. {os.path.basename(music_file)}")
            music_label.pack()

    def play_music(self):
        if not self.is_playing:
            print("Playing music...")
            self.is_playing = True
        else:
            print("Music is already playing.")

    def pause_music(self):
        if self.is_playing:
            print("Pausing music...")
            self.is_playing = False
        else:
            print("Music is already paused.")

# Membuat window Tkinter
root = tk.Tk()
app = MusicApp(root)

# Menjalankan aplikasi Tkinter
root.mainloop()
