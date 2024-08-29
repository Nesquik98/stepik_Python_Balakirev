# Task 1
# morse = {
#     'А': '.-',  'Б': '-...', 'В': '.--',  'Г': '--.',  'Д': '-..',  'Е': '.',    'Ё': '.',    'Ж': '...-', 'З': '--..',
#     'И': '..',  'Й': '.---', 'К': '-.-',  'Л': '.-..', 'М': '--',   'Н': '-.',   'О': '---',  'П': '.--.', 'Р': '.-.',
#     'С': '...', 'Т': '-',    'У': '..-',  'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
#     'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-', ' ': '-...-'
# }
# user_input = input().upper()
# result = []
# for i in user_input:
#     result.append(morse[i])
# result = ' '.join(result)
# print(result)


# Task 2
# morse = {
#     'А': '.-',  'Б': '-...', 'В': '.--',  'Г': '--.',  'Д': '-..',  'Е': '.',    'Ё': '.',    'Ж': '...-', 'З': '--..',
#     'И': '..',  'Й': '.---', 'К': '-.-',  'Л': '.-..', 'М': '--',   'Н': '-.',   'О': '---',  'П': '.--.', 'Р': '.-.',
#     'С': '...', 'Т': '-',    'У': '..-',  'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
#     'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-', ' ': '-...-'
# }
#
# morse_reverse = {}
# for key, value in morse.items():
#     morse_reverse[value] = key
# code_string = input().split(' ')
# code_massage = []
#
# for i in code_string:
#     if i in morse_reverse:
#         # Получение соответствующего символа
#         decoded_char = morse_reverse[i]
#         if decoded_char == 'Ё':
#             decoded_char = 'Е'
#         code_massage.append(decoded_char.lower())
# result = ''.join(code_massage)
# print(result)


# Task 3
# input_numbers = list(input().split())
# non_repeating_numbers = {}
# numbers_list = []
# for num in input_numbers:
#     if num not in non_repeating_numbers:
#         non_repeating_numbers[num] = 1
#         numbers_list.append(num)
# print(' '.join(numbers_list))


# Task 4
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
birthdays = {}
for entry in lst_in:
    day, name = entry.split()
    day = int(day)
    if day in birthdays:
        birthdays[day].append(name)
    else:
        birthdays[day] = [name]
for day, name in birthdays.items():
    print(f"{day}: {', '.join(name)}")
