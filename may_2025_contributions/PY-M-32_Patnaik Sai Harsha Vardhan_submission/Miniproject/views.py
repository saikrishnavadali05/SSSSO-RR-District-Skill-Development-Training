#fileorganizer/views.py
from django.shortcuts import render
from pathlib import Path
import shutil
import os

EXTENSION_MAP = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.tiff': 'Images',
    '.pdf': 'Docs',
    '.doc': 'Docs',
    '.docx': 'Docs',
    '.txt': 'Docs',
    '.xls': 'Docs',
    '.xlsx': 'Docs',
    '.ppt': 'Docs',
    '.pptx': 'Docs',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.aac': 'Audio',
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.zip': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.rar': 'Archives',
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code',
    '.css': 'Code',
    '.java': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
}

def organize_files(target_dir: Path):
    moved_files = []
    errors = []
    if not target_dir.is_dir():
        errors.append(f"{target_dir} is not a valid directory.")
        return moved_files, errors

    try:
        with os.scandir(target_dir) as entries:
            for entry in entries:
                if entry.is_file():
                    file_path = Path(entry.path)
                    file_ext = file_path.suffix.lower()
                    folder_name = EXTENSION_MAP.get(file_ext, 'Others')
                    destination_folder = target_dir / folder_name
                    destination_folder.mkdir(exist_ok=True)
                    destination = destination_folder / file_path.name
                    shutil.move(str(file_path), str(destination))
                    moved_files.append(file_path.name)
    except Exception as e:
        errors.append(str(e))
    return moved_files, errors

def index(request):
    context = {}
    if request.method == 'POST':
        dir_path = request.POST.get('directory')
        target_dir = Path(dir_path)
        moved_files, errors = organize_files(target_dir)
        context['moved_files'] = moved_files
        context['errors'] = errors
        context['directory'] = dir_path
    return render(request, 'fileorganizer/index.html', context)
