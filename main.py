import logging
import os
import sys
import time
from datetime import datetime

import pytz
import telebot
from dotenv import load_dotenv

from parse import get_media_names, get_post_content, remove_files

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN_TELEGRAM'))
time_skip: int = 1800
operations: dict = {'sell': 1, 'rent': 3}
channels: dict = {'sell': '@kypitkvsrtirykiev', 'rent': '@kkkarenda'}   


while True:
    for i in operations:
        tz = pytz.timezone('Europe/Kiev')
        current_datetime = datetime.now(tz)
        if 9 > current_datetime.hour > 22:
            time.sleep(time_skip*2)
            logger.info('Too late/early for posts')
        else:
            message_text = str(get_post_content(type=operations[i]))
            media_list = []
            file_names = get_media_names()
            for a in range(0, len(file_names)):
                file = file_names[a]
                media_list.append(
                    telebot.types.InputMediaPhoto(open(file, 'rb')))
            try:
                recipient = channels[i]
                bot.send_media_group(recipient, media_list)
                bot.send_message(recipient, message_text)
                logger.info(f'Message to {recipient} has been sent succesfully')
            except (TypeError, NameError, AttributeError, Exception) as error:
                message = f'Message sending error: {error}'
                logger.error(message)
            remove_files()
            time.sleep(time_skip/120)

    time.sleep(time_skip)


if __name__ == '__main__':
    bot.infinity_polling()
