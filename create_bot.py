from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = "6389536695:AAHxdxdlHODUGXzopJKTyVm97hoXngHyOA4"
storage = MemoryStorage()

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)