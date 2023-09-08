from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# row, add, insert

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('/start'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

info_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('/start'),
            KeyboardButton('/help'),
        ],
        [
            KeyboardButton("/about")
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

inline_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Operator(Ayol)')
        ],
        [
            KeyboardButton(text='Yuvish(Erkak)')
        ],
        [
            KeyboardButton(text='Shafyorlik')
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)


year_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(1998),
            KeyboardButton(1999),
        ],
        [
            KeyboardButton(2000),
            KeyboardButton(2001),
        ],
        [
            KeyboardButton(2002),
            KeyboardButton(2003),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)


user_info_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('поделиться номером', request_contact=True),
            KeyboardButton('отправить где я', request_location=True)
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)


address_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Andijon Shaxri'),
            KeyboardButton(text='Andijon Tumani'),
        ],
        [
            KeyboardButton(text='Xonabod'),
            KeyboardButton(text='Asaka'),
        ],
        [
            KeyboardButton(text='Baliqchi'),
            KeyboardButton(text="Bo'ston"),
        ],
        [
            KeyboardButton(text='Buloqboshi'),
            KeyboardButton(text='Jalaquduq'),
        ],
        [
            KeyboardButton(text='Izboskan'),
            KeyboardButton(text="Ulug'nor"),
        ],
        [
            KeyboardButton(text='Oltinkol'),
            KeyboardButton(text='Marhamat'),
        ],
        [
            KeyboardButton(text='Paxtaobod'),
            KeyboardButton(text='Shaxrixon'),
        ],
        [
            KeyboardButton(text="Xo'jaobod"),
            KeyboardButton(text="Qo'rg'ontepa"),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

wedding_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Turmush qurganman"),
            KeyboardButton(text="Turmush qurmaganman"),
        ],
        [
            KeyboardButton(text="Ajrashganman")
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

court_kb =  ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="xa"),
            KeyboardButton(text="yoq"),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)