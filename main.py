import os
import time

import telebot
from dotenv import load_dotenv

from parse import get_post_content

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN_TELEGRAM'))


while True:
    bot.send_photo('@kypitkvsrtirykiev', 'realty-prodaja-kvartira-kiev-vinogradar-tiraspolskaya-ulitsa__0cleaned.webp', get_post_content())
    time.sleep(900)


if __name__ == '__main__':
    bot.infinity_polling()
