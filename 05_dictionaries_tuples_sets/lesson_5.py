# Task 1
# num1 = list(map(int, input().split()))
# num2 = list(map(int, input().split()))
# s = set(num1) & set(num2)
# print(*sorted(s))

# Task 2
# num1 = set(list(map(int, input().split())))
# num2 = set(list(map(int, input().split())))
# print(*sorted(num1 - num2))

# Task 3
# num1 = set(list(map(int, input().split())))
# num2 = set(list(map(int, input().split())))
# print(*sorted(num1 ^ num2))

# Task 4
# print(['НЕТ', 'ДА'][set(input().split()) == set(input().split())])

# Task 5
print('НЕ ДОПУЩЕН' if 2 in set(map(int, input().split())) else 'ДОПУЩЕН')