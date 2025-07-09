from aiogram import Router, types
from aiogram.filters import Text
from utils.shazam_helper import recognize_song
import os

router = Router()

@router.message(Text("📱 Shazam"))
async def ask_audio(message: types.Message):
    await message.answer("Iltimos, musiqa eshitiladigan audio fayl yuboring (≤15 soniya).")

@router.message(content_types=types.ContentType.AUDIO | types.ContentType.VOICE)
async def shazam_handler(message: types.Message):
    file = await message.bot.get_file(message.audio.file_id if message.audio else message.voice.file_id)
    file_path = file.file_path
    destination = "shazam_audio.ogg"
    await message.bot.download_file(file_path, destination)

    result = await recognize_song(destination)

    os.remove(destination)

    if result:
        caption = f"🎶 <b>{result['title']}</b>
👤 {result['artist']}"
        await message.answer_photo(result["cover_url"], caption=caption)
    else:
        await message.answer("Kechirasiz, musiqa aniqlanmadi.")
