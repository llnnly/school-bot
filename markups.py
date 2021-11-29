from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btnToKnow = InlineKeyboardButton('✔ узнать предпочтительный колледж', callback_data='btnToKnow')
btnPelmeni = InlineKeyboardButton('Пельмени', callback_data='btnPelmeni')
btnChina = InlineKeyboardButton('Пройти тест на ВИЧ', callback_data='btnChina')
main_btns = InlineKeyboardMarkup().add(btnToKnow, btnPelmeni, btnChina)