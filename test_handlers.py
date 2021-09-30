from aiogram import types
from aiogram.dispatcher import FSMContext
from main import bot

from main_handlers import dp
from states import Test

questions = {
    'start': 'Вы начали тестирование',
    'q1': 'введите свои любимые школьные предметы',
    'q2': 'введите свои самые не любимые школьные предметы',
    'q3': 'введите сдаваемые вами предметы, если имеются (иначе пробел)',
    'final': 'Спасибо за прохождение опроса. Ваш результат: '
}


@dp.callback_query_handler(text="btnToKnow", state=None)
async def enter_test(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, questions['start'])
    await bot.send_message(callback_query.from_user.id, questions['q1'])

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # save answer
    await state.update_data(answer1=answer)

    await message.answer(questions['q2'])

    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text

    # save answer
    await state.update_data(answer2=answer)

    await message.answer(questions['q3'])

    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q2(message: types.Message, state: FSMContext):
    # get answers
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = message.text

    await message.answer(questions['final'] + 'Славянка!')

    # print(answer1, answer2, answer3)
    await state.finish()
