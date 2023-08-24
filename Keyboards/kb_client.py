from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# btn1 = KeyboardButton('/help')
# btn2 = KeyboardButton('/address')
btn_contact = KeyboardButton('поделиться номером', request_contact=True)
btn_address = KeyboardButton('отправить где я', request_location=True)


year_btn1 = KeyboardButton(1999)
year_btn2 = KeyboardButton(1999)
year_btn3 = KeyboardButton(1999)
year_btn4 = KeyboardButton(1999)
year_btn5 = KeyboardButton(1999)
year_btn6 = KeyboardButton(1999)


address_btn1 = KeyboardButton(text='андижон1')
address_btn2 = KeyboardButton(text='андижон2')
address_btn3 = KeyboardButton(text='андижон3')
address_btn4 = KeyboardButton(text='андижон4')
address_btn5 = KeyboardButton(text='андижон5')
address_btn6 = KeyboardButton(text='андижон6')
address_btn7 = KeyboardButton(text='андижон7')
address_btn8 = KeyboardButton(text='андижон8')
address_btn9 = KeyboardButton(text='андижон9')
address_btn10 = KeyboardButton(text='андижон10')


inkb1 = KeyboardButton(text='оператор(жен)')
inkb2 = KeyboardButton(text='стирка(муж)')
inkb3 = KeyboardButton(text='доставщик')


inline_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
inline_kb.add(inkb1).add(inkb2).add(inkb3)


year_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
year_kb.row(year_btn1,year_btn2).row(year_btn3,year_btn4).row(year_btn5,year_btn6)


contact_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
contact_kb.add(btn_contact)


address_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
address_kb.row(address_btn1,address_btn2).row(address_btn3,address_btn4).row(address_btn5,address_btn6).row(address_btn7,address_btn8).row(address_btn9,address_btn10)

#row, add, insert