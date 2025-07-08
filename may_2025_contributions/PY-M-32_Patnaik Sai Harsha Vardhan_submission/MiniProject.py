#Mini Project: File Organizer Script 
import os
from pathlib import Path

def organize_files():
    # Define the mapping of file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.h', '.php', '.rb'],
        'Executables': ['.exe', '.msi', '.dmg', '.app'],
        'Others': []  # For files with extensions not in the above categories
    }
    
    # Get current directory
    current_dir = Path('.')
    
    # Scan all items in the current directory
    with os.scandir(current_dir) as entries:
        for entry in entries:
            # Skip directories and hidden files
            if entry.is_file() and not entry.name.startswith('.'):
                file_path = Path(entry)
                file_ext = file_path.suffix.lower()
                
                # Determine the target folder
                target_folder = None
                for folder, extensions in file_types.items():
                    if file_ext in extensions:
                        target_folder = folder
                        break
                
                # If no matching folder found, use 'Others'
                if target_folder is None:
                    target_folder = 'Others'
                
                # Create the target folder if it doesn't exist
                try:
                    os.makedirs(target_folder, exist_ok=True)
                except Exception as e:
                    print(f"Error creating folder {target_folder}: {e}")
                    continue
                
                # Move the file
                try:
                    destination = current_dir / target_folder / file_path.name
                    file_path.rename(destination)
                    print(f"Moved {file_path.name} to {target_folder}/")
                except Exception as e:
                    print(f"Error moving {file_path.name}: {e}")

if __name__ == "__main__":
    print("Starting file organization...")
    organize_files()
    print("File organization completed!")