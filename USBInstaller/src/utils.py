import os
import platform
import subprocess

def list_usb_drives():
    """List available USB drives."""
    drives = []
    if platform.system() == "Windows":
        # Use wmic to list USB drives
        result = subprocess.run(["wmic", "logicaldisk", "where", "drivetype=2", "get", "deviceid"], capture_output=True, text=True)
        drives = result.stdout.splitlines()[1:]  # Skip the header
        drives = [drive.strip() for drive in drives if drive.strip()]  # Clean up the list
    else:
        # List drives in Linux/Mac
        drives = [f"/dev/sd{chr(d)}" for d in range(ord('a'), ord('z') + 1) if os.path.exists(f"/dev/sd{chr(d)}")]
        # Check mounted drives in /media or /mnt
        drives += [os.path.join('/media', d) for d in os.listdir('/media') if os.path.isdir(os.path.join('/media', d))]
        drives += [os.path.join('/mnt', d) for d in os.listdir('/mnt') if os.path.isdir(os.path.join('/mnt', d))]
    return drives

def format_usb_drive(drive):
    """Format the specified USB drive."""
    print(f"Formatting {drive}...")
    if not os.path.exists(drive):
        raise FileNotFoundError(f"The specified drive does not exist: {drive}")
    
    try:
        if platform.system() == "Windows":
            # Format command for Windows
            subprocess.run(["format", drive, "/FS:NTFS", "/Q", "/Y"], check=True)
        else:
            # Format command for Linux
            subprocess.run(["mkfs.vfat", drive], check=True)
    except Exception as e:
        raise RuntimeError(f"Failed to format the drive: {e}")
