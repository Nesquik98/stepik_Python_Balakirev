# Task 1
# N = int(input())
# for i in range(N):
#     for j in range(N):
#         if j == N - 1:
#             print(5, end='')
#         else:
#             print(1, end=' ')
#     print()

# n = int(input())
# mtrx = [[1] * (n-1) + [5] for _ in range(n)]
# for line in mtrx:
#   print(*line)

# Task 2
# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # ['Hello', 'World', 'Python']  - пример того что будет создано, все пробелы в начале и конце строк удалены.
#
# for string in lst_in:
#     print('-'.join(string.split()))

#Task 4
# def is_prime(number):
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# n = int(input())
# for i in range(2, n):
#     if is_prime(i):
#         print(i, end=' ')


# n = int(input())
# primes = []
# for i in range(2, n):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)
# print(' '.join(map(str, primes)))


# n, res = int(input()), []  # Вводится число n и инициализируется пустой список
# for num in range(2, n):    # Итерируем от 2 до n-1
#     for s in range(2, num // 2 + 1):    # Проверяем делители от 2 до num // 2 + 1
#         if num % s == 0:                # Если num делится на s, num не простое
#             break
#     else:                   # Если не был выполнен break, выполняется else
#         res.append(num)     # Добавляем простое число в список
# print(*res)