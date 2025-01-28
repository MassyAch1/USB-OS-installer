import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from utils import list_usb_drives, format_usb_drive
from iso_handler import read_iso

def install_os(iso_path, usb_drive):
    try:
        print(f"Selected USB Drive: {usb_drive}")  # Debugging line
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

def refresh_usb_drives():
    usb_combobox['values'] = list_usb_drives()
    if usb_combobox['values']:
        usb_combobox.current(0)  # Select the first drive by default

# Create the main window
root = tk.Tk()
root.title("USB OS Installer")
root.geometry("500x200")  # Set a fixed size for the window

# Create a frame for better layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# ISO file selection
tk.Label(frame, text="ISO File:").grid(row=0, column=0, sticky="w")
iso_entry = tk.Entry(frame, width=40)
iso_entry.grid(row=0, column=1, padx=5)
tk.Button(frame, text="Browse", command=browse_iso).grid(row=0, column=2)

# USB drive selection
tk.Label(frame, text="USB Drive:").grid(row=1, column=0, sticky="w")
usb_combobox = ttk.Combobox(frame, width=37)
usb_combobox.grid(row=1, column=1, padx=5)
tk.Button(frame, text="Refresh", command=refresh_usb_drives).grid(row=1, column=2)

# Install button
tk.Button(frame, text="Install OS", command=lambda: install_os(iso_entry.get(), usb_combobox.get()), bg="green", fg="white").grid(row=2, columnspan=3, pady=10)

# Initial population of USB drives
refresh_usb_drives()

root.mainloop()
