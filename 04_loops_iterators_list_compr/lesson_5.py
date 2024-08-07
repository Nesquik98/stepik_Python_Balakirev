# Task 1
cities = list(map(str, input().split()))
iterator = iter(cities)

for i, element in enumerate(iterator):
    print(element)
    if i == 1:
        break
