import tkinter as tk
from tkinter import filedialog, messagebox
from utils import list_usb_drives, format_usb_drive
from iso_handler import read_iso

def install_os(iso_path, usb_drive):
    try:
        # Format the USB drive
        format_usb_drive(usb_drive)
        
        # Read the ISO file
        read_iso(iso_path)
        
        messagebox.showinfo("Success", "OS installation completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_iso():
    iso_path = filedialog.askopenfilename(filetypes=[("ISO files", "*.iso")])
    iso_entry.delete(0, tk.END)
    iso_entry.insert(0, iso_path)

def browse_usb():
    usb_drive = filedialog.askdirectory()
    usb_entry.delete(0, tk.END)
    usb_entry.insert(0, usb_drive)

# Create the main window
root = tk.Tk()
root.title("USB OS Installer")

# ISO file selection
tk.Label(root, text="ISO File:").grid(row=0, column=0)
iso_entry = tk.Entry(root, width=50)
iso_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_iso).grid(row=0, column=2)

# USB drive selection
tk.Label(root, text="USB Drive:").grid(row=1, column=0)
usb_entry = tk.Entry(root, width=50)
usb_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_usb).grid(row=1, column=2)

# Install button
tk.Button(root, text="Install OS", command=lambda: install_os(iso_entry.get(), usb_entry.get())).grid(row=2, columnspan=3)

root.mainloop()
