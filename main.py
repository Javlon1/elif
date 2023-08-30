from handlers import admin, client, other
from create_bot import *
from data__base import sqlite_db

# пишет в терминал


async def on_startup(_):
    print('бот начал работу')
    sqlite_db.sql_start()


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
# other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

