import os.path
from pydub import AudioSegment
import pytube

def view_youtube_audio(url: str):
    yt = pytube.YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    downloaded_file = audio_stream.download(output_path='../../temp')
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.wav'
    AudioSegment.from_file(downloaded_file).export(new_file, format='wav')


view_youtube_audio('https://youtu.be/AGCuED8nWug?si=w5SFaMyp0HifcLsY')