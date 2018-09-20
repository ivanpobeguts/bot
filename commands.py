from helper import count_constellation
from datetime import datetime
import re
import ephem


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def next_full_moon(bot, update):
    user_text = update.message.text
    if user_text.startswith('Когда ближайшее полнолуние после'):
        date_string = user_text[-11:-1]
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            next_full_moon = ephem.next_full_moon(date_string)
            update.message.reply_text(str(next_full_moon))
        except ValueError:
            update.message.reply_text(str("Неправильный формат даты, ожидается YYYY-MM-DD"))


def get_constellation(bot, update):
    user_text = update.message.text
    constel = count_constellation(user_text.split(" ")[1])
    if constel == None:
        constel = 'No such planet'
    update.message.reply_text(constel)


def count_words(bot, update):
    user_text = update.message.text
    if len(re.findall(r'\"(.+?)\"', user_text)) != 0:
        phrase = re.findall(r'\"(.+?)\"', user_text)[0]
        words = re.findall(r'\w+', phrase)
        words_count = len(words)
        update.message.reply_text('{} слов'.format(words_count))
    else:
        phrase = 'Строка должна быть в кавычках'
        update.message.reply_text(str(phrase))
