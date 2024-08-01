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




