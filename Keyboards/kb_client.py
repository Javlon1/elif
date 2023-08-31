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


inline_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='оператор(жен)')
        ],
        [
            KeyboardButton(text='стирка(муж)')
        ],
        [
            KeyboardButton(text='доставщик')
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
            KeyboardButton(text='Андижон Шахар'),
            KeyboardButton(text='Андижон Туман'),
        ],
        [
            KeyboardButton(text='Хонабод'),
            KeyboardButton(text='Асака'),
        ],
        [
            KeyboardButton(text='Баликчи'),
            KeyboardButton(text='Бостон'),
        ],
        [
            KeyboardButton(text='Булокбоши'),
            KeyboardButton(text='Жалакудук'),
        ],
        [
            KeyboardButton(text='Избоскан'),
            KeyboardButton(text='Улугнор'),
        ],
        [
            KeyboardButton(text='Олитнкол'),
            KeyboardButton(text='Мархамат'),
        ],
        [
            KeyboardButton(text='Пахтаобод'),
            KeyboardButton(text='Шахрихон'),
        ],
        [
            KeyboardButton(text='Хожабод'),
            KeyboardButton(text='Коргонтепа'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)