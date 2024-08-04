# Task 1
#
# for i in range(11):
#     print(i, sep=' ', end=' ')

# print(*range(11))

# Task 2
#
# print(*range(-10, 1))


# Task 3
#
# print(*range(-10, -1, 2))


# Task 4
#
# print(*range(1, 20, 3))


# Task 5
#
# numbers = list(map(int, input().split()))
# summ = 0
# for i in numbers:
#     if i % 2 != 0:
#         summ += i
# print(summ)


# Task 6
#
# cities = list(map(str, input().split()))
# for i, val in enumerate(cities):
#     cities[i] = len(val)
# print(*cities)


# Task 7
#
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)


# Task 8
#
# n = int(input())
# for i in range(2, int(n**0.5)):
#     if n % i == 0:
#         print('НЕТ')
#         break
# else:
#     print('ДА')


# Task 9
#
# cities = list(map(str, input().split()))
# mark = ['ь', 'ъ', 'ы']
# result = True
#
# for i, city in enumerate(cities):
#
#     if i + 1 == len(cities):
#         break
#
#     if city[-1] not in mark:
#         result = city[-1] == cities[i + 1][0].lower()
#     else:
#         result = city[-2] == cities[i + 1][0].lower()
#
#     if not result:
#         break
#
# if result:
#     print('ДА')
# else:
#     print('НЕТ')


# Task 10
#
# n = int(input())
# summ = []
# for i in range(3, n):
#     if i % 3 == 0 or i % 5 == 0:
#         summ.append(i)
# print(sum(summ))





