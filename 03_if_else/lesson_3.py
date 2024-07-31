# Task 1
#
# a, b = float(input()), float(input())
# d = a if a > b else b
# print(d)


# Task 2
#
# a = int(input())
# msg = 'кратно 3' if a % 3 == 0 else 'не кратно 3'
# print(msg)


# Task 3
#
# word = input().strip()
# msg = 'палиндром' if word.lower() == word[::-1].lower() else 'не палиндром'
# print(msg)


# Task 4
#
# number = int(input().strip())
# res = 'True' if number == 1 else 'False'
# print(res)


# Task 5

time = int(input().strip())
next_time = 0 if time == 59 else time + 1
print(next_time)

