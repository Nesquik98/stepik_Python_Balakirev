# Task 1
#
# a, b = map(float, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)


# Task 2
#
# word = input().lower()
# if word == word[::-1]:
#     print('ДА')
# else:
#      print('НЕТ')


# Task 3
#
# m, n = map(int, input().split())
# if m % n == 0:
#     print(m // n)
# else:
#     print(f'{m} на {n} нацело не делится')


# Task 4
#
# a, b, c = map(int, input().split())
#
# if c ** 2 == a ** 2 + b ** 2:
#     print('ДА')
# else:
#     print('НЕТ')


# Task 5
#
# a = input().strip()
# if a [-1]== '7':
#     print('ДА')
# else:
#     print('НЕТ')


# Task 6
#
# a = input().strip().lower()
# if 't' in a and 'h' in a and 'o' in a:
#     print('ДА')
# else:
#     print('НЕТ')


# Task 7
#
# cities = list(input().split())
# if 'Москва' in cities:
#     cities.remove('Москва')
# print(*cities)


# Task 8
#
# a, b, c, d = map(int, input().split())
# if (a - c) >= 2 and (b - d) >= 2 or (a - d) >= 2 and (b - c) >= 2:
#     print('ДА')
# else:
#     print('НЕТ')


# Task 9
#
# number = input()
# if number.isdigit() and len(number) == 6:
#     if sum(int(a) for a in number[:3]) == sum(int(a) for a in number[3:]):
#         print('ДА')
#     else:
#         print('НЕТ')


# Task 10

t = float(input())
if (t % 5) < 3:
    print('green')
else:
    print('red')