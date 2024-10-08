import tkinter
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, ttk
from src.actions import system_operations
from src.audio import wav_functions
from src.audio import youtube_functions
from tkinter import messagebox
import os
import sys

OUTPUT_PATH = str(Path(__file__).parent)
ASSETS_PATH = OUTPUT_PATH + r"\assets\frame0"
youtube_path = ''
file_path = ''

selected_convert = ''
selected_download = ''
input_type = ''

### Functions ###

def select_audio_file():
    system_operations.select_file(entry_2)

def select_download_dir():
    system_operations.select_directory(entry_3)

def reset():
    global youtube_path
    global  selected_convert
    global  input_type
    global file_path
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')
    entry_6.delete(0, 'end')
    entry_7.delete(0, 'end')
    entry_8.delete(0, 'end')
    files = os.listdir('../../temp')
    for file in files:
        file_path = os.path.join('../../temp', file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    canvas.itemconfig(status_text, text=" Not Submitted", fill="#fcd303")
    canvas.itemconfig(resample_text, text='')
    canvas.itemconfig(convert_text, text='')
    youtube_path = ''
    file_path = ''
    selected_convert = ''
    input_type = ''


def check_input():
    input_1 = entry_1.get()
    input_2 = entry_2.get()
    global input_type

    if input_1 and input_2:
        entry_1.delete(0, 'end')
        entry_2.delete(0, 'end')
        canvas.itemconfig(status_text, text=" Error: both fields entered", fill="#fc0303")
    elif input_1:
        check_temp()
        if system_operations.is_connected():
            try:
                global youtube_path
                youtube_path = youtube_functions.view_youtube_audio(input_1)
                canvas.itemconfig(status_text, text=" Link Uploaded", fill='#03fc0b')

                for temp_file in ['../../temp/spectrogram.png', '../../temp/waveform.png']:
                    if os.path.isfile(temp_file):
                        os.remove(temp_file)
                bitrate, file_type = wav_functions.get_audio_info(youtube_path)
                canvas.itemconfig(convert_text, text=f"{file_type}")
                canvas.itemconfig(resample_text, text=f"{bitrate}kbps")
                show_spectrogram(youtube_path)
                show_waveform(youtube_path)
                input_type = 'link'
            except Exception as ex:
                print(ex)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                canvas.itemconfig(status_text, text=" Link Error", fill="#fc0303")
                messagebox.showerror(message=f"{ex}")
                entry_1.delete(0, 'end')
                youtube_path = ''
                input_type = ''
    elif input_2:
        check_temp()
        file_path = input_2
        if not os.path.exists(file_path):
            canvas.itemconfig(status_text, text=f" File DNE: {os.path.basename(file_path)}", fill='#fc0303')
            entry_2.delete(0, 'end')
            return
        canvas.itemconfig(status_text, text=" File Inputted", fill='#03fc0b')

        for temp_file in ['../../temp/spectrogram.png', '../../temp/waveform.png']:
            if os.path.isfile(temp_file):
                os.remove(temp_file)
        bitrate, file_type = wav_functions.get_audio_info(file_path)
        canvas.itemconfig(convert_text, text=f"{file_type}")
        canvas.itemconfig(resample_text, text=f"{bitrate}kbps")
        show_spectrogram(file_path)
        show_waveform(file_path)
        input_type = 'file'
    else:
        canvas.itemconfig(status_text, text=" Not Submitted", fill="#fcd303")
        input_type = ''


def show_spectrogram(file_path):
    if os.path.exists(file_path):
        wav_functions.generate_visual_spectrogram(file_path)
        spectrogram = wav_functions.load_spectrogram()
        label = tkinter.Label(image=spectrogram)
        label.image =  spectrogram
        label.place(x=975, y=56.0)

def show_waveform(file_path):
    if os.path.exists(file_path):
        wav_functions.generate_visual_waveform(file_path)
        waveform = wav_functions.load_waveform()
        label2 = tkinter.Label(image=waveform)
        label2.image = waveform
        label2.place(x=975, y=282)

def download_spectrogram():
    check_temp()
    try:
        file_path = ''
        if os.path.exists(entry_2.get()):
            file_path = entry_2.get()
        elif entry_1.get():
            global youtube_path
            file_path = youtube_path
        width = entry_4.get()
        height = entry_6.get()

        if os.path.exists(entry_3.get()):
            if os.path.exists(file_path):
                if width and height:
                    if os.path.exists(f"{os.path.join(entry_3.get(), f"{Path(file_path).stem}_spec{width}x{height}.png")}"):
                        os.remove(f"{os.path.join(entry_3.get(), f"{Path(file_path).stem}_spec{width}x{height}.png")}")

                    wav_functions.generate_download_spectrogram(width, height, file_path, entry_3.get())
                    if os.path.exists(f"{os.path.join(entry_3.get(), f"{Path(file_path).stem}_spec{width}x{height}.png")}"):
                        messagebox.showinfo(title="Download Successful!", message=f"Successfully downloaded to {os.path.join(entry_3.get(), f"{Path(file_path).stem}_spec{width}x{height}.png")}")
                else:
                    messagebox.showerror(title="Dimensions not specified", message="Width or height field is empty")
            else:
                messagebox.showerror(title="No path given", message="No valid file given")
        else:
            messagebox.showerror(title="No download path", message="No valid download path given")
    except Exception as ex:
        messagebox.showerror(title="Error" ,message=f"{ex}")

def download_wavefile():
    check_temp()
    try:
        file_path = ''
        if os.path.exists(entry_2.get()):
            file_path = entry_2.get()
        elif entry_1.get():
            global youtube_path
            file_path = youtube_path
        width = entry_5.get()
        height = entry_7.get()

        if os.path.exists(entry_3.get()):
            if os.path.exists(file_path):
                if width and height:
                    if os.path.exists(
                            f"{os.path.join(entry_3.get(), f"{Path(file_path).stem}_waveform{width}x{height}.png")}"):
                        os.remove(
                            f"{os.path.join(entry_3.get(), f"{Path(file_path).stem}_waveform{width}x{height}.png")}")

                    wav_functions.generate_download_waveform(width, height, file_path, entry_3.get())
                    if os.path.exists(
                            f"{os.path.join(entry_3.get(), f"{Path(file_path).stem}_waveform{width}x{height}.png")}"):
                        messagebox.showinfo(title="Download Successful!",
                                            message=f"Successfully downloaded to {os.path.join(entry_3.get(), f"{Path(file_path).stem}_waveform{width}x{height}.png")}")
                else:
                    messagebox.showerror(title="Dimensions not specified", message="Width or height field is empty")
            else:
                messagebox.showerror(title="No path given", message="No valid file given")
        else:
            messagebox.showerror(title="No download path", message="No valid download path given")
    except Exception as ex:
        messagebox.showerror(title="Error", message=f"{ex}")

def download_visual_eq():
    if os.path.exists(entry_3.get()):
        print("Download visual eq button")
        # TODO Implement visual eq download
    else:
        messagebox.showerror(title="No path given", message="No valid download path given")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def cleanup():
    try:
        files = os.listdir('../../temp')
        for file in files:
            file_path = os.path.join('../../temp',file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        window.destroy()
    except OSError:
        pass

def check_temp():
    if not os.path.exists('../../temp'):
        os.makedirs('../../temp')

def on_select_convert(event):
    global selected_convert
    selected_convert = convert_combobox.get()
    print(f"Selected option = {selected_convert}")

def on_select_download(event):
    global selected_download
    selected_download = download_combobox.get()
    print(f"Selected option = {selected_download}")



### GUI Implementation ###

window = Tk()

window.geometry("1500x800")
window.configure(bg = "#242424")
window.title("VisAudio")

convert_options = ['','mp3', 'wav', 'ogg', 'm4a', 'flac']
convert_combobox = ttk.Combobox(window, values=convert_options, state='readonly', font=('Calibri', 16))
convert_combobox.place(x=500, y=525, height=30, width=150)

download_options = ['', 'Converted File', 'Resampled File', 'Combined', 'Raw (Link Only)']
download_combobox = ttk.Combobox(window, values=download_options, state='readonly', font=('Calibri', 16))
download_combobox.place(x=517, y=695, height=30, width=150)

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
    font=("Calibri Bold", 24 * -1)
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
    font=("Calibri Bold", 24 * -1)
)

canvas.create_text(
    59.0,
    179.0,
    anchor="nw",
    text="Audio File Path",
    fill="#D9D9D9",
    font=("Calibri Bold", 24 * -1)
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

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    378.0,
    545.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    378.0,
    630.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    547.0,
    715.0,
    image=image_image_11
)

convert_text = canvas.create_text(
    270.0,
    526.0,
    anchor="nw",
    text="",
    fill="#03fc0b",
    font=("Calibri Bold", 26 * -1)
)

resample_text = canvas.create_text(
    295.0,
    612.0,
    anchor="nw",
    text="",
    fill="#03fc0b",
    font=("Calibri Bold", 26 * -1)
)

canvas.create_text(
    70.0,
    522.0,
    anchor="nw",
    text="Convert from :",
    fill="#FFFFFF",
    font=("Calibri Bold", 32 * -1)
)

canvas.create_text(
    70.0,
    607.0,
    anchor="nw",
    text="Resample from :",
    fill="#FFFFFF",
    font=("Calibri Bold", 32 * -1)
)

canvas.create_text(
    785.0,
    111.0,
    anchor="nw",
    text="Width",
    fill="#FFFFFF",
    font=("Calibri Bold", 20 * -1)
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    580.0,
    545.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    580.0,
    629.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    597.0,
    715.0,
    image=image_image_14
)

canvas.create_text(
    785.0,
    330.0,
    anchor="nw",
    text="Width",
    fill="#FFFFFF",
    font=("Calibri Bold", 20 * -1)
)

canvas.create_text(
    785.0,
    165.0,
    anchor="nw",
    text="Height",
    fill="#FFFFFF",
    font=("Calibri Bold", 20 * -1)
)

canvas.create_text(
    785.0,
    391.0,
    anchor="nw",
    text="Height",
    fill="#FFFFFF",
    font=("Calibri Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    355.0,
    103.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font="Calibri 16",
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
    249.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font="Calibri 16",
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
font="Calibri 16",
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
    font=("Calibri Bold", 40 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    654.0,
    104.0,
    image=image_image_15
)

canvas.create_text(
    776.0,
    51.0,
    anchor="nw",
    text="Spectrogram",
    fill="#FFFFFF",
    font=("Calibri Bold", 26 * -1)
)

canvas.create_text(
    790.0,
    281.0,
    anchor="nw",
    text="Waveform",
    fill="#FFFFFF",
    font=("Calibri Bold", 26 * -1)
)

canvas.create_text(
    798.0,
    563.0,
    anchor="nw",
    text="Visual EQ",
    fill="#FFFFFF",
    font=("Calibri Bold", 26 * -1)
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    1215.0,
    158.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    1215.0,
    387.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    1215.0,
    641.0,
    image=image_image_18
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
    command=lambda: print(f"{selected_convert}"),
    relief="flat"
)
button_2.place(
    x=400.0,
    y=690.0,
    width=102,
    height=43.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=70.0,
    y=690.0,
    width=95.0,
    height=43.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=download_wavefile,
    relief="flat"
)
button_4.place(
    x=788.0,
    y=448.0,
    width=147.0,
    height=45.0
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
font="Calibri 16",
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
font="Calibri 16",
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
font="Calibri 16",
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
font="Calibri 16",
    highlightthickness=0
)
entry_7.place(
    x=866.0,
    y=388.0,
    width=56.0,
    height=30.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    550.0,
    622.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font="Calibri 24",
    highlightthickness=0
)
entry_8.place(
    x=500.0,
    y=607.0,
    width=90.0,
    height=30.0
)

canvas.create_text(
    610.0,
    607.0,
    anchor="nw",
    text="kbps",
    fill="#FFFFFF",
    font=("Calibri Bold", 24 * -1)
)



canvas.create_rectangle(
    768.0,
    268.00000719765916,
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

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=check_input,
    relief="flat"
)
button_6.place(
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
    font=("Calibri Bold", 24 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=786.0,
    y=674.0,
    width=82.0,
    height=65.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=860.0,
    y=675.0,
    width=86.0,
    height=62.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=select_audio_file,
    relief="flat"
)
button_9.place(
    x=622.0,
    y=221.0,
    width=66.0,
    height=56.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=select_download_dir,
    relief="flat"
)
button_10.place(
    x=618.0,
    y=428.0,
    width=66.0,
    height=56.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=290.0,
    y=686.0,
    width=66.0,
    height=56.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=reset,
    relief="flat"
)
button_12.place(
    x=80.0,
    y=293.0,
    width=66.0,
    height=56.0
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    445.0,
    543.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    445.0,
    629.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    122.0,
    715.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    290.0,
    715.0,
    image=image_image_22
)

canvas.create_text(
    215.0,
    686.0,
    anchor="nw",
    text="Refresh",
    fill="#FFFFFF",
    font=("Calibri Bold", 20 * -1)
)

canvas.create_text(
    215.0,
    710.0,
    anchor="nw",
    text="Graphs",
    fill="#FFFFFF",
    font=("Calibri Bold", 20 * -1)
)

convert_combobox.lift()
download_combobox.lift()
convert_combobox.bind("<<ComboboxSelected>>", on_select_convert)
download_combobox.bind("<<ComboboxSelected>>", on_select_download)
window.protocol('WM_DELETE_WINDOW', cleanup)
window.resizable(False, False)
window.mainloop()

