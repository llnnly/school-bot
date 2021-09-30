from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btnToKnow = InlineKeyboardButton('✔ узнать предпочтительный колледж', callback_data='btnToKnow')
btnPelmeni = InlineKeyboardButton('Пельмени', callback_data='btnPelmeni')
main_btns = InlineKeyboardMarkup().add(btnToKnow, btnPelmeni)
