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

# Task 4
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


# Task 4
# import sys
#
# s, flag = sys.stdin.readlines(), False*
# lst_in = [[1, 0, 0, 0, 0],
#           [0, 0, 1, 0, 1],
#           [0, 0, 0, 0, 0],
#           [0, 1, 0, 1, 0],
#           [0, 0, 0, 0, 0]]  # [list(map(int, x.strip().split())) for x in s]
# flag = False
# for i in range(4):
#     for j in range(4):
#         if lst_in[i][j] + lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] > 1:
#             print('НЕТ')
#             flag = True
#             break
#     if flag:
#         break
# else:
#     print('ДА')-+


# Task 5

# import sys
#
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

# lst_in = [[2, 3, 4, 5, 6],
#           [3, 2, 7, 8, 9],
#           [4, 7, 2, 0, 4],
#           [5, 8, 0, 2, 1],
#           [6, 9, 4, 1, 2]]
# flag = False
# for i_index, i_elem in enumerate(lst_in):
#     for j_index, j_elem in enumerate(i_elem):
#         if j_elem != lst_in[j_index][i_index]:
#             flag = True
#             break
#     if flag:
#         print('НЕТ')
#         break
# else:
#     print('ДА')


