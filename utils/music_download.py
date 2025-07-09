import yt_dlp

async def download_from_link(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloaded.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return "downloaded.mp3"
