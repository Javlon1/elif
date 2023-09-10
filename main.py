from handlers import admin, client
from create_bot import *
from data__base import sqlite_db

# пишет в терминал
async def on_startup(_):
    print('бот начал работу')
    sqlite_db.sql_start()


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)