import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers import search, shazam, download, language

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Bot va Dispatcher obyektlari
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# /start komandasi uchun handler
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎵 Qo‘shiq qidirish"), KeyboardButton(text="📱 Shazam")],
            [KeyboardButton(text="🔗 Linkdan yuklab olish"), KeyboardButton(text="🌐 Tilni tanlash")]
        ],
        resize_keyboard=True
    )
    await message.answer("Assalomu alaykum! Men musiqa botiman. Xizmatlardan birini tanlang:", reply_markup=kb)

# Routerlarni ulash
dp.include_router(search.router)
dp.include_router(shazam.router)
dp.include_router(download.router)
dp.include_router(language.router)

# Botni ishga tushirish
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
