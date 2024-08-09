import os.path
from tkinter import filedialog
from tkinter import messagebox
import pathlib
import requests


SUPPORTED_EXTENSIONS = {'.mp3', '.wav', '.ogg', '.m4a', '.flac'}

def select_file(entry):
    file_path = filedialog.askopenfilename(title="Select audio file")
    if file_path:
        extension = pathlib.Path(file_path).suffix.lower()
        if extension in SUPPORTED_EXTENSIONS:
            entry.delete(0, 'end')
            entry.insert(0, file_path)
        else:
            messagebox.showerror(
                title="Unsupported file type",
                message=f"Invalid file type {extension}\n\nSupported file types: {', '.join(SUPPORTED_EXTENSIONS)}"
            )

def select_directory(entry):
    dir_path = filedialog.askdirectory(title="Select download directory")
    if dir_path:
        entry.delete(0, 'end')
        entry.insert(0, dir_path)


def is_connected():
    url = "https://www.youtube.com"
    try:
        response = requests.get(url, timeout=5)
        return True
    except requests.ConnectionError:
        return False