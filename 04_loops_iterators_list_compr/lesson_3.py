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

numbers = list(map(int, input().split()))
summ = 0
for i in numbers:
    if i % 2 != 0:
        summ += i
print(summ)

