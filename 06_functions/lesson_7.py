# Task 1
# def counter_add():
#     def inner(num: int) -> int:
#         return num + 5
#
#     return inner
#
#
# cnt = counter_add()
# print(cnt(k := int(input())))


# Task 2
# def counter_add(n):
#     def inner(num: int) -> int:
#         return num + n
#     return inner
#
#
# cnt = counter_add(2)
# k = int(input())
#
# result = cnt(k)
# print(result)


# Task 3
# def close_function():
#     def inner_function(s):
#         return f"<h1>{s}</h1>"
#     return inner_function
#
#
# input_string = input()
# function_reference = close_function()
# result = function_reference(input_string)
# print(result)


# Task 4
# def close_function(tag):
#     def inner_function(content):
#         return f"<{tag}>{content}</{tag}>"
#     return inner_function
#
#
# input_tag = input()
# input_content = input()
#
# function_reference = close_function(input_tag)
# result = function_reference(input_content)
# print(result)
