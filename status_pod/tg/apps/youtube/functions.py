from __future__ import unicode_literals
import youtube_dl


def get_audio_by_url_from_youtube(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'nocheckcertificate': True,
        'postprocessors': [{
            # 'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     return ydl.download([url])
