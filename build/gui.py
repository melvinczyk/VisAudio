import tkinter
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from actions import system_operations
from audio import wav_functions
from tkinter import messagebox
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Nick\Documents\VisAudio\build\assets\frame0")

### Functions ###

def select_audio_file():
    system_operations.select_file(entry_2)

def select_download_dir():
    system_operations.select_directory(entry_3)

def check_input():
    if entry_1.get() and entry_2.get():
        entry_1.delete(0, 'end')
        entry_2.delete(0, 'end')
        canvas.itemconfig(status_text, text=" Error: both fields entered", fill="#fc0303")
    elif entry_1.get():
        # TODO YouTube link download function
        pass
    elif entry_2.get():
        if os.path.exists(entry_2.get()):
            print("File exists")
        else:
            canvas.itemconfig(status_text, text=f" File DNE: {os.path.basename(entry_2.get())}", fill='#fc0303')
            entry_2.delete(0, 'end')
            return
        # TODO implement file conversion logic
        canvas.itemconfig(status_text, text=" File Inputted", fill='#03fc0b')
        if os.path.isfile('../../temp/spectrogram.png'):
            os.remove('../../temp/spectrogram.png')
        if os.path.isfile('../../temp/waveform.png'):
            os.remove('../../temp/waveform.png')
        show_spectrogram()
        show_waveform()
        pass
    else:
        canvas.itemconfig(status_text, text=" Not Submitted", fill="#fcd303")

def show_spectrogram():
    if entry_2.get():
        wav_functions.generate_visual_spectrogram(entry_2.get())
        spectrogram = wav_functions.load_spectrogram()
        label = tkinter.Label(image=spectrogram)
        label.image =  spectrogram
        label.place(x=975, y=56.0)
        # canvas.create_image(750, 400, anchor='nw', image=image)

def show_waveform():
    if entry_2.get():
        wav_functions.generate_visual_waveform(entry_2.get())
        waveform = wav_functions.load_waveform()
        label2 = tkinter.Label(image=waveform)
        label2.image = waveform
        label2.place(x=975, y=282)
def download_spectrogram():
    if os.path.exists(entry_3.get()) and os.path.exists(entry_2.get()):
        if entry_4.get() and entry_6.get():
            if os.path.exists(f"{os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_spec{entry_4.get()}x{entry_6.get()}.png")}"):
                os.remove(f"{os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_spec.{entry_4.get()}x{entry_6.get()}png")}")
            wav_functions.generate_download_spectrogram(entry_4.get(), entry_6.get(), entry_2.get(), entry_3.get())
            if os.path.exists(f"{os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_spec{entry_4.get()}x{entry_6.get()}.png")}"):
                messagebox.showinfo(title="Download Successful!", message=f"Successfully downloaded to {os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_spec{entry_4.get()}x{entry_6.get()}.png")}")
        else:
            messagebox.showerror(title="Dimensions not specified", message="Width or height field is empty")
    else:
        messagebox.showerror(title="No path given", message="No valid download path or file given")

def download_wavefile():
    if os.path.exists(entry_3.get()):
        print("Download wavefile button")
        if entry_5.get() and entry_7.get():
            if os.path.exists(f"{os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_waveform{entry_5.get()}x{entry_7.get()}.png")}"):
                os.remove(f"{os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_waveform{entry_5.get()}x{entry_7.get()}.png")}")
            wav_functions.generate_download_waveform(entry_5.get(), entry_7.get(), entry_2.get(), entry_3.get())
            if os.path.exists(f"{os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_waveform{entry_5.get()}x{entry_7.get()}.png")}"):
                messagebox.showinfo(title="Download Successful!", message=f"Successfully downloaded to {os.path.join(entry_3.get(), f"{Path(entry_2.get()).stem}_waveform{entry_5.get()}x{entry_7.get()}.png")}")
            else:
                messagebox.showerror(title="Dimensions not specified", message="Width or height field is empty")
        else:
            messagebox.showerror(title="No path given", message="No valid download path or file given")

def download_visual_eq():
    if os.path.exists(entry_3.get()):
        print("Download visual eq button")
        # TODO Implement spectrogram download
    else:
        messagebox.showerror(title="No path given", message="No valid download path given")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




### GUI Implementation ###

window = Tk()

window.geometry("1500x800")
window.configure(bg = "#242424")


canvas = Canvas(
    window,
    bg = "#242424",
    height = 800,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    750.0,
    400.0,
    image=image_image_1
)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    377.0,
    194.0,
    image=image_image_2
)

