# Task 1
# t = (3.4, -56.7)
# print(t + tuple([int(i) for i in input().split()]))


# Task 2
# cities_tuple = tuple(input().split())
# if 'Москва' not in cities_tuple:
#     cities_tuple += ('Москва',)
# print(*cities_tuple)

# or
#
# cities_tuple = tuple(input().split())
# cities_tuple += [(), ('Москва',)]['Москва' not in cities_tuple]
# print(*cities_tuple)


# Task 3
# cities = tuple(input().split())
# if 'Ульяновск' in cities:
#     cities = tuple(city for city in cities if city != 'Ульяновск')
# print(*cities)


# Task 4
# names = tuple(input().split())
# filter_names = [name for name in names if 'ва' in name.lower()]
# print(' '.join(name.lower() for name in filter_names))

# or
#
# names = tuple(map(str.lower, input().split()))
# print(*filter(lambda x: 'ва' in x, names))


# Task 5
# numbers = tuple(map(int, input().split()))
# unigue_numbers = ()
# for number in numbers:
#     if number not in unigue_numbers:
#         unigue_numbers += (number,)
# print(' '.join(map(str, unigue_numbers)))


# Task 6
# numbers = tuple(map(int, input().split()))
# repeated_numbers = []
#
# for index, number in enumerate(numbers):
#     if numbers.count(number) > 1:
#         repeated_numbers.append(index)
#
# print(' '.join(map(str, repeated_numbers)))


# Task 7
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# num = int(input())
# t2 = tuple(row[:num] for row in t[:num])
# for row in t2:
#      print(' '.join(map(str, row)))

# or

num = int(input())
mtrx = tuple(tuple(int(x == y) for x in range(num)) for y in range(num))
for row in mtrx:
     print(*row)