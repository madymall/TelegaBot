from aiogram import Bot, executor, Dispatcher, types
from decouple import config
import logging
import markups


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!")

@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    question = "Сколько библиотек можно импорировать в один проект?"
    answers = ['Не более 5', 'Не более 10', 'Не более 20', 'Неограниченное количество']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        reply_markup=markups.markup
                        )

@dp.message_handler(commands=['quiz2'])
async def quiz2(message: types.Message):
    question = "Где правильно создана переменная?"
    answers = ['int num = 2', 'var num = 2', 'num = float(2)', '$num = 2']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=markups.button_next
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

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)

