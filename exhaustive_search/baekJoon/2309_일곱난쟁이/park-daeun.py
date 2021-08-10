import sys
from itertools import combinations

arr = [int(sys.stdin.readline()) for _ in range(9)]
com_arr = list(combinations(arr, 7))

print(com_arr)

for com in com_arr:
    if sum(com) <= 100:
        a = sorted(com)
        for c in a:
            print(c)
        break

'''
입력 예시
20
7
23
19
10
15
25
8
13

출력 예시
7
8
10
13
19
20
23
'''