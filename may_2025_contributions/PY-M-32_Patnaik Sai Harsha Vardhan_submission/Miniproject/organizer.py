#File Organizer mini project 
import os
from pathlib import Path
import shutil

# Mapping from file extensions to folder names
EXTENSION_MAP = {
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.tiff': 'Images',

    # Documents
    '.pdf': 'Docs',
    '.doc': 'Docs',
    '.docx': 'Docs',
    '.txt': 'Docs',
    '.xls': 'Docs',
    '.xlsx': 'Docs',
    '.ppt': 'Docs',
    '.pptx': 'Docs',

    # Audio
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.aac': 'Audio',

    # Videos
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',

    # Archives
    '.zip': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.rar': 'Archives',

    # Code files
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.java': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
}

def organize_files(target_dir: Path):
    if not target_dir.is_dir():
        print(f"{target_dir} is not a valid directory.")
        return

    with os.scandir(target_dir) as entries:
        for entry in entries:
            if entry.is_file():
                file_path = Path(entry.path)
                file_ext = file_path.suffix.lower()
                folder_name = EXTENSION_MAP.get(file_ext, 'Others')  # Default folder

                destination_folder = target_dir / folder_name
                try:
                    destination_folder.mkdir(exist_ok=True)
                    destination = destination_folder / file_path.name

                    shutil.move(str(file_path), str(destination))
                    print(f"Moved {file_path.name} to {folder_name}/")
                except Exception as e:
                    print(f"Error moving file {file_path.name}: {e}")

if __name__ == "__main__":
    current_dir = Path.cwd()
    organize_files(current_dir)
