from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin_panel12 = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel12.add(KeyboardButton(text='📊Statistika'))
admin_panel12.add(KeyboardButton(text='🚻All Users'))
admin_panel12.add(KeyboardButton(text='📣Reklama'))


reklama_pan = ReplyKeyboardMarkup(resize_keyboard=True)
reklama_pan.add(KeyboardButton(text="💬Matn"))
reklama_pan.add(KeyboardButton(text="📷Rasm + Matn"))
reklama_pan.add(KeyboardButton(text="🎞Video + Matn"))

matn_url = ReplyKeyboardMarkup(resize_keyboard=True)
matn_url.add(KeyboardButton(text="Text no inline url"))
matn_url.add(KeyboardButton(text="Text with inline url"))

rasm_url = ReplyKeyboardMarkup(resize_keyboard=True)
rasm_url.add(KeyboardButton(text="Image no inline url"))
rasm_url.add(KeyboardButton(text="Image with inline url"))

video_url = ReplyKeyboardMarkup(resize_keyboard=True)
video_url.add(KeyboardButton(text="Video no inline url"))
video_url.add(KeyboardButton(text="Video with inline url"))