# Task 1
#
# n, m = map(int, input().split())
# counter = n   #отслеживание текущего цикла
# while counter <= m:
#     print(counter ** 2, end=' ')
#     counter += 1


# Task 2
#
# x = float(input())
# counter = 2
# while counter <= 10:
#     x_res = x * counter
#     print(f'{x_res:.1f}', end=' ')
#     counter += 1


# Task 3
#
# n = int(input())
# sum = 0
# i = 1
# while i <= n:
#     sum += 1 / i
#     i += 1
# print(f'{sum:.3f}')


# Task 4
#
# counter = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     counter += num
# print(counter)


# Task 5
#
# s = input()
# while '--' in s:
#     s = s.replace('--', '-')
# print(s)


# Task 6
#
# n = int(input())
# counter = 1
# while n > 0:
#     n_last = n % 10
#     counter *= n_last
#     n = n // 10
# print(counter)


# Task 7
#
# n = int(input())
# if n == 0:
#     print('')
# else:
#     f1, f2 = 1, 1
#     res_f = []
#     while len(res_f) < n:
#         res_f.append(f1)
#         f1, f2 = f2, f1 + f2
# print(' '.join(map(str, res_f)))


# Task 8
#
# n = int(input())
# a = 1
# i = 3
# while i < n:
#     a *= 2
#     i += 3
# print(a)


# Task 9
#
# counter = 1000
# n = int(input())
# for i in range(n):
#     counter += counter * 0.05
# print(round(counter, 2))

counter = 1000
year = 0
n = int(input())
while year < n:
    counter += counter * 0.05
    year += 1
print(round(counter, 2))