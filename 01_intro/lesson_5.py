# Task 1 Напишите программу, которая из входного потока читает вещественное число. Нужно определить, что целая
# часть  прочитанного числа кратна 3. На экран вывести True, если кратно и False - в противном случае. Задача делается
# без использования условного оператора.
#
# a = float(input())
# print(int(a) % 3 == 0)


# Task 2 Напишите программу, которая читает из входного потока стоимость книги X рублей в виде вещественного числа (например, X = 435.78)
# - положительное вещественное число с точностью до сотых (два знака после запятой). Требуется определить, является ли дробное значение
# # (число после запятой) больше 50. На экран вывести True, если больше и False - в противном случае. Задача делается без использования условного оператора.
#
# x = float(input())
# print((x * 100 % 100) > 50)


# Task 3 Напишите программу, в которой читаются два целочисленных значения, записанных в одну строчку через пробел, с помощью команды:
# a, b = map(int, input().split())
# Необходимо определить, можно ли первое число нацело разделить на второе. На экран вывести True, если делится и False - в противном случае.
# Задача делается без использования условного оператора.
#
# a, b = map(int, input().split())
# print((a % b) == 0)


# Task 4 Напишите программу, в которой читаются три целых положительных числа с помощью команды:
# a, b, c = map(int, input().split())
# Необходимо определить, можно ли их интерпретировать (воспринимать) как длины сторон треугольника. Напомню, что сумма длин двух произвольных
# сторон всегда должна быть больше третьей стороны. На экран вывести True, если треугольник формируется и False - в противном случае.
# Задача делается без использования условного оператора.

a, b, c = map(int, input().split())
print(a + b > c and c + b > a and c + a > b)


