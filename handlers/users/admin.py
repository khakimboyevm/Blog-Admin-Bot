import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.default.admin_pan import *
from states.main import peggy_state, Admin
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from filters import IsPrivate
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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

@dp.message_handler(text="💬Matn", user_id=ADMINS, state=Admin.reklama)
async def reklam_type_text(message: types.Message):
    await message.answer("Reklama turini tanlang", reply_markup=matn_url)
    await Admin.choose_text.set()

@dp.message_handler(text="Text no inline url", user_id=ADMINS, state=Admin.choose_text)
async def reklam_type_matn(message: types.Message):
    await message.answer("‼️ Tarqatmoqchi bo'lgan matnni yuboring. E'tiborli bo'ling yuborgan matningizni o'chirib bo'lmaydi")
    await Admin.reklam_matn.set()

@dp.message_handler(user_id=ADMINS, state=Admin.reklam_matn)
async def sent_matn_reklam(message: types.Message, state: FSMContext):
    ad_matn = message.text
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]   
        await bot.send_message(chat_id=user_id, text=ad_matn)
        await asyncio.sleep(0.05)

    await bot.send_message(chat_id=ADMINS[0], text="Xabar Tarqatildi😊", reply_markup=admin_panel12)
    await Admin.admin_pan.set()

@dp.message_handler(text="Text with inline url", user_id=ADMINS, state=Admin.choose_text)
async def reklam_type_matn_url(message: types.Message):
    await message.answer("‼️ Tugmaga yoziladigan matn yuboring E'tiborli bo'ling yuborilgan matnni o'chirib bo'lmaydi")
    await Admin.matn_btn_text.set()

@dp.message_handler(user_id=ADMINS, state=Admin.matn_btn_text)
async def get_text_btn_text(message: types.Message, state: FSMContext):
    btn_text = message.text
    await state.update_data({
        'btn_text':btn_text
    })
    await message.answer("‼️ Link yuboring E'tiborli bo'ling yuborilgan linkni o'chirib bo'lmaydi")
    await Admin.reklam_matn_url.set()

@dp.message_handler(user_id=ADMINS, state=Admin.reklam_matn_url)
async def get_link_text(message: types.Message, state: FSMContext):
    link = message.text
    await state.update_data({
        'link':link
    })
    await message.answer("‼️ Tarqatmoqchi bo'lgan matnni yuboring. E'tiborli bo'ling yuborgan matningizni o'chirib bo'lmaydi")
    await Admin.matn_url_text.set()

@dp.message_handler(user_id=ADMINS, state=Admin.matn_url_text)
async def sent_matn_reklam(message: types.Message, state: FSMContext):
    data = await state.get_data()
    matn_btn = InlineKeyboardMarkup(row_width=1)
    matn_btn.add(InlineKeyboardButton(text=f"{data['btn_text']}", url=f"{data['link']}"))
    ad_matn = message.text
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]   
        await bot.send_message(chat_id=user_id, text=ad_matn, reply_markup=matn_btn)
        await asyncio.sleep(0.05)

    await bot.send_message(chat_id=ADMINS[0], text="Xabar Tarqatildi😊", reply_markup=admin_panel12)
    await Admin.admin_pan.set()


@dp.message_handler(text="📷Rasm + Matn", user_id=ADMINS, state=Admin.reklama)
async def reklam_type_image(message: types.Message):
    await message.answer("Reklama turini tanlang", reply_markup=rasm_url)
    await Admin.choose_image.set()

@dp.message_handler(text="Image no inline url", user_id=ADMINS, state=Admin.choose_image)
async def reklam_type_rasm(message: types.Message):
    await message.answer("‼️ Tarqatmoqchi bo'lgan rasm ni yuboring. E'tiborli bo'ling rasmni tagiga matn yozing, yuborgan rasmingiz hoziroq foydalanuvchilarga jo'natiladi.")
    await Admin.reklam_rasm.set()

@dp.message_handler(content_types=["photo"],user_id=ADMINS, state=Admin.reklam_rasm)
async def sent_rasm_reklam(message: types.Message):
    msg_cap = message.caption
    photo = message.photo[-1].file_id
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]
        await bot.send_photo(chat_id=user_id, photo=photo, caption=msg_cap)
        await asyncio.sleep(0.05)

    await bot.send_message(chat_id=ADMINS[0], text="Rasm + Matn tarqatildi😊", reply_markup=admin_panel12)
    await Admin.admin_pan.set()

@dp.message_handler(text="Image with inline url", user_id=ADMINS, state=Admin.choose_image)
async def reklam_type_rasm_url(message: types.Message):
    await message.answer("‼️ Tugmaga yoziladigan matn yuboring E'tiborli bo'ling yuborilgan matnni o'chirib bo'lmaydi")
    await Admin.rasm_btn_text.set()

