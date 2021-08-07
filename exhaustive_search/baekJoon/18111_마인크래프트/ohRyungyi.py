import sys
from collections import Counter

N, M, B = sys.stdin.readline().split('\n')[0].split(' ')
N = int(N)
M = int(M)
B = int(B)

maps = list()

for i in range(N):
    data = list(map(int, sys.stdin.readline().split('\n')[0].split(' ')))
    maps += data

# 모든 블록의 갯수 저장
tot_blocks = sum(maps)

heights = Counter(maps)
# print(min(heights), max(heights))

result = [500*500*256, 0]

for h in range(max(heights), min(heights)-1, -1):
    test = [0, h]

    temp = (tot_blocks+B) - (h*N*M)

    if temp >= 0:
        for height, count in heights.items():
            if height > h:
                test[0]+=(height-h)*2*count
            elif height < h:
                test[0]+=(h-height)*count
        
        if test[0] < result[0]:
            result[0] = test[0]
            result[1] = test[1]



print(result[0], result[1])

'''
입력
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

출력
2 0

입력
3 4 1
64 64 64 64
64 64 64 64
64 64 64 63

출력
1 64

입력
3 4 0
64 64 64 64
64 64 64 64
64 64 64 63

출력
22 63
'''