from aiogram import Bot, executor, Dispatcher, types
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode
import logging
import markups
import random


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")

@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup1 = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )
    markup1.add(button_call_1)

    question = "Сколько библиотек можно импорировать в один проект?"
    answers = ['Не более 5', 'Не более 10', 'Не более 20', 'Неограниченное количество']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        open_period=5,
                        reply_markup=markup1
                        )


@dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def quiz1(call: types.CallbackQuery):
    markup2 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    markup2.add(button_call_2)
    question = "Где правильно создана переменная?"
    answers = ['int num = 2', 'var num = 2', 'num = float(2)', '$num = 2']
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        reply_markup=markup2
                        )

@dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def quiz3(call: types.CallbackQuery):
    markup3 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    markup3.add(button_call_2)

    question = "Какого типа данных не существует в python?"
    answers = ['int', 'str', 'elif', 'tuple']
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        reply_markup=markup3
                        )



@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("mem/IMAGE 2022-04-08 02:11:04.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.isdigit():
        a = int(message.text)
        await message.answer(a ** 2)
    else:
        await message.answer(message.text)

@dp.message_handler()
async def game(message: types.Message):
    emo = '🏀 🎲 🎯 🎳 🎰'.split()
    e = random.choice(emo)
    if message.text == 'game':
        await bot.send_dice(message.from_user.id, emo=e)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)

