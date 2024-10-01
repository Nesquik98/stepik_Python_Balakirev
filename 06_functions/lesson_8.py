# Task 1 created a function and defined a decorator for that function
# def func_show(func):
#     def wrapper(width, height):
#         p = func(width, height)
#         print(f"Площадь прямоугольника: {p}")
#         return p
#     return wrapper
#
#
# def get_sq(width, height):
#     return width * height


# Task 2 decorator/function/@ operator (convert the passed string into a numbered list of words and return the list)
# def show_menu(func):
#     def wrapper(*args):
#         items = func(*args)
#         for i, item in enumerate(items, 1):
#             print(f"{i}. {item}")
#         return items
#     return wrapper
#
#
# @show_menu
# def get_menu(s):
#     return s.split()
#
# menu = input()


# Task 3 function sorts a list of numbers in ascending order
# def sort_decorator(func):
#     def wrapper(s):
#         lst = func(s)
#         return sorted(lst)
#
#     return wrapper
#
#
# @sort_decorator
# def get_list(s):
#     return list(map(int, s.split()))
#
#
# input_string = input()
# lst = get_list(input_string)
#
# print(*lst)


# Task 4 function converts input strings into lists and returns a dictionary
# def string_to_list(s1, s2):
#     list1 = s1.split()
#     list2 = s2.split()
#     return list1, list2
#
#
# def lists_to_dict_decorator(func):
#     def wrapper(s1, s2):
#         list1, list2 = func(s1, s2)
#         return dict(zip(list1, list2))
#     return wrapper
#
#
# @lists_to_dict_decorator
# def strings_to_list(s1, s2):
#     list1 = s1.split()
#     list2 = s2.split()
#     return list1, list2
#
#
# s1, s2 = input(), input()
# d = strings_to_list(s1, s2)
#
# print(*sorted(d.items()))


# Task 5 transliteration using the decarated function
# def replace_symbols(func):
#     def wrapper(s):
#         result = func(s)
#         while '--' in result:
#             result = result.replace('--', '-')
#         if result.startswith('-'):
#             result = result[1:]
#         if result.endswith('-'):
#             result = result[:-1]
#         return result
#     return wrapper
#
#
# @replace_symbols
# def transliterate(s):
#     t = {
#         'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
#     }
#     s = s.lower().strip()
#     result = []
#
#     for char in s:
#         if char in t:
#             result.append(t[char])
#         elif char in ' -:;.,_':
#             if result and result[-1] != '-':
#                 result.append('-')
#         elif char in '!?':
#             if result and result[-1] == '-':
#                 result[-1] = char
#             else:
#                 result.append(char)
#         else:
#             result.append(char)
#     return ''.join(result)
#
#
# s = input()
# print(transliterate(s))

