import logging
from aiogram import executor
from create_delivery_bot import dp
from functional import actions



logging.basicConfig(level=logging.INFO)


actions.register_message_handler(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)