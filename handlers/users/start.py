from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS 
from keyboards.inline.subscription import check_button
from states.main import *
from filters import IsPrivate


@dp.message_handler(CommandStart(),IsPrivate(),state="*")
async def bot_start(message: types.Message):
    username = message.from_user.username
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    user = await db.select_user(telegram_id=message.from_user.id)
    teshkrish = await check_button(bot)
    if user is None:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        # ADMINGA xabar beramiz
        count = await db.count_users()
        msg = f"Bazada <b>{count}</b> ta foydalanuvchi bor.\n<b>{user[1]}</b> bazaga qo'shildi.\n@{user[2]} - username\n<b>{user[0]}</b> - id"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    # user = await db.select_user(telegram_id=message.from_user.id)
    await bot.send_message(chat_id=ADMINS[0], text=f"<b>{full_name}</b> bazaga oldin qo'shilgan\n@{username} - username\n<b>{user_id}</b> - id")
    await message.answer(f"Xush kelibsiz! {full_name}\nKanallarga obuna bo'ling!", reply_markup=teshkrish)
    await peggy_state.subscribe.set()
# @{user[2]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor.