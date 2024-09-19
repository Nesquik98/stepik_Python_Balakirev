# Task 1
# def get_rec_N(n):
#     if n > 0:
#         get_rec_N(n - 1)
#         print(n)
#
#
# N = int(input())
# get_rec_N(N)

# Task 2
def get_rec_sum(nums: list[int]) -> int:
    if not nums:
        return 0
    nums[1] += nums[0]
    return get_rec_sum(nums[1:])


nums = list(map(int, input().split()))
print(get_rec_sum(nums))