import tkinter
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, messagebox
from pathlib import Path

from src.actions import system_operations
from src.audio import wav_functions
from src.audio import youtube_functions
import os
import sys

OUTPUT_PATH = str(Path(__file__).parent)
ASSETS_PATH = OUTPUT_PATH + r"\assets\frame0"


class VisAudio:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800")
        self.root.configure(bg="#242424")
        self.root.title("VisAudio")

        self.youtube_path = ''
        self.file_path = ''
        self.selected_convert_item = ''
        self.selected_download_item = ''
        self.input_type = ''

        self.setup_ui()

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def setup_ui(self):
        self.convert_options = ['', 'mp3', 'wav', 'ogg', 'flac', 'm4a']
        self.convert_combobox = ttk.Combobox(window, values=self.convert_options, state='readonly',
                                             font=('Calibri', 16))
        self.convert_combobox.place(x=500, y=525, height=30, width=150)
        self.convert_combobox.bind("<<ComboboxSelected>>", self.on_select_convert)

        self.download_options = ['', 'Converted File', 'Resampled File', 'Combined', 'Raw (Link Only)']
        self.download_combobox = ttk.Combobox(self.root, values=self.download_options, state='readonly',
                                              font=('Calibri', 16))
        self.download_combobox.place(x=517, y=695, height=30, width=150)
        self.download_combobox.bind("<<ComboboxSelected>>", self.on_select_download)

        self.canvas = Canvas(
            window,
            bg="#242424",
            height=800,
            width=1500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.load_images()
        self.create_widgets()

        self.convert_combobox.lift()
        self.download_combobox.lift()

    def load_images(self):
        self.images = {
            "image_1": PhotoImage(file=self.relative_to_assets("image_1.png")),
            "image_2": PhotoImage(file=self.relative_to_assets("image_2.png")),
            "image_3": PhotoImage(file=self.relative_to_assets("image_3.png")),
            "image_4": PhotoImage(file=self.relative_to_assets("image_4.png")),
            "image_5": PhotoImage(file=self.relative_to_assets("image_5.png")),
            "image_6": PhotoImage(file=self.relative_to_assets("image_6.png")),
            "image_7": PhotoImage(file=self.relative_to_assets("image_7.png")),
            "image_8": PhotoImage(file=self.relative_to_assets("image_8.png")),
            "image_9": PhotoImage(file=self.relative_to_assets("image_9.png")),
            "image_10": PhotoImage(file=self.relative_to_assets("image_10.png")),
            "image_11": PhotoImage(file=self.relative_to_assets("image_11.png")),
            "image_12": PhotoImage(file=self.relative_to_assets("image_12.png")),
            "image_13": PhotoImage(file=self.relative_to_assets("image_13.png")),
            "image_14": PhotoImage(file=self.relative_to_assets("image_14.png")),
            "image_15": PhotoImage(file=self.relative_to_assets("image_15.png")),
            "image_16": PhotoImage(file=self.relative_to_assets("image_16.png")),
            "image_17": PhotoImage(file=self.relative_to_assets("image_17.png")),
            "image_18": PhotoImage(file=self.relative_to_assets("image_18.png")),
            "image_19": PhotoImage(file=self.relative_to_assets("image_19.png")),
            "image_20": PhotoImage(file=self.relative_to_assets("image_20.png")),
            "image_21": PhotoImage(file=self.relative_to_assets("image_21.png")),
            "image_22": PhotoImage(file=self.relative_to_assets("image_22.png")),
        }

    def create_widgets(self):
        self.canvas.create_image(750, 400, image=self.images["image_1"])
        self.canvas.create_image(377, 194, image=self.images["image_2"])
        self.canvas.create_image(377, 580, image=self.images["image_3"])
        self.canvas.create_image(377, 110, image=self.images["image_4"])
        self.canvas.create_image(377, 253, image=self.images["image_5"])
        self.canvas.create_image(377, 583, image=self.images["image_6"])
        self.canvas.create_image(1113, 407, image=self.images["image_7"])
        self.canvas.create_image(377, 460, image=self.images["image_8"])
        self.canvas.create_image(377, 545, image=self.images["image_9"])
        self.canvas.create_image(377, 630, image=self.images["image_10"])
        self.canvas.create_image(547, 715, image=self.images["image_11"])
        self.canvas.create_image(580, 545, image=self.images["image_12"])
        self.canvas.create_image(580, 629, image=self.images["image_13"])
        self.canvas.create_image(597, 715, image=self.images["image_14"])
        self.canvas.create_image(654, 104, image=self.images["image_15"])
        self.canvas.create_image(1215, 158, image=self.images["image_16"])
        self.canvas.create_image(1215, 387, image=self.images["image_17"])
        self.canvas.create_image(1215, 641, image=self.images["image_18"])
        self.canvas.create_image(445, 543, image=self.images["image_19"])
        self.canvas.create_image(445, 629, image=self.images["image_20"])
        self.canvas.create_image(122, 715, image=self.images["image_21"])
        self.canvas.create_image(290, 715, image=self.images["image_22"])

        self.canvas.create_text(340.0,303.0,anchor="nw",text="Status:",fill="#FFFFFF",font=("Calibri Bold", 24 * -1))
        self.canvas.create_text(
            59.0,
            40.0,
            anchor="nw",
            text="Valid YouTube Link",
            fill="#D9D9D9",
            font=("Calibri Bold", 24 * -1)
        )
        self.canvas.create_text(
            59.0,
            179.0,
            anchor="nw",
            text="Audio File Path",
            fill="#D9D9D9",
            font=("Calibri Bold", 24 * -1)
        )

        convert_text = self.canvas.create_text(
            270.0,
            526.0,
            anchor="nw",
            text="",
            fill="#03fc0b",
            font=("Calibri Bold", 26 * -1)
        )

        resample_text = self.canvas.create_text(
            295.0,
            612.0,
            anchor="nw",
            text="",
            fill="#03fc0b",
            font=("Calibri Bold", 26 * -1)
        )

        self.canvas.create_text(
            70.0,
            522.0,
            anchor="nw",
            text="Convert from :",
            fill="#FFFFFF",
            font=("Calibri Bold", 32 * -1)
        )

        self.canvas.create_text(
            70.0,
            607.0,
            anchor="nw",
            text="Resample from :",
            fill="#FFFFFF",
            font=("Calibri Bold", 32 * -1)
        )

        self.canvas.create_text(
            785.0,
            111.0,
            anchor="nw",
            text="Width",
            fill="#FFFFFF",
            font=("Calibri Bold", 20 * -1)
        )

        self.canvas.create_text(
            785.0,
            330.0,
            anchor="nw",
            text="Width",
            fill="#FFFFFF",
            font=("Calibri Bold", 20 * -1)
        )

        self.canvas.create_text(
            785.0,
            165.0,
            anchor="nw",
            text="Height",
            fill="#FFFFFF",
            font=("Calibri Bold", 20 * -1)
        )

        self.canvas.create_text(
            785.0,
            391.0,
            anchor="nw",
            text="Height",
            fill="#FFFFFF",
            font=("Calibri Bold", 20 * -1)
        )

        self.canvas.create_text(
            349.0,
            151.0,
            anchor="nw",
            text="or",
            fill="#FFFFFF",
            font=("Calibri Bold", 40 * -1)
        )

        self.canvas.create_text(
            776.0,
            51.0,
            anchor="nw",
            text="Spectrogram",
            fill="#FFFFFF",
            font=("Calibri Bold", 26 * -1)
        )

        self.canvas.create_text(
            790.0,
            281.0,
            anchor="nw",
            text="Waveform",
            fill="#FFFFFF",
            font=("Calibri Bold", 26 * -1)
        )

        self.canvas.create_text(
            798.0,
            563.0,
            anchor="nw",
            text="Visual EQ",
            fill="#FFFFFF",
            font=("Calibri Bold", 26 * -1)
        )

        self.canvas.create_text(
            610.0,
            607.0,
            anchor="nw",
            text="kbps",
            fill="#FFFFFF",
            font=("Calibri Bold", 24 * -1)
        )

        status_text = self.canvas.create_text(
            415.0,
            303.0,
            anchor="nw",
            text=" Not Submitted",
            fill="#fcd303",
            font=("Calibri Bold", 24 * -1)
        )

        self.canvas.create_text(
            215.0,
            686.0,
            anchor="nw",
            text="Refresh",
            fill="#FFFFFF",
            font=("Calibri Bold", 20 * -1)
        )

        self.canvas.create_text(
            215.0,
            710.0,
            anchor="nw",
            text="Graphs",
            fill="#FFFFFF",
            font=("Calibri Bold", 20 * -1)
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
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
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
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
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
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

        entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
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
            file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
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
            file=self.relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
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
            file=self.relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
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
            file=self.relative_to_assets("entry_8.png"))
        entry_bg_8 = self.canvas.create_image(
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

    def on_select_convert(self, event):
        self.selected_convert = self.convert_combobox.get()

    def on_select_download(self, event):
        self.selected_download = self.download_combobox.get()


if __name__ == "__main__":
    window = Tk()
    app = VisAudio(window)
    window.mainloop()
