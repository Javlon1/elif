import sqlite3 as sq
from create_bot import *


def sql_start():
    global base, cur
    base = sq.connect('worker.db')
    cur = base.cursor()
    if base:
        print('data base connected')
    cur.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, fullname TEXT, dataofbir TEXT, bolim TEXT, num1 TEXT, num2 TEXT, address TEXT, job TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for i in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, i[3],f'\n\n<em><b>Имя,фамилия: </b> {i[1]}\n\n <b>год рождения: </b> {i[2]}\n\n <b>номер телефона: </b> {i[4]}\n\n <b>дополнительны номер телефона: </b> {i[5]}\n\n <b>кем хочет работать: </b> {i[0]}\n\n <b>адресс: </b> {i[6]}\n\n <b>кем раньше работал: </b> {i[7]}\n\n <b>сколько хочет зарабатывать: </b> {i[8]}\n</em>', parse_mode="HTML")
     