canvas.create_text(
    340.0,
    303.0,
    anchor="nw",
    text="Status:",
    fill="#FFFFFF",
    font=("Inika Bold", 24 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    377.0,
    580.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    378.0,
    110.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    378.0,
    253.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    377.0,
    583.0,
    image=image_image_6
)

canvas.create_text(
    59.0,
    40.0,
    anchor="nw",
    text="Valid YouTube Link",
    fill="#D9D9D9",
    font=("Inika Bold", 24 * -1)
)

canvas.create_text(
    59.0,
    179.0,
    anchor="nw",
    text="Audio File Path",
    fill="#D9D9D9",
    font=("Inika Bold", 24 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1113.0,
    407.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    378.0,
    460.0,
    image=image_image_8
)

canvas.create_text(
    785.0,
    111.0,
    anchor="nw",
    text="Width",
    fill="#FFFFFF",
    font=("Inika Bold", 20 * -1)
)

canvas.create_text(
    785.0,
    330.0,
    anchor="nw",
    text="Width",
    fill="#FFFFFF",
    font=("Inika Bold", 20 * -1)
)

canvas.create_text(
    785.0,
    165.0,
    anchor="nw",
    text="Height",
    fill="#FFFFFF",
    font=("Inika Bold", 20 * -1)
)

canvas.create_text(
    785.0,
    391.0,
    anchor="nw",
    text="Height",
    fill="#FFFFFF",
    font=("Inika Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    355.0,
    104.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=103.0,
    y=82.0,
    width=504.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    356.0,
    250.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=104.0,
    y=228.0,
    width=504.0,
    height=43.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    355.0,
    456.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=103.0,
    y=433.0,
    width=504.0,
    height=44.0
)

canvas.create_text(
    349.0,
    151.0,
    anchor="nw",
    text="or",
    fill="#FFFFFF",
    font=("Inika Bold", 40 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    654.0,
    104.0,
    image=image_image_9
)

canvas.create_text(
    776.0,
    51.0,
    anchor="nw",
    text="Spectrogram",
    fill="#FFFFFF",
    font=("Inika Bold", 26 * -1)
)

canvas.create_text(
    790.0,
    281.0,
    anchor="nw",
    text="Waveform",
    fill="#FFFFFF",
    font=("Inika Bold", 26 * -1)
)

canvas.create_text(
    798.0,
    563.0,
    anchor="nw",
    text="Visual EQ",
    fill="#FFFFFF",
    font=("Inika Bold", 26 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1215.0,
    158.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1215.0,
    387.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1215.0,
    641.0,
    image=image_image_12
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=download_spectrogram,
    relief="flat"
)
button_1.place(
    x=791.0,
    y=221.0,
    width=147.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=download_wavefile,
    relief="flat"
)
button_2.place(
    x=788.0,
    y=448.0,
    width=147.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=download_visual_eq,
    relief="flat"
)
button_3.place(
    x=789.0,
    y=615.0,
    width=148.0,
    height=46.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    894.0,
    124.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=866.0,
    y=108.0,
    width=56.0,
    height=30.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    894.0,
    346.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=866.0,
    y=330.0,
    width=56.0,
    height=30.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    894.0,
    178.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=866.0,
    y=162.0,
    width=56.0,
    height=30.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    894.0,
    404.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=866.0,
    y=388.0,
    width=56.0,
    height=30.0
)

canvas.create_rectangle(
    768.0,
    268.0000071976591,
    1460.9996337890625,
    269.0879821777344,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    768.0,
    497.00000719765916,
    1460.9996337890625,
    498.0879821777344,
    fill="#FFFFFF",
    outline="")

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=check_input,
    relief="flat"
)
button_4.place(
    x=144.0,
    y=295.0,
    width=179.0,
    height=48.0
)

status_text = canvas.create_text(
    415.0,
    303.0,
    anchor="nw",
    text=" Not Submitted",
    fill="#fcd303",
    font=("Inika Bold", 24 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=786.0,
    y=674.0,
    width=82.0,
    height=65.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=860.0,
    y=675.0,
    width=86.0,
    height=62.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=select_audio_file,
    relief="flat"
)
button_7.place(
    x=622.0,
    y=221.0,
    width=66.0,
    height=56.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=select_download_dir,
    relief="flat"
)
button_8.place(
    x=618.0,
    y=428.0,
    width=66.0,
    height=56.0
)


window.resizable(False, False)
window.mainloop()

