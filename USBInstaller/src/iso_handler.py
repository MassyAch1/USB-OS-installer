import os
import shutil
import zipfile

def read_iso(iso_path):
    """Read the ISO file and extract its contents."""
    print(f"Reading ISO file: {iso_path}")
    if not os.path.exists(iso_path):
        raise FileNotFoundError(f"ISO file not found: {iso_path}")
    
    # Create a temporary directory to extract the ISO contents
    temp_dir = "temp_iso_extraction"
    os.makedirs(temp_dir, exist_ok=True)

    # Extract the ISO file
    with zipfile.ZipFile(iso_path, 'r') as iso_zip:
        iso_zip.extractall(temp_dir)
    
    print(f"ISO contents extracted to: {temp_dir}")
    return temp_dir
