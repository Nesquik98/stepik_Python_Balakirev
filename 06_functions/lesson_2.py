# Task 1
# def get_sq(x):
#     return x ** 2
#
#
# num = float(input())
#
# result = get_sq(num)
# print(result)


# Task 2
# def is_triangle(*args) -> bool:
#     if len(*args) != 3:
#         return False
#     a, b, c = args
#     return abs(a - b) < c and abs(b - c) < a and abs(c - a) < b


# Task 3
# def is_large(s: str) -> bool:
#     return len(s) >= 3


# Task 4
# def parity_check(number):
#     return number % 2 == 0
#
#
# while True:
#     x = int(input())
#     if x == 1:
#         break
#     if parity_check(x):
#         print(x)


# Task 5
def parity_check(num: int) -> bool:
    return num % 2 != 0


lst_d = list(map(int, input().split()))
lst = [x for x in lst_d if parity_check(x)]
print(*lst)


