from aiogram import Router, types
from aiogram.filters import Text
from utils.music_search import search_song

router = Router()

@router.message(Text("🎵 Qo‘shiq qidirish"))
async def ask_song_name(message: types.Message):
    await message.answer("Qo‘shiq nomi, ijrochisi yoki matnini yuboring:")

@router.message()
async def search_handler(message: types.Message):
    if message.text:
        result = await search_song(message.text)
        if result:
            await message.answer_audio(
                audio=result["audio_url"],
                title=result["title"],
                performer=result["artist"],
                thumb=result.get("cover_url")
            )
        else:
            await message.answer("Kechirasiz, qo‘shiq topilmadi.")
