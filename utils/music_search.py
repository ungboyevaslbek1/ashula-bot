import yt_dlp

async def search_song(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch1',
        'quiet': True,
        'extract_flat': False,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if "entries" in info:
            info = info["entries"][0]

        return {
            "title": info.get("title"),
            "artist": info.get("uploader"),
            "audio_url": info.get("url"),
            "cover_url": info.get("thumbnail")
        }
