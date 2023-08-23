from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_load = KeyboardButton('/menu')
btn_delete = KeyboardButton('/delete')


kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_admin.add(btn_load).add(btn_delete)