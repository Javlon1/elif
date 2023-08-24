from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import *
from aiogram import types
from Keyboards.kb_client import inline_kb, year_kb, address_kb,address_kb
from data__base import sqlite_db
from aiogram.dispatcher.filters import Text


COMMAND_START = "<em>Добро пожаловать \n\nкем ты хочешь работаь у нас </em>"


COMMAND_HELP = """
    <em><b> вас приветствует ALLADIN чем мы вам можем помочь
    /start - начать работу с ботом
    /help - список команд </b></em>
"""


ADDRESS = """
    <em>наш адресс вфвйцвйцвй йривцйвцй вйц воцйпв нцйпвйцвпйцн </em>
"""


LINK_BOT = "https://t.me/ElifAdminBot"


class FSMAdmin(StatesGroup):
    bolim = State()
    fullname = State()
    dataofbir = State()
    photo = State()
    num1 = State()
    num2 = State()
    address = State()
    job = State()
    price = State()


async def command_start(message: types.Message):
    await message.answer(f"{message.from_user.first_name}, {COMMAND_START}", parse_mode="HTML", reply_markup=inline_kb)
    await FSMAdmin.bolim.set()
    await message.delete()


# async def command_help(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id, text=COMMAND_HELP, parse_mode="HTML")
#     await message.delete()


# async def command_address(message: types.Message):
#     await message.reply(text=ADDRESS, parse_mode="HTML")


async def load_bolim(message: types.Message, state: FSMContext):
    if message.text == "оператор(жен)":
        async with state.proxy() as data:
            data['bolim'] = "оператор"
        await FSMAdmin.next()
        await message.answer('имя фамилия: ')
    elif message.text == "стирка(муж)":
        async with state.proxy() as data:
            data['bolim'] = "стирка"
        await FSMAdmin.next()
        await message.answer('имя фамилия: ')
    else:
        async with state.proxy() as data:
            data['bolim'] = message.text
        await FSMAdmin.next()
        await message.answer('имя фамилия: ')


# выход из состоянии
# @dp.message_handler(state="*",commands="отмена")
# @dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("ok")


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text
    await message.answer('имя принято ✅',reply_markup=year_kb)
    await FSMAdmin.next()
    await message.answer('когда ты родился? \nнапример: 1999')


# @dp.message_handler(state=FSMAdmin.name)
async def load_dataofbir(message: types.Message, state: FSMContext):
    mes = (message.text)
    if (mes).isdigit():
        if len(mes) == 4:
            async with state.proxy() as data:
                data['dataofbir'] = message.text
            await message.answer('год рождения принято ✅')
            await FSMAdmin.next()
            await message.answer('отправь фото')
        else:
            await message.answer('не существует такого года рождения')
    else:
        await message.answer('не пиши буквы')


# @dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await message.answer('фото принято ✅')
    await FSMAdmin.next()
    await message.answer('отправь номер телефона')


async def load_num1(message: types.Message, state: FSMContext):
    mes = (message.text)
    if (mes).isdigit():
        if len(mes) == 9:
            async with state.proxy() as data:
                data['num1'] = message.text
            await message.answer('номер принято ✅')
            await FSMAdmin.next()
            await message.answer('отправь ещё раз номер телефона')
        else:
            await message.answer('пиши номер в таком ввиде: 905251243')
    else:
        await message.answer('не пиши буквы')


async def load_num2(message: types.Message, state: FSMContext):
    mes = (message.text)
    if (mes).isdigit():
        if len(mes) == 9:
            async with state.proxy() as data:
                data['num2'] = message.text
            await message.answer('второй номер принято ✅')
            await FSMAdmin.next()
            await message.answer('где ты живешь',reply_markup=address_kb)
        else:
            await message.answer('пиши номер в таком ввиде: 905251243')
    else:
        await message.answer('не пиши буквы')


async def load_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer('адрес принято ✅')
    await FSMAdmin.next()
    await message.answer('где ты раньше работал')


async def load_job(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job'] = message.text
    await message.answer('принято ✅')
    await FSMAdmin.next()
    await message.answer('сколько хочешь получить в месяц\nнапример: 100-$')


# ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.name)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = (message.text)

    await sqlite_db.sql_add_command(state)
    await state.finish()
    await message.answer('Заявка принято')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state=None)
    # dp.register_message_handler(command_help, commands=['help'])
    # dp.register_message_handler(command_address, commands=['address'])
    dp.register_message_handler(cancel_handler, state="*", commands="отмена")
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(load_bolim, state=FSMAdmin.bolim)
    dp.register_message_handler(load_name, state=FSMAdmin.fullname)
    dp.register_message_handler(load_dataofbir, state=FSMAdmin.dataofbir)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_num1, state=FSMAdmin.num1)
    dp.register_message_handler(load_num2, state=FSMAdmin.num2)
    dp.register_message_handler(load_address, state=FSMAdmin.address)
    dp.register_message_handler(load_job, state=FSMAdmin.job)
    dp.register_message_handler(load_price, state=FSMAdmin.price)