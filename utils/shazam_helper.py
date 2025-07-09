from shazamio import Shazam

async def recognize_song(file_path: str):
    shazam = Shazam()
    result = await shazam.recognize_song(file_path)

    if result.get("track"):
        track = result["track"]
        return {
            "title": track.get("title"),
            "artist": track.get("subtitle"),
            "cover_url": track["images"].get("coverart"),
            "url": track.get("url")
        }
    return None
