from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton


def first_markup():
    first_conv = KeyboardButton('Конвертировать🔄')
    first_course = KeyboardButton('Курс📈')
    first_close = KeyboardButton('Закрыть')
    base_markup = ReplyKeyboardMarkup([[first_conv, first_course], [first_close]], resize_keyboard=True)
    return base_markup


def second_markup():
    second_usd = KeyboardButton('USD → RUB')
    second_eur = KeyboardButton('EUR → RUB')
    second_chf = KeyboardButton('CHF → RUB')
    second_try = KeyboardButton('TRY → RUB')
    second_jpy = KeyboardButton('JPY → RUB')
    second_btc = KeyboardButton('BTC → RUB')
    second_course = ReplyKeyboardMarkup([[second_usd, second_eur, second_chf], [second_try, second_jpy, second_btc],
                                         ['↹', 'Назад']], resize_keyboard=True)
    return second_course


def re_second_markup():
    re_2_usd = KeyboardButton('RUB → USD')
    re_2_eur = KeyboardButton('RUB → EUR')
    re_2_chf = KeyboardButton('RUB → CHF')
    re_2_try = KeyboardButton('RUB → TRY')
    re_2_jpy = KeyboardButton('RUB → JPY')
    re_2_btc = KeyboardButton('RUB → BTC')
    re_2_markup = ReplyKeyboardMarkup([[re_2_usd, re_2_eur, re_2_chf], [re_2_try, re_2_jpy, re_2_btc],
                                       ['↹', 'Назад']], resize_keyboard=True)
    return re_2_markup


def third_markup():
    course_usd = KeyboardButton('USD')
    course_eur = KeyboardButton('EUR')
    course_chf = KeyboardButton('CHF')
    course_try = KeyboardButton('TRY')
    course_jpy = KeyboardButton('JPY')
    course_btc = KeyboardButton('BTC')
    course = ReplyKeyboardMarkup([[course_usd, course_eur, course_chf], [course_try, course_jpy, course_btc],
                                  ['Назад']], resize_keyboard=True)
    return course
