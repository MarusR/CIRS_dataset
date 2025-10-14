import os
import gdown
import zipfile 

# config
google_drive_file_id = '1HbUYIozzIUaQsz4PpnkaKbGndnFwLkLJ'
output_zip_path = 'data/raw/wdi_data.zip'
extract_to_path = 'data/raw/'

# === Ensure data/raw directory exists ===
os.makedirs(extract_to_path, exist_ok=True)

# === Download ZIP from Google Drive ===
print(f"Downloading file from Google Drive (ID: {google_drive_file_id})...")
gdown.download(id=google_drive_file_id, output=output_zip_path, quiet=False)

# === Unzip into data/raw ===
print(f"Extracting {output_zip_path} into {extract_to_path}...")
with zipfile.ZipFile(output_zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

# === Cleanup ZIP file (optional) ===
os.remove(output_zip_path)
print("Download and extraction complete.")