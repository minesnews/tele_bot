from aiogram import types


button1 = types.KeyboardButton(text='Старт')
button2 = types.KeyboardButton(text='Стоп')
button3 = types.KeyboardButton(text='Инфо')
button4 = types.KeyboardButton(text='/question')
button5 = types.KeyboardButton(text='Рандом')
button6 = types.KeyboardButton(text='Покажи лису')
button7 = types.KeyboardButton(text='/prof')


keyboard1 = [
    [button1, button7, button3],
    [button4, button5, button6]
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
#keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#keyboard.add(button1, button2, button3)