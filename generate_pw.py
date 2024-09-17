# Membuat window utama
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Label judul
title_label = tk.Label(root, text="Custom Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Label dan slider untuk memilih panjang password
length_label = tk.Label(root, text="Select password length:")
length_label.pack(pady=5)

password_length_slider = tk.Scale(root, from_=8, to_=128, orient="horizontal", length=300)
password_length_slider.set(12)  # Default panjang password
password_length_slider.pack(pady=5)

# Label untuk password yang dihasilkan
password_label = tk.Label(root, text="Generated password:")
password_label.pack(pady=5)

# Entry box untuk menampilkan password yang dihasilkan
password_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
password_entry.pack(pady=5)

# Tombol untuk menghasilkan password
generate_button = tk.Button(root, text="Generate Password", command=on_generate, font=("Helvetica", 12), bg="lightblue")
generate_button.pack(pady=20)

# Loop utama aplikasi
root.mainloop()
