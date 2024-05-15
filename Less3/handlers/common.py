from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import keyboard
from utils.random_fox import fox

router = Router()


@router.message(F.text.lower() == 'старт')
@router.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\nДоступные команды: /start, /stop, /user, /info, /prof, /question\nВы так же можете написать следующие сообщения: привет; как дела; какой сегодня день (в зависимости от рандома выбирает какой сегодня день) и бот ответит\nДоступные фильтры: рандом, старт, юзер, стоп, инфо', reply_markup=keyboard)

# @dp.message(Command(commands=['start']))
@router.message(F.text.lower() == 'рандом')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Привет, твоё число: {number}!')

@router.message(F.text.lower() == 'стоп')
@router.message(Command(commands=['stop']))
async def stop(message: types.Message):
    await message.answer(f'Пока, {message.from_user.full_name}!')
    #print(message)

@router.message(F.text.lower() == 'юзер')
@router.message(Command(commands=['user']))
async def user(message: types.Message):
    await message.answer(f'Информация о вас: имя: {message.from_user.first_name}, фамилия: {message.from_user.last_name}, имя пользователя: @{message.from_user.username}')

#@router.message(F.text.lower() == 'инфо')
@router.message(Command(commands=['info']))
@router.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    await message.answer(f'Информация о боте: имя: Ghost Automaton, имя пользователя: @Elijah_Animus_bot')

@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису')
    await message.answer_photo(img_fox)
    #img_fox = fox()
    #await bot.send_photo(message.from_user.id, img_fox)