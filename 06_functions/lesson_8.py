# Task 1
def func_show(func):
    def wrapper(width, height):
        p = func(width, height)
        print(f"Площадь прямоугольника: {p}")
        return p
    return wrapper


def get_sq(width, height):
    return width * height
