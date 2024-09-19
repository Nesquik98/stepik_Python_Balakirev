# Task 1
# input_numbers = map(int, input().split())
# *lst, x, y, z = input_numbers
# print(*lst)

# Task 2
# input_cities = input().split()
# lst_c = (*input_cities,)
# print(lst_c)

# Task 3
# a, b = [int(x) for x in input().split()]
# lst = [*range(a, b + 1)]
# print(*lst)

# Task 4
# numbers = list(map(float, input().split()))
# cities = input().split()
# lst = [*numbers, *cities]
# print(*lst)

# Task 5
# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # ['название=url', ]
#
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
#
# add_menu = dict(item.split('=') for item in lst_in)  # split: [['название'],['url']], [[],[]]
# menu = {**menu, **add_menu}                          # dict: {'название': 'url', '': ''}
