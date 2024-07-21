# Math functions and the math module
# Математические функции и модуль math

# Task 1  Допишите текст программы для вычисления модуля введенного с клавиатуры числа
# в переменную d. Выведите результат (модуль) в консоль с помощью функции print.
#
# d = int(input())
# print(abs(d))


# Task 2 Допишите текст программы для нахождения минимального значения из пяти введенных
# целых чисел с выводом результата в консоль (минимального значения) с помощью функции print.
#
# d1, d2, d3, d4, d5 = map(int, input().split())
# print(min(d1, d2, d3, d4, d5))


# Task 3 Допишите текст программы для нахождения максимального значения из пяти введенных
# целых чисел с выводом результата (максимального значения) в консоль с помощью функции print.
#
# d1, d2, d3, d4, d5 = map(int, input().split())
# print(max(d1, d2, d3, d4, d5))


# Task 4 Допишите текст программы для вычисления евклидового расстояния (гипотенузы)
# по перемещениям a и b (формула): . Округлите результат с точностью до сотых.
# Полученное значение выведите на экран.
#
# a, b = map(int, input().split())
# import math
# result = math.sqrt(a**2 + b**2)
# result_rounded = round(result, 2)
# print(result_rounded)


# Task 5 Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе),
# используя формулу ., где . Выведите результат в консоль в виде целого числа с помощью функции print.
# Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.
#
# import math
# n, k = map(int, input().split())
# result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
# print(result)


# Task 6  В летний лагерь нужно отвезти n детей и m вожатых с помощью автобусов (значения считываются
# из входного потока в программе ниже). Максимальная вместимость каждого автобуса 20 человек.
# Допишите программу для вычисления минимального числа автобусов, необходимых для перевозки детей
# вместе с вожатыми. Результат выведите в консоль в виде целого числа.

from math import ceil
n, m = map(int, input().split())
print(ceil((n + m) / 20))