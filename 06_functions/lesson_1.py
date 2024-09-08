# Task 1
# def send_mail():
#     text = "It's my first function"
#     print(text)
#
#
# send_mail()


# Task 2
# def sent_mail():
#     text = f"Уважаемый, {input()}! Вы верно выполнили это задание!"
#     print(text)
#
#
# sent_mail()


# Task 3
# def sent_mail():
#     text = f"Предмет имеет вес: {input()} кг."
#     print(text)
#
#
# sent_mail()


# Task 4
# def calculate_metrix(x):
#     v_min = min(x)
#     v_max = max(x)
#     v_sum = sum(x)
#     print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")
#
#
# calculate_metrix([int(x) for x in input().split()])


# Task 5
# def entry_parameter(width, height):
#     print(f"Периметр прямоугольника, равен {2 * (width + height)}")
#
#
# width, height = map(int, input().split())
#
# entry_parameter(width, height)


# Task 6
def check_email(email):
    valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_."
    if "@" not in email or "." not in email:
        print("НЕТ")
        return

    for symbol in email:
        if symbol not in valid_characters and symbol != "@":
            print("НЕТ")
            return

    print("ДА")


email = input()
check_email(email)