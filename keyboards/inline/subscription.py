from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import CHANNELS

async def check_button(bot):
    teshkrish = InlineKeyboardMarkup(row_width=1)

    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        keyboard = InlineKeyboardButton(text=chat.title, url=invite_link)
        teshkrish.add(keyboard)

    teshkrish.add(InlineKeyboardButton(text="✅Tekshirish", callback_data="tekshirish"))
    return teshkrish