import sys
n, m = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split())) #items = [2, 1, 3]
from itertools import combinations
com = list(combinations(items, 3)) #com = [(2,1), (2,3), (1,3)]
com_sum = list(map(sum,com)) #com_sum = [3, 5, 4]
com_sum.sort(reverse = True) #com_sum = [3, 4, 5]
for i in com_sum:
    if i <= m:
        print(i)
        break;