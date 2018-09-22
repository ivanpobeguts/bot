import re


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
