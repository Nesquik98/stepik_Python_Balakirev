# Task 1
# def get_sq(x):
#     return x ** 2
#
#
# num = float(input())
#
# result = get_sq(num)
# print(result)


# Task 2
# def is_triangle(*args) -> bool:
#     if len(*args) != 3:
#         return False
#     a, b, c = args
#     return abs(a - b) < c and abs(b - c) < a and abs(c - a) < b


# Task 3
# def is_large(s: str) -> bool:
#     return len(s) >= 3


# Task 4
# def parity_check(number):
#     return number % 2 == 0
#
#
# while True:
#     x = int(input())
#     if x == 1:
#         break
#     if parity_check(x):
#         print(x)


# Task 5
# def parity_check(num: int) -> bool:
#     return num % 2 != 0
#
#
# lst_d = list(map(int, input().split()))
# lst = [x for x in lst_d if parity_check(x)]
# print(*lst)


# Task 6
# tp = input().strip()
# if tp == 'RECT':
#     def get_sq(length, width):
#         return length * width
# else:
#     def get_sq(side):
#         return side * side


# Task 7
# def is_long_city(city: str) -> bool:
#     return len(city) >= 6
#
#
# cities = input().strip().split()
# lst = [city for city in cities if is_long_city(city)]
# print(*lst)


# Task 8
# def city_length(city: str) -> tuple:
#     return city, len(city)
#
#
# cities = input().strip().split()
# d = {city: city_length(city)[1] for city in cities}
# a = sorted(d, key=d.get)
# print(*a)


# Task 9
digs = list(map(int, input().strip().split()))


def multiply(a: int, b: int) -> int:
    return a * b


print(multiply(min(digs), max(digs)))