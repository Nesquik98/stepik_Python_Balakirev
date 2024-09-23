# get_sq = lambda x: x ** 2

# get_div = lambda x, y: None if y == 0 else x / y

# print((lambda x: x if x >= 0 else -x)(float(input())))

# check_ra = lambda string: 'ra' in string
# string = input()
# print(check_ra(string))
#
# print((lambda string: True if 'ra' in string else False)(input()))

# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
#
# digs = list(map(int, input().split()))
#
# all_value = filter_lst(digs)
# print(*all_value)
#
# negative_value = filter_lst(digs, key=lambda x: x < 0)
# print(*negative_value)
#
# nonnegative_value = filter_lst(digs, key=lambda x: x >= 0)
# print(*nonnegative_value)
#
# range_value = filter_lst(digs, key=lambda x: 3 <= x <= 5)
# print(*range_value)