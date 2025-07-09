from aiogram import Router, types
from aiogram.filters import Text
from utils.music_download import download_from_link

router = Router()

@router.message(Text("🔗 Linkdan yuklab olish"))
async def ask_link(message: types.Message):
    await message.answer("TikTok yoki Instagram videosi linkini yuboring:")

@router.message()
async def download_handler(message: types.Message):
    if "tiktok.com" in message.text or "instagram.com" in message.text:
        audio_path = await download_from_link(message.text)
        if audio_path:
            await message.answer_audio(audio=open(audio_path, "rb"))
        else:
            await message.answer("Musiqa ajratib bo‘lmadi.")
