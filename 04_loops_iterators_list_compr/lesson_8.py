# Task 1
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

print(*[element for sublist in lst_in for element in sublist][::-1])
