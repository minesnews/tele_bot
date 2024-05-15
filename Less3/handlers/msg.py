from aiogram import Router, types, F
import random

router = Router()

@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif 'какой сегодня день' in message.text.lower():
        rand = random.randint(0, 2)
        day = ''
        if rand == 0:
            day = 'хороший'
        elif rand == 1:
            day = 'отличный'
        else:
            day = 'превосходный'
        await message.reply(f'Сегодня {day} день! (рандом= {rand})')
    else:
        await message.reply('Не понимаю тебя...')