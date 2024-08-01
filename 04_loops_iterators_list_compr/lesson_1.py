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

n = int(input())
sum = 0
i = 1
while i <= n:
    sum += 1 / i
    i += 1
print(f'{sum:.3f}')