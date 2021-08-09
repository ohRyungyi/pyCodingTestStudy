import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split('\n')[0].split(' '))

sequence = list(map(int, sys.stdin.readline().split('\n')[0].split(' ')))

answer = 0
for i in range(1, N+1):
    for num in combinations(sequence, i):
        if sum(num) == S:
            answer+=1

print(answer)


'''
입력
5 0
-7 -3 -2 5 8

출력
1
'''