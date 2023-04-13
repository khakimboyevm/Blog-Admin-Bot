import pyfiglet
from aiogram import types
# from keyboards.default.test1 import *
from loader import dp

@dp.message_handler(text = "Create Word")
async def create_libs(message: types.Message):
    await message.answer("Istalgan So'xni yozib yuboring.")
    if len(message.text) > 100:
        await message.answer("Juda katta matn!!!")
    else:
        test = message.text
        font = pyfiglet.Figlet()
        result = font.renderText(test)
        await message.answer(result)