import asyncio

from aiogram import executor
from config import dp
import logging
from handlers import client, callback, fsmAdminMenu, notification

from database import bot_db
from handlers.notification import scheduler


async def on_start_up(_):
    # asyncio.create_task(scheduler())
    bot_db.sql_create()

client.register_hendlers_client(dp)
callback.register_hendlers_callback(dp)
fsmAdminMenu.register_hendler_fsmAdminGetUser(dp)

notification.register_hendlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_start_up)