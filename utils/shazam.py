from aiogram import Router, types
from aiogram.filters import Text
from utils.acrcloud import recognize_acrcloud

router = Router()

@router.message(Text("📱 Shazam"))
async def ask_audio(message: types.Message):
    await message.answer("Audio yoki ovozli xabar yuboring (5-15 soniya).")

@router.message(lambda msg: msg.audio or msg.voice)
async def handle_audio(message: types.Message):
    file = message.audio or message.voice
    file_path = await message.bot.get_file(file.file_id)
    file_url = f"https://api.telegram.org/file/bot{message.bot.token}/{file_path.file_path}"

    # Yuklab olish
    audio = await message.bot.download_file(file_path.file_path)
    with open("temp.mp3", "wb") as f:
        f.write(audio.read())

    result = recognize_acrcloud("temp.mp3")
    if result.get("status", {}).get("msg") == "Success":
        metadata = result["metadata"]["music"][0]
        title = metadata.get("title", "Noma'lum")
        artist = metadata.get("artists", [{}])[0].get("name", "Noma'lum")
        await message.answer(f"<b>{title}</b> - {artist}")
    else:
        await message.answer("Kechirasiz, musiqa aniqlanmadi.")
