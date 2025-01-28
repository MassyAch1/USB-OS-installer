import argparse
from utils import list_usb_drives, format_usb_drive
from iso_handler import read_iso

def main():
    parser = argparse.ArgumentParser(description="USB Installer for OS")
    parser.add_argument("iso", help="Path to the ISO file")
    parser.add_argument("usb", help="USB drive to install the OS")
    
    args = parser.parse_args()
    
    # List available USB drives
    usb_drives = list_usb_drives()
    print("Available USB drives:", usb_drives)
    
    # Format the USB drive
    format_usb_drive(args.usb)
    
    # Read the ISO file
    read_iso(args.iso)

if __name__ == "__main__":
    main()
