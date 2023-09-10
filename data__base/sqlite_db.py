import sqlite3 as sq
from create_bot import *


def sql_start():
    global base, cur
    base = sq.connect('worker.db')
    cur = base.cursor()
    if base:
        print('data base connected')
    cur.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, fullname TEXT, dataofbir TEXT, bolim TEXT, num1 TEXT, num2 TEXT, address1 TEXT, address2 TEXT, wedding TEXT, court TEXT, job TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (tuple(data.values())))
        base.commit()


async def sql_read(message):
    j = 0
    for i in cur.execute('SELECT * FROM menu').fetchall():
        j+=1
        await bot.send_photo(message.from_user.id, i[3],f"\n\n<b>id: </b>{j}\n\n<em><b> Ism, Familiya: </b> {i[1]}\n\n <b>Tug'ilgan yili: </b> {i[2]}\n\n <b>Telefon raqami: </b> {i[4]}\n\n <b>Qo'shimcha telefon raqami: </b> {i[5]}\n\n <b>Bo'lim: </b> {i[0]}\n\n <b>Manzili: </b> {i[6]}, {i[7]}\n\n <b>Ijtimoiy holati: </b>{i[8]} \n\n <b>Sudlanganmi: {i[9]}</b> \n\n<b>kim bo'lib ishlagan: </b> {i[10]}\n\n <b>Qancha maoshga ishlamoqchi: </b> {i[11]}\n</em>", parse_mode="HTML")