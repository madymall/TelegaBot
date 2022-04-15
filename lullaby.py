from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging

from aiogram import executor
from config import dp
import logging
from handlers import callback, client, notification, fsmAdminMenu

client.register_hendlers_client(dp)
callback.register_hendlers_callback(dp)
fsmAdminMenu.register_hendler_fsmAdminGetUser(dp)

notification.register_hendlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)