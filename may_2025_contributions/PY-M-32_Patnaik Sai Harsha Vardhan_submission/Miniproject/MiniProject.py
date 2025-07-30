#File Organizer mini project 
import os
from pathlib import Path
import shutil

# Mapping extensions to folder names
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Docs": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def get_category(ext):
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(directory):
    for entry in os.scandir(directory):
        if entry.is_file():
            ext = Path(entry.name).suffix.lower()
            category = get_category(ext)
            dest_folder = Path(directory) / category
            dest_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(entry.path), str(dest_folder / entry.name))
                print(f"Moved {entry.name} to {dest_folder}")
            except Exception as e:
                print(f"Could not move {entry.name}: {e}")

if __name__ == "__main__":
    organize_files(os.getcwd())
