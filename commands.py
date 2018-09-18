from helper import count_constellation
import re


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
