from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = "6521901813:AAHRjHh29d-k9NW6KLa1WmJmxKZxCOgMY60"
storage = MemoryStorage()

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)