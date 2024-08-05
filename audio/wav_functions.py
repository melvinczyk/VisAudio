import os.path

import librosa
import librosa.feature
from matplotlib import  pyplot as plt
import numpy as np
from PIL import Image, ImageTk


def generate_visual_spectrogram(file_path):
    plt.figure(figsize=(6, 2.51))
    signal, sr = librosa.load(file_path)
    mel_spec = librosa.power_to_db(np.abs(librosa.stft(y=signal, n_fft=2048, hop_length=512)))
    librosa.display.specshow(mel_spec, fmax=8000,cmap='magma')
    # plt.colorbar(format='%+2.0f dB')
    # plt.title(f"{os.path.basename(file_path)}")
    plt.savefig('../temp/spectrogram.png', bbox_inches='tight', pad_inches=0)


def load_spectrogram():
    with Image.open('../temp/spectrogram.png') as img:
        photo = ImageTk.PhotoImage(img)
        return photo

def generate_visual_waveform(file_path):
    plt.figure(figsize=(6, 2.51))
    signal, sr = librosa.load(file_path)
    librosa.display.waveshow(y=signal, sr=sr)
    plt.axis('off')

    plt.savefig('../temp/waveform.png', bbox_inches='tight', pad_inches=0)


def load_waveform():
    with Image.open('../temp/waveform.png') as img:
        photo = ImageTk.PhotoImage(img)
        return photo