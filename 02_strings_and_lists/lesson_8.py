# Task 1 На вход программе подается строка, содержащая целые числа, записанные через пробел. Необходимо прочитать эти
# числа и сохранить в списке lst (как числа в порядке их следования в строке). Проверить, если первое число
# сформированного списка не равно последнему числу, то в список добавить значение True, а иначе - добавить значение
# False. Результирующий список lst вывести на экран командой: print(*lst)
# Реализовать задачу без использования условных операторов.
#
# lst = input().split()
# lst.append(lst[-1] != lst[0])
# print(*lst)


# Task 2
#
# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1, 'Ульяновск')
# print(*cities)


# Task 3

# lst = list(input())
# lst = [x for x in lst if x.isdigit() or x in ('(', ')')]
# lst[0] = str(8)
# print("".join(lst))

# lst.remove('+')
# lst.remove('-')
# lst.remove('-')
# lst.remove('7')
# lst.insert(0, '8')


# Task 4
#
# name = input().split()
# print(f'{name[2]} {name[0][0]}.{name[1][0]}.')
