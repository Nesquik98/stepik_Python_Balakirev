# Task 1
# d = {"house": "дом", "car": "машина",
#      "tree": "дерево", "road": "дорога",
#      "river": "река"}
# print(d)
#
# lst = input().split()
# lst = [x.split("=") for x in lst]
# d = dict([(x[0], int(x[1])) for x in lst])
# print(*sorted(d.items()))


# Task 2
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for i in lst_in:
#     key, value = i.split("=")
#     key = int(key)
#     d[key] = value
# print(*sorted(d.items()))


# Task 3
# input_string = input().strip()  #удаляем пробелы вокруг строк
# pairs = input_string.split(' ')
# d = {pair.split('=')[0]: pair.split('=')[1] for pair in pairs}
# keys_to_check = ['house', 'True', '5']
# if all(key in d for key in keys_to_check):
#     print("ДА")
# else:
#     print("НЕТ")


# Task 4
# input_string = input().strip()
# pairs = input_string.split(' ')
# d = {pair.split('=')[0]: pair.split('=')[1] for pair in pairs}
# if "False" in d:
#     del d["False"]
# if "3" in d:
#     del d["3"]
# print(*sorted(d.items()))