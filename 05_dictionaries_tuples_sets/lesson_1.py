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