@dp.message_handler(user_id=ADMINS, state=Admin.rasm_btn_text)
async def get_image_btn_text(message: types.Message, state: FSMContext):
    image_btn_text = message.text
    await state.update_data({
        'image_btn_text':image_btn_text
    })
    await message.answer("‼️ Link yuboring E'tiborli bo'ling yuborilgan linkni o'chirib bo'lmaydi")
    await Admin.reklam_rasm_url.set()

@dp.message_handler(user_id=ADMINS, state=Admin.reklam_rasm_url)
async def get_link_image_text(message: types.Message, state: FSMContext):
    image_link = message.text
    await state.update_data({
        'image_link':image_link
    })
    await message.answer("‼️ Tarqatmoqchi bo'lgan rasm va matnni yuboring. E'tiborli bo'ling yuborgan rasm va matningizni o'chirib bo'lmaydi")
    await Admin.rasm_url_text.set()

@dp.message_handler(content_types=['photo'], user_id=ADMINS, state=Admin.rasm_url_text)
async def sent_rasm_url_reklam(message: types.Message, state: FSMContext):
    data = await state.get_data()
    rasm_btn = InlineKeyboardMarkup(row_width=1)
    rasm_btn.add(InlineKeyboardButton(text=f"{data['image_btn_text']}", url=f"{data['image_link']}"))
    msg_cap = message.caption
    image = message.photo[-1].file_id
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]   
        await bot.send_photo(chat_id=user_id, photo=image, caption=msg_cap, reply_markup=rasm_btn)
        await asyncio.sleep(0.05)

    await bot.send_message(chat_id=ADMINS[0], text="Xabar Tarqatildi😊", reply_markup=admin_panel12)
    await Admin.admin_pan.set()


@dp.message_handler(text="🎞Video + Matn", user_id=ADMINS, state=Admin.reklama)
async def reklam_type_video(message: types.Message):
    await message.answer("Reklama turini tanlang", reply_markup=video_url)
    await Admin.choose_video.set()

@dp.message_handler(text="Video no inline url", user_id=ADMINS, state=Admin.choose_video)
async def reklam_type_rasm(message: types.Message):
    await message.answer("‼️ Tarqatmoqchi bo'lgan video ni yuboring. E'tiborli bo'ling rasmni tagiga matn yozing, yuborgan rasmingiz hoziroq foydalanuvchilarga jo'natiladi.")
    await Admin.reklam_video.set()

@dp.message_handler(content_types=["video"],user_id=ADMINS, state=Admin.reklam_video)
async def sent_video_reklam(message: types.Message):
    msg_cap = message.caption
    video = message.video.file_id
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]
        await bot.send_video(chat_id=user_id, video=video, caption=msg_cap)
        await asyncio.sleep(0.05)

    await bot.send_message(chat_id=ADMINS[0], text="Vidoe + Matn tarqatildi😊", reply_markup=admin_panel12)
    await Admin.admin_pan.set()

@dp.message_handler(text="Video with inline url", user_id=ADMINS, state=Admin.choose_video)
async def reklam_type_video_url(message: types.Message):
    await message.answer("‼️ Tugmaga yoziladigan matn yuboring E'tiborli bo'ling yuborilgan matnni o'chirib bo'lmaydi")
    await Admin.video_btn_text.set()

@dp.message_handler(user_id=ADMINS, state=Admin.video_btn_text)
async def get_video_btn_text(message: types.Message, state: FSMContext):
    video_btn_text = message.text
    await state.update_data({
        'video_btn_text':video_btn_text
    })
    await message.answer("‼️ Link yuboring E'tiborli bo'ling yuborilgan linkni o'chirib bo'lmaydi")
    await Admin.reklam_video_url.set()

@dp.message_handler(user_id=ADMINS, state=Admin.reklam_video_url)
async def get_link_video_text(message: types.Message, state: FSMContext):
    video_link = message.text
    await state.update_data({
        'video_link':video_link
    })
    await message.answer("‼️ Tarqatmoqchi bo'lgan video va matnni yuboring. E'tiborli bo'ling yuborgan video va matningizni o'chirib bo'lmaydi")
    await Admin.video_url_text.set()
    
@dp.message_handler(content_types=["video"],user_id=ADMINS, state=Admin.video_url_text)
async def sent_video_url_reklam(message: types.Message, state: FSMContext):
    data = await state.get_data()
    video_btn = InlineKeyboardMarkup(row_width=1)
    video_btn.add(InlineKeyboardButton(text=f"{data['video_btn_text']}", url=f"{data['video_link']}"))
    msg_cap = message.caption
    video = message.video.file_id
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]
        await bot.send_video(chat_id=user_id, video=video, caption=msg_cap, reply_markup=video_btn)
        await asyncio.sleep(0.05)

    await bot.send_message(chat_id=ADMINS[0], text="Vidoe + Matn tarqatildi😊", reply_markup=admin_panel12)
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
