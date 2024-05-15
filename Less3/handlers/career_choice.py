from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.career_keyboard import make_keyboard


router = Router()

age_choise = 0

available_jobs = [
    'Программист',
    'Маркетолог',
    'Менеджер',
    'Аналитик',
    'Бухгалтер'
]

available_grades = [
    'Низкий',
    'Средний',
    'Высокий'
]

available_ages = [
    'Молодой',
    'Средний',
    'Пожилой'
]

available_salary =[
    "Низкая",
    "Средняя",
    "Высокая"
]

class Choice(StatesGroup):
    job = State()
    grade = State()
    age = State()
    salary = State()

#################################################################################################################

@router.message(Command(commands=['prof']))
async def start(message: types.Message, state: FSMContext):
    await message.answer(f'Какая профессия вас интересует?', reply_markup=make_keyboard(available_jobs))
    await state.set_state(Choice.job)

@router.message(Choice.job, F.text.in_(available_jobs))
async def jobs(message: types.Message, state: FSMContext):
    await message.answer(f'Как вы оцениваете свою профессию?', reply_markup=make_keyboard(available_grades))
    await state.set_state(Choice.grade)

@router.message(Choice.job)
async def job_incorrectly(message: types.Message):
    await message.answer(f'Неправильно! Попробуй еще раз!', reply_markup=make_keyboard(available_jobs))

@router.message(Choice.grade, F.text.in_(available_grades))
async def grades(message: types.Message, state: FSMContext):
    await message.answer(f'Вы всё прошли, с вами свяжутся! {message.text}', reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(Choice.grade)
async def grade_incorrectly(message: types.Message):
    await message.answer(f'Неправильно! Попробуй еще раз!', reply_markup=make_keyboard(available_grades))
#################################################################################################################

@router.message(Command(commands=['question']))
async def start(message: types.Message, state: FSMContext):
    await message.answer(f'Какой ваш возраст?', reply_markup=make_keyboard(available_ages))
    await state.set_state(Choice.age)

@router.message(Choice.age, F.text.in_(available_ages))
async def ages(message: types.Message, state: FSMContext):
    await message.answer(f'Какой ваш уровень зарплаты?', reply_markup=make_keyboard(available_salary))
    await state.set_state(Choice.salary)
    global age_choise
    age_choise = message.text


@router.message(Choice.age)
async def age_incorrectly(message: types.Message):
    await message.answer(f'Неправильно! Попробуй еще раз!', reply_markup=make_keyboard(available_ages))

@router.message(Choice.salary, F.text.in_(available_salary))
async def salary(message: types.Message, state: FSMContext):
    global age_choise
    if (age_choise == 'Средний') and (message.text == 'Средняя'):
        await message.answer(f'Вы всё прошли, с вами свяжутся!', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(f'Вы нам не подходите! ', reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(Choice.salary)
async def salary_incorrectly(message: types.Message):
    await message.answer(f'Неправильно! Попробуй еще раз!', reply_markup=make_keyboard(available_grades))
