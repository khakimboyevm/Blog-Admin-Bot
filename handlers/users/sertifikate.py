from aiogram import types
from keyboards.inline.certificate import *
from PIL import Image, ImageFont, ImageDraw
import random
import os
from loader import dp
from states.main import peggy_state
from aiogram.dispatcher import FSMContext
from filters import IsPrivate

@dp.message_handler(IsPrivate(), commands=["take_certificate"], state="*")
async def choosegame(message: types.Message):
    await message.answer("O'zingizni qaysi o'yinda zo'rman deb bilasiz. Tanlag!", reply_markup=Gameni_tanlash)
    await peggy_state.sertificate.set()
@dp.callback_query_handler(text="cs-go", state=peggy_state.sertificate)
async def preperexam(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Sertifikat olishingiz uchun siz testda o'tishingiz kerak. Testga Tayyormisiz!", reply_markup=Tayyorgarlik)
    await peggy_state.test.set()

# -------------------CS-GO---------------------------- #

resultscs = []

# 1

@dp.callback_query_handler(text="tayyorman", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.message.edit_text("Unda Boshlaymiz😉\n\n1.M4A4 dan AK-47 ustunligi nimada?", reply_markup=cs1)

@dp.callback_query_handler(text="AK-47_oq_don", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="AK-47_rejim", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="AK-47_zarar", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("2.O'yin paytida AWP qurolini olish qancha turadi?", reply_markup=cs2)

# 2

@dp.callback_query_handler(text="4750$", state=peggy_state.test)
async def cs_exam2(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("3.O'yin paytida Desert Eagle qurolini olish qancha turadi?", reply_markup=cs3)

@dp.callback_query_handler(text="4450$", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="4900$", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 3

@dp.callback_query_handler(text="700$", state=peggy_state.test)
async def cs_exam3(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("4.AK-47 zirhsiz boshga qancha zarar yetkazadi?", reply_markup=cs4)

@dp.callback_query_handler(text="600$", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="750$", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 4

@dp.callback_query_handler(text="143", state=peggy_state.test)
async def cs_exam4(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("5.Bir round o'yin qancha davom etadi?", reply_markup=cs5)

@dp.callback_query_handler(text="84", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="107", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 5

@dp.callback_query_handler(text="1m 45s", state=peggy_state.test)
async def cs_exam5(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("6.Molotov necha soniya yonadi?", reply_markup=cs6)

@dp.callback_query_handler(text="1m 35s", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="1m 55s", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 6

@dp.callback_query_handler(text="9.6s", state=peggy_state.test)
async def cs_exam6(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("7.Bayter kim?", reply_markup=cs7)

@dp.callback_query_handler(text="4.7s", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="12.5s", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 7

@dp.callback_query_handler(text="O'lja", state=peggy_state.test)
async def cs_exam7(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("8.Terrorchilarga qarshi qanday qurollar mavjud emas?", reply_markup=cs8)

@dp.callback_query_handler(text="Dim_bayter", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="Bomba_qoyuvchi", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 8

@dp.callback_query_handler(text="USP-S", state=peggy_state.test)
async def cs_exam8(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("9.Pichoq bilan o'ldirganingiz uchun qancha pul olasiz?", reply_markup=cs9)

@dp.callback_query_handler(text="AK_mavjud", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="GALIL_AR", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 9

@dp.callback_query_handler(text="1500-$", state=peggy_state.test)
async def cs_exam9(call: types.CallbackQuery):
    await call.answer("To'g'ri!")
    await call.message.edit_text("10.AK-47 qancha turadi?", reply_markup=cs10)

@dp.callback_query_handler(text="1000-$", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="2000-$", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

# 10

@dp.callback_query_handler(text="3100", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="2900$", state=peggy_state.test)
async def agree_exam(call: types.CallbackQuery):
    await call.answer("Xato! Qaytadan urinib ko'ring")

@dp.callback_query_handler(text="2700$", state=peggy_state.test)
async def cs_exam10(call: types.CallbackQuery):
    await call.message.edit_text("Ism Familya yozing.\n\nImloviy xatolarga yo'l qo'ymang")
    await peggy_state.write_to_ser.set()

@dp.message_handler(state=peggy_state.write_to_ser)
async def ism_familya(message: types.Message, state: FSMContext):
    if len(message.text) > 20:
        await message.answer("Sizning ismingiz 20 ta belgidan ko'p.\nIltimos qisqartrib yozishga harakat qiling")
    elif len(message.text) < 15:
        await message.answer("Sizning ismingiz 15 ta belgidan kam.\nIltimos to'liq yozing.")
    else:
        my_image = Image.open("D:/Asosiy/Blog-Admin-Bot/images/CS-GO.jpg")
        title_font = ImageFont.truetype("D:/Asosiy/Blog-Admin-Bot/images/Fonts/Alkatra-VariableFont_wght.ttf", 55)

        title_font1 = ImageFont.truetype("D:/Asosiy/Blog-Admin-Bot/images/Fonts/Alkatra-VariableFont_wght.ttf", 30)
        title_text = message.text
        num_cs = random.randint(75, 90)
        num_cs_str = str(num_cs)
        title_text1 = num_cs_str
        image_editable = ImageDraw.Draw(my_image)
        image_editable1 = ImageDraw.Draw(my_image)
        image_editable.text((530,300), title_text + "ga", (175, 0, 0), font=title_font)
        image_editable1.text((900, 475), title_text1 + " %", (175, 0, 0), font=title_font1)
        telegram_id=message.from_user.id,
        my_image.save(f"{telegram_id}.jpg")
        with open(f"D:/Asosiy/Blog-Admin-Bot/{telegram_id}.jpg", "rb") as cs_photo:
            await message.answer_photo(photo=cs_photo)
            os.remove(f"D:/Asosiy/Blog-Admin-Bot/{telegram_id}.jpg")
            await state.finish()