# Task 1

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

print(m)
number = int(input())
if number == 1:
    print('1. Введение в Python')
elif number == 2:
    print('2. Строки и списки')
elif number == 3:
    print('3. Условные операторы')
elif number == 4:
    print('4. Циклы')
elif number == 5:
    print('5. Словари, кортежи и множества')
elif number == 6:
    print('6. Выход')
else:
    print('Ошибка. Введите число от 1 до 6')

