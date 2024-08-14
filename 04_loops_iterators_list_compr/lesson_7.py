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

number = int(input())
print(*[x for x in range(1, number + 1) if number % x == 0])
