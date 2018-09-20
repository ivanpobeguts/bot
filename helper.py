import ephem
from datetime import datetime
import re


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


def next_full_moon(user_text):
    date_string = user_text[-11:-1]
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        next_full_moon = ephem.next_full_moon(date_string)
        return str(next_full_moon)
    except ValueError:
        return "Неправильный формат даты, ожидается YYYY-MM-DD"


def calculate(user_text):
    try:
        if re.match(r'(\d+)[\+*-/](\d+)', user_text):
            chunks = ['']

            for character in user_text:
                if character.isdigit():
                    if chunks[-1].isdigit():
                        chunks[-1] += character
                    else:
                        chunks.append(character)
                elif character in '+-/*':
                    chunks.append(character)
            if '+' in chunks:
                return int(chunks[1]) + int(chunks[3])
            if '-' in chunks:
                return int(chunks[1]) - int(chunks[3])
            if '*' in chunks:
                return int(chunks[1]) * int(chunks[3])
            if '/' in chunks:
                return int(chunks[1]) / int(chunks[3])
        else:
            return 'Неправильный формат. Пример: 129+389='
    except ZeroDivisionError:
        return 'Деление на ноль'


def calculate_in_words(text):
    numbers_dict = {
        'один': 1,
        'два': 2,
        'три': 3,
        'четыре': 4,
        'пять': 5,
        'шесть': 6,
        'семь': 7,
        'восемь': 8,
        'девять': 9,
        'десять': 10,
    }
    try:
        words = text.lower().split(' ')
        if 'плюс' in words:
            return int(numbers_dict[words[2]]) + int(numbers_dict[words[4]])
        elif 'минус' in words:
            return int(numbers_dict[words[2]]) - int(numbers_dict[words[4]])
        elif 'умножить' in words:
            return int(numbers_dict[words[2]]) * int(numbers_dict[words[5]])
        elif 'разделить' in words:
            return int(numbers_dict[words[2]]) / int(numbers_dict[words[5]])
        else:
            return 'Неверное название операции'
    except ValueError:
        return 'Неправильный формат запроса'
    except ZeroDivisionError:
        return 'Деление на ноль'
    except KeyError:
        return 'Неверный формат числа'