from aiogram import types
from main import dp, bot
import markups


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer('hello, Gay', reply_markup=markups.main_btns)


@dp.callback_query_handler(text="btnPelmeni")
async def pelmeni(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'https://youtu.be/yD-UlZUUnpk')