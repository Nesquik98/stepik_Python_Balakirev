# Task 1
# def get_even(*args):
#     return [num for num in args if num % 2 == 0]

# Task 2
def get_biggest_city(*cities):
    biggest_city = ''
    for city in cities:
        if len(city) > len(biggest_city):
            biggest_city = city

    return biggest_city


def get_biggest_city(*cities) -> str:
    return max(cities, key=len)