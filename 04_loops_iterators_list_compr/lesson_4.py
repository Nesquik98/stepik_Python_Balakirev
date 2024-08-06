# Task 1
#
# a = input()
# index_lst = []
# start = 0
# while True:
#     start = a.find('ра', start)
#     if start == -1:
#         break
#     index_lst.append(start)
#     start += 2
#
# if index_lst:
#     print(*index_lst)
# else:
#     print(-1)


# Task 2
#
# number = input('Enter number')
# if not number.startswith('+7'):
#     print('НЕТ')
# elif not (number[2] == '(' and number[6] == ')' and number[10] == '-' and number[13] == '-'):
#     print('НЕТ')
# elif not (number[3:6] + number[7:10] + number[11:13] + number[14:]).isdigit():
#     print('НЕТ')
# else:
#     print('ДА')


# Task 3
# numbers = input().strip().replace(' ', '')
#
# operands_lst = [x for x in numbers if x in ('-', '+')]
# numbers_lst = []
#
# start_num_index = 0
# for index, item in enumerate(numbers):
#     if not item.isdigit():
#         numbers_lst.append(int(numbers[start_num_index:index]))
#         start_num_index = index + 1
# else:
#     numbers_lst.append(int(numbers[start_num_index:]))
#
#
# temp = None
# for index, item in enumerate(operands_lst):
#     if item == '+':
#         temp = numbers_lst[index] + numbers_lst[index + 1]
#         numbers_lst[index + 1] = temp
#     elif item == '-':
#         temp = numbers_lst[index] - numbers_lst[index + 1]
#         numbers_lst[index + 1] = temp
# print(temp)


# Task 4
# numbers = list(map(int, input().split()))
# for i, number in enumerate(numbers):
#     numbers[i] = number ** 2
# print(*numbers)


# Task 5
#
# numbers = list(map(int, input().split()))
# index = 0
# while index < len(numbers):
#     numbers.insert(index, numbers[index])
#     index += 2
# print(*numbers)


numbers = list(map(int, input().split()))
for i in range(0, len(numbers) * 2, 2):
    numbers.insert(i, numbers[i])
print(*numbers)
