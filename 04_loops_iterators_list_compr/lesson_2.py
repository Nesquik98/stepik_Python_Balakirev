# Task 1
#
# p = [0] * 10
# count = 0
# while count < 5:
#     index = int(input())
#     if p[index] == 1:
#         continue
#     p[index] = 1
#     count += 1
# print(*p)


# Task 2
#
# p = 1
# while True:                 # запуск бесконечного цикла
#     num = int(input())
#     if num == 0:
#         break
#     if num < 0:
#         continue
#     p *= num
# print(p)


# Task 3
#
# city = input().split()
# i = 0       # инициализация индекса
# word_length = True      # флаг проверки длин слов
# while i < len(city):
#     if len(city[i]) <= 5:
#         word_length = False
#         break
#     i += 1
# if word_length:
#     print('ДА')
# else:
#     print('НЕТ')


# Task 4
#
# names = input().split()
# i = 0
# name_rev = False
# while i < len(names):
#     name = names[i] #текущее имя
#     if name[0].lower() == name[-1].lower():  # первая и последняя буква строчные
#         name_rev = True
#         break # найдено слово цикл прерван
#     i += 1
# if name_rev:
#     print('ДА')
# else:
#     print('НЕТ')


# print(('НЕТ','ДА')[any(i for i in input().lower().split() if i[0] == i[-1])])

# Task 5
#
# n = int(input())
# if n > 99:
#     print('слишком большое значение n')
# else:
#     i = 15
#     while i <= n:
#         if i % 3 == 0 and i % 5 == 0:
#             print(i, end=' ')
#         i += 15


# Task 6
#
# n = int(input())
# x = 1
# while x * x <= n:
#     x += 1
# print(x)


# Task 7

distance = 10
day = 1
x = int(input())
while distance <= x: #пока дистанция не станет больше x
    distance += distance * 0.1 #увеличение дистанции на 10%
    day += 1 #следующий день
print(day)
