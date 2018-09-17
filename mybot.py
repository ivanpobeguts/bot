# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import datetime


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
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_constellation))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def get_constellation(bot, update):
    user_text = update.message.text
    constel = count_constellation(user_text.split(" ")[1])
    if constel == None:
        constel = 'No such planet'
    update.message.reply_text(constel)


def count_constellation(planet_name):
    today_date = str(datetime.today().date())

    if planet_name == 'Mars':
        planet = ephem.Mars(today_date)
    elif planet_name == 'Mercury':
        planet = ephem.Mercury(today_date)
    elif planet_name == 'Venus':
        planet = ephem.Venus(today_date)
    elif planet_name == 'Jupiter':
        planet = ephem.Jupiter(today_date)
    elif planet_name == 'Saturn':
        planet = ephem.Saturn(today_date)
    elif planet_name == 'Uranus':
        planet = ephem.Uranus(today_date)
    elif planet_name == 'Neptune':
        planet = ephem.Neptune(today_date)
    elif planet_name == 'Pluto':
        planet = ephem.Pluto(today_date)
    else:
        return None

    constel = ephem.constellation(planet)
    return constel[1]  


if __name__ == '__main__':
 main()