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
            # Use diskpart to format the drive on Windows
            script = f"""
            select volume {drive[0]}
            clean
            create partition primary
            format fs=ntfs quick
            assign
            """
            script_file = "format_script.txt"
            with open(script_file, "w") as f:
                f.write(script)
            subprocess.run(["diskpart", "/s", script_file], check=True)
            os.remove(script_file)
        else:
            # Use mkfs.vfat to format the drive on Linux/Mac
            # Ensure the drive is unmounted first
            subprocess.run(["umount", drive], stderr=subprocess.DEVNULL)
            subprocess.run(["mkfs.vfat", drive], check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to format the drive: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")