# Task 1
#
# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
#
# print(m)
# number = int(input())
# if number == 1:
#     print('1. Введение в Python')
# elif number == 2:
#     print('2. Строки и списки')
# elif number == 3:
#     print('3. Условные операторы')
# elif number == 4:
#     print('4. Циклы')
# elif number == 5:
#     print('5. Словари, кортежи и множества')
# elif number == 6:
#     print('6. Выход')
# else:
#     print('Ошибка. Введите число от 1 до 6')


# Task 2
#
# numbers = input().split()
# a = int(numbers[0])
# b = int(numbers[1])
# c = int(numbers[2])
# min_numbers = a
# if min_numbers > b:
#     min_numbers = b
# if min_numbers > c:
#     min_numbers = c
# print(min_numbers)


# Task 3
#
# weight = float(input())
# if weight <= 60:
#     print('1')
# elif weight <= 64:
#     print('2')
# elif weight <= 69:
#     print('3')
# elif weight > 69:
#     print('4')


# Task 4
#
# days = int(input())
# if days == 1:
#     days = 'понедельник'
# elif days == 2:
#     days = 'вторник'
# elif days == 3:
#     days = 'среда'
# elif days == 4:
#     days = 'четверг'
# elif days == 5:
#     days = 'пятница'
# elif days == 6:
#     days = 'суббота'
# elif days == 7:
#     days = 'воскресенье'
# else:
#     days = 'Данного дня недели не существует'
# print(days)


# Task 5
#
# month = int(input())
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     month = 31
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     month = 30
# elif month == 2:
#     month = 28
# else:
#     month = 'В месяце не может быть столько дней'
# print(month)


# Task 6

all_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = map(int, input().split())
prev_month = None
next_month = None
next_day = None
prev_day = None
if day == 1:
    prev_day = all_month[month - 2]
    next_day = 2
    prev_month = month - 1 if month != 1 else 12
    next_month = month
elif day == all_month[month - 1]:
    prev_day = day - 1
    next_day = 1
    prev_month = month
    next_month = month + 1 if month != 12 else 1
else:
    prev_day = day - 1
    next_day = day + 1
    next_month = month
    prev_month = month
print(f"{'%02d' % prev_month}.{'%02d' % prev_day} {'%02d' % next_month}.{'%02d' % next_day}")