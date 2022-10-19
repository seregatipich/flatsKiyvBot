import os
import sqlite3
import time

import telebot
from dotenv import load_dotenv

from parse import get_info

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN_TELEGRAM'))

while True:
    bot.send_message('@kypitkvsrtirykiev', get_info())
    time.sleep(900)


if __name__ == '__main__':
    bot.infinity_polling()
