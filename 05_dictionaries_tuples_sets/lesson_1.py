# Task 1
# d = {"house": "дом", "car": "машина",
#      "tree": "дерево", "road": "дорога",
#      "river": "река"}
# print(d)


lst = input().split()
lst = [x.split("=") for x in lst]
d = dict([(x[0], int(x[1])) for x in lst])
print(*sorted(d.items()))
