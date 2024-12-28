import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Style
import qrcode
from PIL import Image, ImageTk

# Function to generate and display QR code
def generate_qr():
    data = entry.get()
    if not data.strip():
        messagebox.showwarning("Input Error", "Please enter some text or URL.")
        return

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Convert to an image compatible with Tkinter
    qr_image_tk = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk
    qr_label.place(relx=0.5, rely=0.6, anchor="center")

# Function to save QR code
def save_qr():
    data = entry.get()
    if not data.strip():
        messagebox.showwarning("Save Error", "Generate a QR code before saving.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if save_path:
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(save_path)
        messagebox.showinfo("Save Success", f"QR Code saved to {save_path}")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x600")
root.configure(bg="#F9FAFB")

# Style configuration
style = Style()
style.configure("TButton", font=("Segoe UI", 12), padding=5)
style.configure("TLabel", font=("Segoe UI", 12), background="#F9FAFB", foreground="#333333")

# Header Section
header = tk.Label(root, text="QR Code Generator", font=("Segoe UI", 20, "bold"), bg="#F9FAFB", fg="#333333")
header.pack(pady=20)

# Input Field
input_frame = tk.Frame(root, bg="#F9FAFB")
input_frame.pack(pady=10, padx=20, fill="x")

entry_label = tk.Label(input_frame, text="Enter Text or URL:", font=("Segoe UI", 12), bg="#F9FAFB", fg="#555555")
entry_label.pack(anchor="w")

entry = tk.Entry(input_frame, font=("Segoe UI", 12), relief="flat", bd=1, highlightthickness=1, highlightbackground="#D1D5DB")
entry.pack(fill="x", pady=10)

# Button Section
button_frame = tk.Frame(root, bg="#F9FAFB")
button_frame.pack(pady=20)

generate_button = tk.Button(button_frame, text="Generate QR", font=("Segoe UI", 12), bg="#4CAF50", fg="#FFFFFF", bd=0, padx=20, pady=10, command=generate_qr)
generate_button.pack(side="left", padx=10)

save_button = tk.Button(button_frame, text="Save QR", font=("Segoe UI", 12), bg="#007BFF", fg="#FFFFFF", bd=0, padx=20, pady=10, command=save_qr)
save_button.pack(side="left", padx=10)

# QR Code Display
qr_label = tk.Label(root, bg="#F9FAFB")
qr_label.pack()

# Footer
footer = tk.Label(root, text="© 2024 QR Generator", font=("Segoe UI", 10), bg="#F9FAFB", fg="#9CA3AF")
footer.pack(side="bottom", pady=10)

# Start the GUI loop
root.mainloop()
