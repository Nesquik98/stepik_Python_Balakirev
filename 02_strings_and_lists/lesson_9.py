# Task 1
#
# lst = [5.4, 6.7, 10.4]
# digs = list(map(int, input().split()))
# lst.append(digs)
# print(lst)


# Task 2
#
# result = [input().split(), input().split(), input().split()]
# print(result)


# Task 3
#
# result = [input().split(), input().split(), input().split()]
# print(result[0][-1], result[1][-1], result[2][-1])


# Task 4

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]
word = input()
print(word in t[0] or word in t[1] or word in t[2])