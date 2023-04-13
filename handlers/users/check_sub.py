from loader import dp, bot
from aiogram import types
from data.config import CHANNELS
from utils.misc import subscription
# from keyboards.default.test1 import testt1
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.callback_query_handler(text="tekshirish")
async def checker(call: types.CallbackQuery):
    await call.answer("Loading!")
    result = ""
    final_status = True
    for channel in CHANNELS:
        status = await subscription.chack(user_id=call.from_user.id, channel=channel)
        channel = await bot .get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lmagansiz!\n\n"
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f" <a href='{invite_link}'><b>{channel.title}</b></a> kanallarga obuna bo'lgansiz")
        
    if final_status:
        await call.message.delete()
        await call.message.answer("Siz hozircha faqat menyudagi take_certiciate bo'limidan foydalana olasiz.")
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text="✅Tekshirish", callback_data="tekshirish"))
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=markup)