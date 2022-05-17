from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor

API_TOKEN = ''

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 