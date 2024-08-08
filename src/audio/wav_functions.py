import mimetypes
import os.path

import librosa
import librosa.feature
from matplotlib import  pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from pathlib import Path
from pydub import AudioSegment
import mimetypes


def generate_visual_spectrogram(file_path):
    plt.figure(figsize=(6, 2.51))
    signal, sr = librosa.load(file_path)
    mel_spec = librosa.power_to_db(np.abs(librosa.stft(y=signal, n_fft=2048, hop_length=512)))
    librosa.display.specshow(mel_spec, fmax=8000,cmap='magma')
    plt.savefig('../../temp/spectrogram.png', bbox_inches='tight', pad_inches=0)


def load_spectrogram():
    with Image.open('../../temp/spectrogram.png') as img:
        photo = ImageTk.PhotoImage(img)
        return photo

def generate_visual_waveform(file_path):
    plt.figure(figsize=(6, 2.51))
    signal, sr = librosa.load(file_path)
    librosa.display.waveshow(y=signal, sr=sr)
    plt.axis('off')
    plt.savefig('../../temp/waveform.png', bbox_inches='tight', pad_inches=0)


def load_waveform():
    with Image.open('../../temp/waveform.png') as img:
        photo = ImageTk.PhotoImage(img)
        return photo


def generate_download_spectrogram(width, height, file_path, download_path):
    plt.figure(figsize=(float(width), float(height)))
    signal, sr = librosa.load(file_path)
    mel_spec = librosa.power_to_db(np.abs(librosa.stft(y=signal, n_fft=2048, hop_length=512)))
    librosa.display.specshow(mel_spec, fmax=8000, x_axis='time', y_axis='mel', cmap='magma')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f"{os.path.basename(file_path)}")
    plt.savefig(os.path.join(download_path, f"{Path(file_path).stem}_spec{width}x{height}.png"), bbox_inches='tight', pad_inches=0)


def generate_download_waveform(width, height, file_path, download_path):
    plt.figure(figsize=(float(width), float(height)))
    signal, sr = librosa.load(file_path)
    librosa.display.waveshow(y=signal, sr=sr, axis='time')
    plt.title(f"{os.path.basename(file_path)}")
    plt.savefig(os.path.join(download_path, f"{Path(file_path).stem}_waveform{width}x{height}.png"), bbox_inches='tight', pad_inches=0)


def get_audio_info(file_path):
    audio = AudioSegment.from_file(file_path)
    bitrate_bps = audio.frame_rate * audio.frame_width * 8
    bitrate_kbps = bitrate_bps / 1000
    file_type, _ = mimetypes.guess_type(file_path)
    return bitrate_kbps, file_type

def convert(file_path, convert_type):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist")

        file_name, file_extension = os.path.splitext(os.path.basename(file_path))
        dir = os.path.dirname(file_path)

        audio = AudioSegment.from_file(file_path)

        output_file_path = os.path.join(dir, f"{file_name}.{convert_type}")
        audio.export(output_file_path, format=convert_type)
        return output_file_path
    except FileNotFoundError as ex:
        print(f"Error: {ex}")
    except Exception as ex:
        print(f"Error: {ex}")