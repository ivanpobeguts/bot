from helper import *
import re


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def handle_text_message(bot, update):
    user_text = update.message.text
    if user_text.startswith('Когда ближайшее полнолуние после'):
        update.message.reply_text(next_full_moon(user_text))
    elif user_text.endswith('='):
        update.message.reply_text(calculate(user_text))
    elif user_text.startswith('сколько будет'):
        update.message.reply_text(calculate_in_words(user_text))


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
