# File Organizer

## Project Description

The File Organizer is a Python project that automatically sorts files in a directory into categorized subfolders based on their file extensions. It includes a simple command-line Python script and a Django-based web UI for organizing files on the server.

---

## Features

### Python Script
- Organizes files by categories such as Images, Documents, Audio, Videos, Archives, Code, and Others.
- Creates destination folders automatically if they do not exist.
- Easy to run locally without dependencies beyond Python 3.x standard library.

### Django Web UI
- Provides a web interface to select and organize directories on the server.
- Displays moved files and any errors encountered.
- Requires Django for setup and operation.

---

## Requirements

- Python 3.x
- Django (for the web UI)

---

## Usage

### Python Script

1. Place `organizer.py` in the directory you want to organize.
2. Run the script:
3. Files in the directory will be sorted automatically.

### Django Web UI

1. Add the `fileorganizer` app to your Django project.
2. Include `fileorganizer.urls` in your project's `urls.py`.
3. Run the Django development server:
4. Open the browser at `http://127.0.0.1:8000/`.
5. Enter the absolute directory path to organize and submit.

---

## File Categories and Extensions

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Docs:** `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Audio:** `.mp3`, `.wav`, `.aac`
- **Videos:** `.mp4`, `.mov`, `.avi`, `.mkv`
- **Archives:** `.zip`, `.tar`, `.gz`, `.rar`
- **Code:** `.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`
- **Others:** Any unrecognized file extensions

---

## Possible Extensions

- Recursive organization inside subdirectories.
- Custom extensions mapping via config or user input.
- “Dry-run” mode preview.
- Logging enhancements.
- User authentication and permissions in Django UI.
- File upload support via the web interface.

