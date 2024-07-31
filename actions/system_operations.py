from tkinter import filedialog
from tkinter import messagebox
import pathlib


def select_file(entry):
    file_path = filedialog.askopenfilename(title="Select audio file")
    extension = pathlib.Path(file_path).suffix
    if extension == ".mp3" or extension == ".wav":
        entry.delete(0, 'end')
        entry.insert(0, file_path)
    else:
        messagebox.showerror(title="Unsupported file type", message=f"Invalid file type {extension}\n\nSupported file types: .mp3, .wav")


def select_directory(entry):
    dir_path = filedialog.askdirectory(title="Select download directory")
    if dir_path:
        entry.delete(0, 'end')
        entry.insert(0, dir_path)