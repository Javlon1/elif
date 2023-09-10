from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import *
from aiogram import types
from Keyboards.kb_client import inline_kb, year_kb, address_kb, address_kb, court_kb, info_kb, wedding_kb
from data__base import sqlite_db
from aiogram.dispatcher.filters import Text


COMMAND_START = "<em> Ассалому алейкум ELIF Gilam va Mebel Yuvish ботига хуш келибсиз \n\nКим болиб ишламокчисиз </em>"


COMMAND_HELP = """
    <em><b> Ассалому алейкум ELIF Gilam va Mebel Yuvish\n
/start - Ro'yxatdan o'tish
/about - Korxona haqid ma'lumot
</b></em>
"""

ABOUT = """
ELIF Gilam va Mebel Yuvish\n\n... хакида ... \n\nRasmiy kanalimiz - https://t.me/ELIF_GilamYuvish
"""


LINK_BOT = "https://t.me/ElifAdminBot"


class FSMAdmin(StatesGroup):
    bolim = State()
    fullname = State()
    dataofbir = State()
    photo = State()
    num1 = State()
    num2 = State()
    address1 = State()
    address2 = State()
    wedding = State()
    court = State()
    job = State()
    price = State()


async def command_start(message: types.Message):
    await message.answer(f"{message.from_user.first_name}, {COMMAND_START}", parse_mode="HTML", reply_markup=inline_kb)
    await FSMAdmin.bolim.set()
    await message.delete()


async def about(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=ABOUT, parse_mode="HTML")
    await message.delete()


async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=COMMAND_HELP, parse_mode="HTML")
    await message.delete()


# async def command_address(message: types.Message):
#     await message.reply(text=ADDRESS, parse_mode="HTML")


async def load_bolim(message: types.Message, state: FSMContext):
    if message.text == "Operator(Ayol)":
        async with state.proxy() as data:
            data['bolim'] = "Operator"
        await FSMAdmin.next()
        await message.answer('Ism Familiyangiz: ')
    elif message.text == "Yuvish(Erkak)":
        async with state.proxy() as data:
            data['bolim'] = "Yuvish"
        await FSMAdmin.next()
        await message.answer('Ism Familiyangiz: ')
    else:
        async with state.proxy() as data:
            data['bolim'] = message.text
        await FSMAdmin.next()
        await message.answer('Ism Familiyangiz: ')


# выход из состоянии
# @dp.message_handler(state="*",commands="cancel")
# @dp.message_handler(Text(equals="cancel", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Ro`yxatdan o`tish bekor qilindi\n\n", reply_markup=info_kb)


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        matn = message.text
        if matn.split()[0] != matn:
            data['fullname'] = message.text
            await message.answer('Ism Familiyangiz qabul qilindi ✅', reply_markup=year_kb)
            await FSMAdmin.next()
            await message.answer("Tug'ilgan yilingizni yozing \nMisol uchun: 2003")
        else:
            await message.answer('Iltimos Ism va Familiyangizni yozing! \n\nMisol uchun: (Mukhammadjonov Javlon)')


# @dp.message_handler(state=FSMAdmin.name)
async def load_dataofbir(message: types.Message, state: FSMContext):
    mes = (message.text)
    if (mes).isdigit():
        if len(mes) == 4:
            if mes > '1990':
                if mes < '2023':
                    async with state.proxy() as data:
                        data['dataofbir'] = message.text
                    await message.answer("Tug'ilgan yilingizni qabul qilindi ✅")
                    await FSMAdmin.next()
                    await message.answer("O'z suratingizni yuboring")
                else:
                    await message.answer("Tug'ilgan yilingizni to'g'ri yozing.", reply_markup=year_kb)
            else:
                await message.answer("Tug'ilgan yilingizni bizga to'g'ri kelmaydi")
        else:
            await message.answer("Tug'ilgan yilingizni to'g'ri kiriting!\n\nMisol uchun: 2003", reply_markup=year_kb)
    else:
        await message.answer("Tug'ilgan yilingizni to'g'ri yozing.\n(faqat raqam bilan)", reply_markup=year_kb)


