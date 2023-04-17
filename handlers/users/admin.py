import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.default.admin_pan import admin_panel12, reklama_pan
from states.main import peggy_state, Admin
from aiogram.dispatcher import FSMContext
from filters import IsPrivate

@dp.message_handler(IsPrivate(), text="/admin", user_id=ADMINS, state="*")
async def admin_panel(message: types.Message):
    await message.answer("Admin panelga xush kelibsiz", reply_markup=admin_panel12)
    await Admin.admin_pan.set()

@dp.message_handler(text="🚻All Users", user_id=ADMINS, state=Admin.admin_pan)
async def get_all_users(message: types.Message, state: FSMContext):
    users = await db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[-1])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
            await state.finish()
    else:
       await bot.send_message(message.chat.id, df)
       
@dp.message_handler(text="📣Reklama", user_id=ADMINS, state=Admin.admin_pan)
async def reklam_type(message: types.Message):
    await message.answer("Reklama turini tanlang", reply_markup=reklama_pan)
    await Admin.reklama.set()

@dp.message_handler(text="Matn", user_id=ADMINS, state=Admin.reklama)
async def reklam_type_matn(message: types.Message):
    await message.answer("Tarqatmoqchi bo'lgan matnni yuboring. E'tiborli bo'ling yuborgan matningizni o'chirib bo'lmaydi")
    await Admin.reklam_matn.set()

@dp.message_handler(user_id=ADMINS, state=Admin.reklam_matn)
async def sent_matn_reklam(message: types.Message, state: FSMContext):
    ad_matn = message.text
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]   
        await bot.send_message(chat_id=user_id, text=ad_matn)
        await asyncio.sleep(0.05)
    await bot.send_message(chat_id=ADMINS[0], text="Xabar Tarqatildi")
    await Admin.admin_pan.set()

@dp.message_handler(text="Rasm + Man", user_id=ADMINS, state=Admin.reklama)
async def reklam_type_rasm(message: types.Message):
    await message.answer("Tarqatmoqchii bo'lgan rasm ni yuboring. E;tiborli bo'ling rasmni tagiga matn yozing, yuborgan rasmingiz hoziroq foydalanuvchilarga jo'natiladi.")
    await Admin.reklam_rasm.set()

@dp.message_handler(content_types=["photo"],user_id=ADMINS, state=Admin.reklam_rasm)
async def sent_rasm_reklam(message: types.Message):
    msg_cap = message.caption
    photo = message.photo[-1].file_id
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_photo(chat_id=user_id, photo=photo, caption=msg_cap)
        await asyncio.sleep(0.05)

    await bot.send_message(chat_id=ADMINS[0], text="Rasm + Matn tarqatildi")
    await Admin.admin_pan.set()

@dp.message_handler(text="📊Statistika", user_id=ADMINS, state=Admin.admin_pan)
async def get_statis(message: types.Message, state: FSMContext):
    count = await db.count_users()
    await message.answer(f"Bazada <b>{count}</b> ta foydalanuvchi bor.")
    await Admin.admin_pan.set()

@dp.message_handler(IsPrivate(), text="/cleandb", user_id=ADMINS, state="*")
async def get_all_users(message: types.Message):
    await db.delete_users()
    await message.answer("Baza tozalandi!")
