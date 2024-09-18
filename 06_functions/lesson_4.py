# Task 1
# def get_even(*args):
#     return [num for num in args if num % 2 == 0]

# Task 2
# def get_biggest_city(*cities):
#     biggest_city = ''
#     for city in cities:
#         if len(city) > len(biggest_city):
#             biggest_city = city
#
#     return biggest_city
#
#
# def get_biggest_city(*cities) -> str:
#     return max(cities, key=len)

# Task 3
def get_data_fig(*args, **kwargs):
    perimetr = sum(args)
    result = (perimetr,)

    if 'tp' in kwargs:
        result += (kwargs['tp'],)
    if 'color' in kwargs:
        result += (kwargs['color'],)
    if 'closed' in kwargs:
        result += (kwargs['closed'],)
    if 'width' in kwargs:
        result += (kwargs['width'],)

    return result
