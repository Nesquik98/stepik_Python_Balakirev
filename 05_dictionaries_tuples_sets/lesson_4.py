# Task 1
# s = list(map(float, input().split()))
# print(*sorted(s))

# Task 2
# suggestion = set(list(input().lower().split()))
# print(len(suggestion))


# Task 3
# num = set()
# suggestion = input()
# for i in suggestion:
#     if i.isdigit():
#         num.add(i)
# if num:
#     print(*sorted(num))
# else:
#     print('НЕТ')


# Task 4
import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(len(set(lst_in))


# Task 5
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# names = [x[:x.index(':')] for x in lst_in]
# print(len(set(names)))


# Task 6
# import sys
# city = list(map(str.strip, sys.stdin.readlines()))
# cities = set()
# for i in city:
#     if i == 'q':
#         break
#     cities.add(i)
# print(len(cities))