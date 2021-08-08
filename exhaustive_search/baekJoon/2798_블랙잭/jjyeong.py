import sys


# ############ 무식한 방법##########
# N, M = map(int, sys.stdin.readline().split()) # N, M 
# li = list(map(int, sys.stdin.readline().split()))

# sum = 0
# candidate = 0
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             sum = li[i] + li[j] + li[k]
#             if sum <= M:
#                 candidate = max (candidate, sum) # 값 비교. -> 작은 값들 중에 큰 값!


#print(candidate)

############ itertools 사용하기!!! ############
from itertools import combinations

N, M = map(int, sys.stdin.readline().split()) # N, M 

li = list(map(int, sys.stdin.readline().split()))

candidate = 0
for combi in combinations(li,3):
    #print(combi)
    if sum(combi) <= M:
        candidate= max(candidate, sum(combi))

print(candidate)


############ 우수코드 ############
# [N,M],c=eval('map(int,input().split()),'*2)
# from itertools import*
# print(max(i for i in map(sum,combinations(c,3))if i<=M)) 