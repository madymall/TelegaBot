from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp, ADMIN

from database import bot_db

# @dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")

# @dp.message_handler(commands=['quiz'])
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


# @dp.message_handler(commands=['quiz1'])
async def quiz1(message: types.Message):
    markup2 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    markup2.add(button_call_2)
    question = "Где правильно создана переменная?"
    answers = ['int num = 2', 'var num = 2', 'num = float(2)', '$num = 2']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5,
                        reply_markup=markup2
                        )

# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("mem/IMAGE 2022-04-08 02:11:04.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

# @dp.message_handler(commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id != ADMIN:
            await message.reply("Ты не мой БОСС!")

        if not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")

        else:
            await message.bot.delete_message(message.chat.id, message.message_id)
            await message.bot.kick_chat_member(message.chat.id, user_id=message.reply_to_message.from_user.id)
            await bot.send_message(
                message.chat.id,
                f"{message.reply_to_message.from_user.full_name} забанен по воле {message.from_user.full_name}")


    else:
        await message.answer("Это работает только в группах!")

async def show_random_dish(message: types.Message):
    await bot_db.sql_command_random(message)

def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(mem, commands=["mem"])
    dp.register_message_handler(hello, commands=["start"])
    dp.register_message_handler(quiz, commands=["quiz"])
    dp.register_message_handler(quiz, commands=["quiz1"])
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")
    dp.register_message_handler(show_random_dish, commands=["random"])