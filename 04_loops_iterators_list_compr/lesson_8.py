# Task 1
# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# print(*[element for sublist in lst_in for element in sublist][::-1])


# Task 2
# nums = [int(i) for i in input().split()]
# mtrx_size = int(len(nums) ** 0.5)
# mtrx = [[nums[i * mtrx_size + j] for j in range(mtrx_size)] for i in range(mtrx_size)]
# print(mtrx)

#or
# nums = list(map(int, input().split()))
# mtx_size = int(len(nums) ** 0.5)
# it_nums = iter(nums)
# print([[next(it_nums) for _ in range(mtx_size)] for __ in range(mtx_size)])


# Task 3
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

lst = [[word for word in s.split() if len(word) > 3] for s in t]
print(lst)