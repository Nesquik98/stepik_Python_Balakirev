# N = 6
# a = [0] * N
#
# for i in range(N):
#     a[i] = i ** 2
# print(a)
#
# a = [x ** 2 for x in range(N)]


# d_inp = input("Целые числа через пробел: ")
#
# a = [int(d) for d in d_inp.split()] # [1, 2, 3, 4]
# a = [d for d in d_inp.split()]        # ['1', '2', '3', '4']
#
# print(a)


# d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
# a = ['четное' if x % 2 == 0 else 'нечетное'
#      for x in d
#      if x > 0
#      ]
# print(a)


# Task 1
# numbers = input()
# lst = [float(x) for x in numbers.split()]    # [5.56, -8.7, 1.0, 3.14, 77.845]
# lst_abs = [abs(x) for x in lst]
# print(lst_abs)

# lst = input().split()
# lst_abs = [abs(float(x)) for x in lst]
# print(lst_abs)


# Task 2
# print([int(x) for x in input()])


# Task 3
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             print(1, end=' ')
#         else:
#             print(0, end=' ')

# N = int(input())
# lst = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
# for k in lst:
#     print(*k)
#
# N = int(input())
# mtrx = [[[0, 1][x == y] for y in range(N)] for x in range(N)]
# for line in mtrx:
#     print(*line)


# Task 4
# input_cities = input().split()
# long_cities = [city for city in input_cities if len(city) > 5]
# print(*long_cities)

# print(*[city for city in input().split() if len(city) > 5])


# Task 5
# number = int(input())
# print(*[x for x in range(1, number + 1) if number % x == 0])


# Task 6
# n = int(input())
# mtrx = [[x for y in range(n)] for x in range(n)]
# for line in mtrx:
#     print(*line)

# Task 7
# nums = list(map(float, input().split()))
# print(*[num for idx, num in enumerate(nums) if idx % 2 == 0])


# Task 8
# num1 = list(map(int, input().split()))
# num2 = list(map(int, input().split()))
# print(*[num1[i] + num2[i] for i in range(len(num1))])
#
# print(*[sum(pair) for pair in zip(*[list(map(int, input().split())) for _ in range(2)])])


# Task 9
# input_str = input().split()
# lst = [[input_str[i], int(input_str[i + 1])] for i in range(0, len(input_str), 2)]
# print(lst)
