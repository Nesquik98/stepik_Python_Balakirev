# Task 1
# s = list(map(float, input().split()))
# print(*sorted(s))

# Task 2
# suggestion = set(list(input().lower().split()))
# print(len(suggestion))


# Task 3
num = set()
suggestion = input()
for i in suggestion:
    if i.isdigit():
        num.add(i)
if num:
    print(*sorted(num))
else:
    print('НЕТ')
