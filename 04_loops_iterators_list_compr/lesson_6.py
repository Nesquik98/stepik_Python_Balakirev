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
import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# ['Hello', 'World', 'Python']  - пример того что будет создано, все пробелы в начале и конце строк удалены.

for string in lst_in:
    print('-'.join(string.split()))



