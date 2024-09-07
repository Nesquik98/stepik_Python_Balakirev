# Task 1
# string = input().split()
# grade1 = int(string[0])
# grades = string[1:]
#
# d = {grade1 + i: grade for i, grade in enumerate(grades)}
#
# print(d[4])


# Task 2
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(len({number for number in lst_in}))


# Task 3
# string = set(input().lower().split())
# print(len({word for word in string if len(word) >= 3}))


# Task 4
# import sys
# string = sys.stdin.read().strip().lower().split()
# uniq_word = {word for word in string}
# count_word = {word: string.count(word) for word in uniq_word}
# print(count_word.get('и', 0))
#
# #OR
#
# lst = input().lower().split()
# d = {i: lst.count(i) for  i in lst}
# print(d['и'] if 'и' in d else 0)





