from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '1793598789:AAHQEG5sCcnMbN3m9nzdQ_twMQFgaqNwcTo'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

if __name__ == '__main__':
    from test_handlers import dp
    from China_test_handlers import dp
    executor.start_polling(dp, skip_updates=True)