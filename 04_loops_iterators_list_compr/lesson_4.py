# Task 1

a = input()
index_lst = []
start = 0
while True:
    start = a.find('ра', start)
    if start == -1:
        break
    index_lst.append(start)
    start += 2

if index_lst:
    print(*index_lst)
else:
    print(-1)
