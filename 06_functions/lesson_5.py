# Task 1
# def get_rec_N(n):
#     if n > 0:
#         get_rec_N(n - 1)
#         print(n)
#
#
# N = int(input())
# get_rec_N(N)

# Task 2
# def get_rec_sum(nums: list[int]) -> int:
#     if not nums:
#         return 0
#     nums[1] += nums[0]
#     return get_rec_sum(nums[1:])
#
#
# nums = list(map(int, input().split()))
# print(get_rec_sum(nums))

# Task 3
# N = int(input())
#
#
# def fib_rec(N, f=[1, 1]):
#     if len(f) == N:
#         return f
#     f.append(f[-1] + f[-2])
#     return fib_rec(N, f)

# Task 4
# n = int(input())
# def fact_rec(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact_rec(n - 1)

# Task 5
# def get_line_list(d, a=[]):
#     for element in d:
#         if isinstance(element, list):  # Если элемент - это список, рекурсивно обрабатываем его
#             get_line_list(element, a)
#         else:
#             a.append(element)
#     return a
#
#
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

# Task 6
def get_path(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return get_path(N - 1) + get_path(N - 2)


N = int(input())
print(get_path(N))