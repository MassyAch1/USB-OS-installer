import os
import platform
import subprocess

def list_usb_drives():
    """List available USB drives."""
    drives = []
    if platform.system() == "Windows":
        # List drives in Windows
        drives = [f"{d}:\\" for d in range(65, 91) if os.path.exists(f"{d}:")]
    else:
        # List drives in Linux/Mac
        drives = [f"/dev/sd{chr(d)}" for d in range(ord('a'), ord('z') + 1) if os.path.exists(f"/dev/sd{chr(d)}")]
    return drives

def format_usb_drive(drive):
    """Format the specified USB drive."""
    print(f"Formatting {drive}...")
    if platform.system() == "Windows":
        # Format command for Windows
        subprocess.run(["format", drive, "/FS:NTFS", "/Q", "/Y"], check=True)
    else:
        # Format command for Linux
        subprocess.run(["mkfs.vfat", drive], check=True)
