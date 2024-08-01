# Task 1

n, m = map(int, input().split())
counter = n  #отслеживание текущего цикла
while counter <= m:
    print(counter ** 2, end=' ')
    counter += 1

