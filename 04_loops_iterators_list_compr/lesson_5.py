# Task 1
# cities = list(map(str, input().split()))
# iterator = iter(cities)
#
# for i, element in enumerate(iterator):
#     print(element)
#     if i == 1:
#         break


# Task 2
iterator = iter(input())
for element in iterator:
    if element == ' ':
        break
    print(element, end='')
