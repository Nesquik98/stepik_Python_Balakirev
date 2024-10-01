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
def string_to_list(s1, s2):
    list1 = s1.split()
    list2 = s2.split()
    return list1, list2


def lists_to_dict_decorator(func):
    def wrapper(s1, s2):
        list1, list2 = func(s1, s2)
        return dict(zip(list1, list2))
    return wrapper


@lists_to_dict_decorator
def strings_to_list(s1, s2):
    list1 = s1.split()
    list2 = s2.split()
    return list1, list2


s1, s2 = input(), input()
d = strings_to_list(s1, s2)

print(*sorted(d.items()))