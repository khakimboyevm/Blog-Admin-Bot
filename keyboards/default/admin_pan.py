from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# admin_panel = ReplyKeyboardMarkup(
#     [
#         [KeyboardButton(text='📊Statistika')],
#         [KeyboardButton(text='🚻All Users')],
#         [KeyboardButton(text='📣Reklama')]
#     ], resize_keyboard=True
# )

admin_panel12 = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel12.add(KeyboardButton(text='📊Statistika'))
admin_panel12.add(KeyboardButton(text='🚻All Users'))
admin_panel12.add(KeyboardButton(text='📣Reklama'))


reklama_pan = ReplyKeyboardMarkup(resize_keyboard=True)
reklama_pan.add(KeyboardButton(text="Matn"))
reklama_pan.add(KeyboardButton(text="Rasm + Man"))