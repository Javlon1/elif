from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btn1 = KeyboardButton('/help')
btn2 = KeyboardButton('/address')
btn3 = KeyboardButton('/Загрузить')
btn_contact = KeyboardButton('поделиться номером', request_contact=True)
btn_address = KeyboardButton('отправить где я', request_location=True)


inkb1 = KeyboardButton(text='оператор(жен)')
inkb2 = KeyboardButton(text='стирка(муж)')
inkb3 = KeyboardButton(text='доставщик')

inline_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

inline_kb.add(inkb1).add(inkb2).add(inkb3)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


#row, add, insert
kb_client.add(btn1).insert(btn2).row(btn_contact,btn_address).add(btn3)