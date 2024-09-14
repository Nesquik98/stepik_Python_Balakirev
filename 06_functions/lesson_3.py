# 1
# import time
#
#
# def get_nod(a, b):
#     """Вычисляется НОД для натуральных чисел a и b
#         по алгоритму Евклида.
#         :param a: первое натуральное число
#         :param b: второе натуральное число
#         :return: НОД
#         """
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#
#     return a
#
#
# def test_nod(funk):
#     # --- тест №1 ------------
#     a = 28
#     b = 35
#     res = funk(a, b)
#     if res == 7:
#         print("#test1 - ok")
#     else:
#         print("#test1 - fail")
#
#     # --- тест №2 ------------
#     a = 100
#     b = 1
#     res = funk(a, b)
#     if res == 1:
#         print("#test2 - ok")
#     else:
#         print("#test2 - fail")
#
#     # --- тест №3 ------------
#     a = 2
#     b = 10000000
#     st = time.time()
#     res = funk(a, b)
#     et = time.time()
#     dt = et - st
#     if res == 2 and dt < 1:
#         print("#test3 - ok")
#     else:
#         print("#test3 - fail")
#
#
# # res = get_nod(18, 24)
# # print(res)
# # help(get_nod)
#
# test_nod(get_nod)


# 2
# def get_nod(a, b):
#     """Вычисляется НОД для натуральных чисел a и b
#         по быстрому алгоритму Евклида.
#         :param a: первое натуральное число
#         :param b: второе натуральное число
#         :return: НОД
#         """
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a % b
#
#     return a
#
#
# test_nod(get_nod)

# Task 1
# def get_rect_value(length, width, tp=0):
#     if tp == 0:
#         return 2 * (length + width) # периметр
#     else:
#         return length * width   # площадь


# Task 2
# def check_password(password, chars="$%!?@#"):
#     if len(password) < 8:
#         return False
#
#     if any(char in password for char in chars):
#         return True
#     else:
#         return False


# Task 3
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# def get_string_value(text, sep = '-'):
#     text = text.lower()
#     result = ''.join(t[char] if char in t else char for char in text)
#     result = result.replace(' ', sep)
#     return result
#
# text = input()
#
# print(get_string_value(text))
# print(get_string_value(text, sep='+'))


# Task 4
def get_string_value(text, tag='h1'):
    result = f"<{tag}>{text}</{tag}>"
    return result


input_text = input()

print(get_string_value(input_text))
print(get_string_value(input_text, tag='div'))
