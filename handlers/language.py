from aiogram import Router, types
from aiogram.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(Text("🌐 Tilni tanlash"))
async def language_menu(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")]
        ]
    )
    await message.answer("Tilni tanlang:", reply_markup=kb)

@router.callback_query(Text(startswith="lang_"))
async def set_language(callback: types.CallbackQuery):
    lang = callback.data.split("_")[1]
    await callback.answer(f"Til o‘zgartirildi: {lang.upper()}")
    await callback.message.delete()