# @dp.message_handler(content_types=['any'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):

    mes = (message.text)

    if mes != str(mes):
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await message.answer('Suratingizni qabul qilindi ✅')
        await FSMAdmin.next()
        await message.answer("Telefon raqamingizni kiriting\n\nmasalan: (991179009)")
    else:
        await message.answer('<b>Matn emas, rasmingizni yuboring !</b>', parse_mode="HTML")


async def load_num1(message: types.Message, state: FSMContext):
    mes = (message.text)
    if (mes).isdigit():
        if len(mes) == 9 or len(mes) == 12:
            async with state.proxy() as data:
                data['num1'] = message.text
            await message.answer('Telefon raqamingizni qabul qilindi ✅')
            await FSMAdmin.next()
            await message.answer("📞Siz bilan tez va oson bog'lanish uchun qo'shimcha raqam ham yozib qoldiring!")
        else:
            await message.answer('Telefon raqamingizni shu tarzda yozing:\n\n(998991179009 yoki 991179009)')
    else:
        await message.answer("Telefon raqamingizni to'g'ri yozing.\n(faqat raqam bilan)")


async def load_num2(message: types.Message, state: FSMContext):
    mes = (message.text)
    if (mes).isdigit():
        if len(mes) == 9 or len(mes) == 12:
            async with state.proxy() as data:
                data['num2'] = message.text
            await message.answer("Qo'shimcha raqam qabul qilindi ✅")
            await FSMAdmin.next()
            await message.answer('Qayerdansiz?', reply_markup=address_kb)
        else:
            await message.answer('Telefon raqamingizni shu tarzda yozing:(998991179009 yoki 991179009)')
    else:
        await message.answer("Telefon raqamingizni to'g'ri yozing.\n(faqat raqam bilan)")


async def load_address1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address1'] = message.text
    await message.answer('Yashash manzilingiz qabul qilindi ✅')
    await FSMAdmin.next()
    await message.answer("Manzilingiz (Mahalla nomi, uy raqami...)")


async def load_address2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address2'] = message.text
    await message.answer('Yashash manzilingiz qabul qilindi ✅')
    await FSMAdmin.next()
    await message.answer("Ijtimoiy holatingiz:",reply_markup=wedding_kb)


async def load_wedding(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['wedding'] = message.text
    await message.answer('Ijtimoiy holatingiz qabul qilindi ✅')
    await FSMAdmin.next()
    await message.answer("Sudlanganmisiz?",reply_markup=court_kb)


async def load_court(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['court'] = message.text
    await message.answer('malumot qabul qilindi ✅')
    await FSMAdmin.next()
    await message.answer("Oldingi ish joyingiz?")


async def load_job(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job'] = message.text
    await message.answer('qabul qilindi ✅')
    await FSMAdmin.next()
    await message.answer("Qancha maoshga ishlamoqchisiz?")


# ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.name)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = (message.text)

    await sqlite_db.sql_add_command(state)
    await state.finish()
    await message.answer('Arizangiz qabul qilindi ✅')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state="*")
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(about, commands=['about'])
    # dp.register_message_handler(command_address, commands=['address'])
    dp.register_message_handler(cancel_handler, state="*", commands="cancel")
    dp.register_message_handler(cancel_handler, Text(
        equals="cancel", ignore_case=True), state="*")
    dp.register_message_handler(load_bolim, state=FSMAdmin.bolim)
    dp.register_message_handler(load_name, state=FSMAdmin.fullname)
    dp.register_message_handler(load_dataofbir, state=FSMAdmin.dataofbir)
    dp.register_message_handler(load_photo, content_types=[
                                'any'], state=FSMAdmin.photo)
    dp.register_message_handler(load_num1, state=FSMAdmin.num1)
    dp.register_message_handler(load_num2, state=FSMAdmin.num2)
    dp.register_message_handler(load_address1, state=FSMAdmin.address1)
    dp.register_message_handler(load_address2, state=FSMAdmin.address2)
    dp.register_message_handler(load_wedding, state=FSMAdmin.wedding)
    dp.register_message_handler(load_court, state=FSMAdmin.court)
    dp.register_message_handler(load_job, state=FSMAdmin.job)
    dp.register_message_handler(load_price, state=FSMAdmin.price)