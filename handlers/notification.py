from aiogram import types, Dispatcher

from database import bot_db
from config import bot
import asyncio
import aioschedule
import random



async def random_dish():
    result = await bot_db.sql_command_all(mes)
    r_d = random.randint(0, len(result) - 1)
    await bot.send_photo(chat_id=chat_id.from_user.id, photo=result[r_d][0],
                         caption=f"Name: {result[r_d][1]}\n"
                                 f"Description: {result[r_d][2]}\n"
                                 f"Price: {result[r_d][3]}")
# print(random_dish())
async def scheduler():
    aioschedule.every().day.at('23:05').do(random_dish)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


# @dp.message_handler()
async def echo_message(message: types.Message):
    global mes
    mes = message.chat.id
    global chat_id
    chat_id = message.chat.id

    # Check bad words
    bad_words = "java bitch дурак балбес эшек".split()

    for i in bad_words:
        if i in message.text.lower():
            await message.delete()
            await bot.send_message(message.chat.id,
                                   f"{message.from_user.full_name}, сам ты {i}!!!"
                                   )

    # Send dice
    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji="🎯")

    # notification
    if message.text == "блюдо дня".lower():
        await message.reply("Дождитесь 20:00")
        await scheduler()


def register_hendlers_notification(dp: Dispatcher):
    dp.register_message_handler(echo_message)

