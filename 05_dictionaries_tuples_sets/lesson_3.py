# Task 1
t = (3.4, -56.7)
print(t + tuple([int(i) for i in input().split()]))


# Task 2
cities_tuple = tuple(input().split())
if 'Москва' not in cities_tuple:
    cities_tuple += ('Москва',)
print(*cities_tuple)

# or

cities_tuple = tuple(input().split())
cities_tuple += [(), ('Москва',)]['Москва' not in cities_tuple]
print(*cities_tuple)




