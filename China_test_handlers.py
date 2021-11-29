from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

from main import bot

from main_handlers import dp
from states import China_test

questions = {
    'start': 'Вы начали тест',
    'q1': ['Является ли Тайвань государством? (да/нет)', ['да', 'нет'], 'assets/taiwan.jpg'],
    'q2': ['Что произошло на главной площади Тяньаньмэнь в 1989 году??? (ничего/ничего)', ['ничего', 'ничего'], 'assets/square.jpg'],
    'q3': ['У вас больше одного ребенка в семье?? (да/нет)', ['да', 'нет'], 'assets/demography.jpg'],
    'good_final': 'ура русский Иван город пермь правильно ответил на все вопрос о нефритовый стержень великий China',
    'bad_final': 'вы разочаровать партия Китай и мудрый Xi вы раб бургер грязная америка'
}


async def minus_credit(msg):
    photo = InputFile("assets/minus.jpg")
    await bot.send_photo(chat_id=msg.chat.id, photo=photo)


async def plus_credit(msg):
    photo = InputFile("assets/plus.jpg")
    await bot.send_photo(chat_id=msg.chat.id, photo=photo)


@dp.callback_query_handler(text="btnChina", state=None)
async def enter_test(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, questions['start'])
    await bot.send_message(callback_query.from_user.id, questions['q1'][0])

    await China_test.Q1.set()


@dp.message_handler(state=China_test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # answer to user
    if answer == questions['q1'][1][0]:
        await minus_credit(message)
        answer = False
    elif answer == questions['q1'][1][1]:
        await plus_credit(message)
        answer = True
    else:
        await minus_credit(message)
        answer = False

    # save answer
    await state.update_data(answer1=answer)

    await message.answer(questions['q2'][0])

    await China_test.next()


@dp.message_handler(state=China_test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text

    # answer to user
    if answer == questions['q2'][1][0]:
        await plus_credit(message)
        answer = True
    elif answer == questions['q2'][1][1]:
        await plus_credit(message)
        answer = True
    else:
        await minus_credit(message)
        answer = False

    # save answer
    await state.update_data(answer2=answer)

    await message.answer(questions['q3'][0])

    await China_test.next()


@dp.message_handler(state=China_test.Q3)
async def answer_q2(message: types.Message, state: FSMContext):
    last_answer = message.text

    # answer to user
    if last_answer == questions['q3'][1][0]:
        await minus_credit(message)
        answer = False
    elif last_answer == questions['q3'][1][1]:
        await plus_credit(message)
        answer = True
    else:
        await minus_credit(message)
        answer = False

    # get answers
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = last_answer

    if (answer1 and answer2 and answer3):
        await message.answer(questions['good_final'])
        photo = InputFile("assets/credits_up.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    else:
        await message.answer(questions['bad_final'])
        photo = InputFile("assets/credits_down.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

        # print(answer1, answer2, answer3)
    await state.finish()