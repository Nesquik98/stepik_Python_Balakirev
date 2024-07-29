# Task 1
#
# a, b = map(float, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)


# Task 2

word = input().lower()
if word == word[::-1]:
    print('ДА')
else:
     print('НЕТ')