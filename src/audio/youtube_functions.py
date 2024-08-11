import os
import yt_dlp as ytdlp
import sys

def view_youtube_audio(url: str) -> str:
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '../../temp/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
                'preferredquality': '192',
            }],
            'prefer_ffmpeg': True,
            'keepvideo': False
        }

        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            if title:
                flac_file = os.path.join('../../temp', f"{title}.flac")
                return flac_file

        return None

    except Exception as ex:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(f"Error: {exc_type}, File: {fname}, Line: {exc_tb.tb_lineno}")
        return None
