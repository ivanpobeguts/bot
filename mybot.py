# -*- coding: utf-8 -*-
# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from commands import *

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater("694299832:AAEm7tyrRzIh1d7ODVpMPkTbY-wJ7S17LmA", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(CommandHandler("wordcount", count_words))
    dp.add_handler(MessageHandler(Filters.text, handle_text_message))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
