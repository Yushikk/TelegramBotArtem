import os
from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Whichname(StatesGroup):
    taskname = State()
    hours = State()
    day = State()
    minutes = State()
    result_filename = ''


class ResultName(StatesGroup):
    day1 = State()


class Clear(StatesGroup):
    day2 = State()


@router.message(Command('start'))
async def command_start(message):
    await message.answer(
        f'Привет!\n{message.from_user.first_name}\nРад тебя видеть😀 Я бот-Ежедневник, который упростит тебе жизнь')


@router.message(Command('help'))
async def command_help(message):
    await message.answer("""Всегда рад тебе помочь! Вот список команд, которые я могу выполнить
    /start - приветствие
    /help - расскажу о том, что умею
    /add - позволит добавить дело в бот. Сначала он попросит вас ввести название самого дела, а затем выбрать день и время
    /show - покажет все дела на конкретный день
    /clear - удаляет абсолютно все дела за конкретный день""")


@router.message(F.text == '/add')
async def func(message: Message, state: FSMContext):
    await state.set_state(Whichname.day)
    await message.answer('На какой день недели добавить дело', reply_markup=choose(message.from_user.id))


def choose(user_telegram_id: int) -> ReplyKeyboardMarkup:
    choose_list = [
        [KeyboardButton(text="Понедельник")],
        [KeyboardButton(text="Вторник")],
        [KeyboardButton(text="Среда")],
        [KeyboardButton(text="Четверг")],
        [KeyboardButton(text="Пятница")],
        [KeyboardButton(text="Суббота")],
        [KeyboardButton(text="Воскресенье")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=choose_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


@router.message(Whichname.day)
async def func_day(message: Message, state: FSMContext):
    Whichname.result_filename = str(message.from_user.id) + message.text + '.txt'
    file = open(Whichname.result_filename, 'a')
    file.write(f'{message.text}\n')
    file.close()
    await state.update_data(day=message.text)
    await state.set_state(Whichname.taskname)
    await message.answer('Введите название дела')


@router.message(Whichname.taskname)
async def func_taskname(message: Message, state: FSMContext):
    file = open(Whichname.result_filename, 'a')
    file.write(f'{message.text}\n')
    file.close()
    await state.update_data(taskname=message.text)
    await state.set_state(Whichname.hours)
    await message.answer('Введите время в часах', reply_markup=chas(message.from_user.id))


@router.message(Whichname.hours)
async def func_hours(message: Message, state: FSMContext):
    file = open(Whichname.result_filename, 'a')
    file.write(f'{message.text}:')
    file.close()
    await state.update_data(hours=message.text)
    await state.set_state(Whichname.minutes)
    await message.answer('Введите минуты', reply_markup=minut(message.from_user.id))


@router.message(Whichname.minutes)
async def func_minutes(message: Message, state: FSMContext):
    file = open(Whichname.result_filename, 'a')
    file.write(f'{message.text}\n')
    file.close()
    await state.update_data(minutes=message.text)
    tasks = await state.get_data()
    await message.answer(
        f'Ваше дело: {tasks["taskname"]}\nДень недели: {tasks["day"]}\nВремя: {tasks["hours"]}:{tasks["minutes"]}')
    await state.clear()


def chas(user_telegram_id: int) -> ReplyKeyboardMarkup:
    chas_list = [
        [KeyboardButton(text="01"), KeyboardButton(text="02"), KeyboardButton(text="03"), KeyboardButton(text="04")],
        [KeyboardButton(text="05"), KeyboardButton(text="06"), KeyboardButton(text="07"), KeyboardButton(text="08")],
        [KeyboardButton(text="09"), KeyboardButton(text="10"), KeyboardButton(text="11"), KeyboardButton(text="12")],
        [KeyboardButton(text="13"), KeyboardButton(text="14"), KeyboardButton(text="15"), KeyboardButton(text="16")],
        [KeyboardButton(text="17"), KeyboardButton(text="18"), KeyboardButton(text="19"), KeyboardButton(text="20")],
        [KeyboardButton(text="21"), KeyboardButton(text="22"), KeyboardButton(text="23"), KeyboardButton(text="00")]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=chas_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


def minut(user_telegram_id: int) -> ReplyKeyboardMarkup:
    minut_list = [
        [KeyboardButton(text="01"), KeyboardButton(text="02"), KeyboardButton(text="03"), KeyboardButton(text="04"),
         KeyboardButton(text="05")],
        [KeyboardButton(text="06"), KeyboardButton(text="07"), KeyboardButton(text="08"), KeyboardButton(text="09"),
         KeyboardButton(text="10")],
        [KeyboardButton(text="11"), KeyboardButton(text="12"), KeyboardButton(text="13"), KeyboardButton(text="14"),
         KeyboardButton(text="15")],
        [KeyboardButton(text="16"), KeyboardButton(text="17"), KeyboardButton(text="18"), KeyboardButton(text="19"),
         KeyboardButton(text="20")],
        [KeyboardButton(text="21"), KeyboardButton(text="22"), KeyboardButton(text="23"), KeyboardButton(text="24"),
         KeyboardButton(text="25")],
        [KeyboardButton(text="26"), KeyboardButton(text="27"), KeyboardButton(text="28"), KeyboardButton(text="29"),
         KeyboardButton(text="30")],
        [KeyboardButton(text="31"), KeyboardButton(text="32"), KeyboardButton(text="33"), KeyboardButton(text="34"),
         KeyboardButton(text="35")],
        [KeyboardButton(text="36"), KeyboardButton(text="37"), KeyboardButton(text="38"), KeyboardButton(text="39"),
         KeyboardButton(text="40")],
        [KeyboardButton(text="41"), KeyboardButton(text="42"), KeyboardButton(text="43"), KeyboardButton(text="44"),
         KeyboardButton(text="45")],
        [KeyboardButton(text="46"), KeyboardButton(text="47"), KeyboardButton(text="48"), KeyboardButton(text="49"),
         KeyboardButton(text="50")],
        [KeyboardButton(text="51"), KeyboardButton(text="52"), KeyboardButton(text="53"), KeyboardButton(text="54"),
         KeyboardButton(text="55")],
        [KeyboardButton(text="56"), KeyboardButton(text="57"), KeyboardButton(text="58"), KeyboardButton(text="59"),
         KeyboardButton(text="00")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=minut_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


@router.message(F.text == '/show')
async def func(message: Message, state: FSMContext):
    await state.set_state(ResultName.day1)
    await message.answer('За какой день недели показать все дела', reply_markup=choose(message.from_user.id))


@router.message(ResultName.day1)
async def func_day1(message: Message, state: FSMContext):
    Whichname.result_filename = str(message.from_user.id) + message.text + '.txt'
    if os.path.exists(Whichname.result_filename):
        file = open(Whichname.result_filename, 'r')
        await message.answer('Ваши дела на этот день:\n' + file.read())
        file.close()
    else:
        await message.answer('На этот день задач нет')
    await state.clear()


@router.message(F.text == '/clear')
async def func(message: Message, state: FSMContext):
    await state.set_state(Clear.day2)
    await message.answer('За какой день недели удалить дела', reply_markup=choose(message.from_user.id))


@router.message(Clear.day2)
async def func_day2(message: Message, state: FSMContext):
    Whichname.result_filename = str(message.from_user.id) + message.text + '.txt'
    if os.path.exists(Whichname.result_filename):
        os.remove(Whichname.result_filename)
        await message.answer('Дела удалены')
    else:
        await message.answer('На этот день задач нет')
    await state.clear()
