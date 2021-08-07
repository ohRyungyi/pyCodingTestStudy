import sys

# N, M = map(int, sys.stdin.readline().split()) # N, M 

# li = list(map(int, sys.stdin.readline().split()))



# ############ 무시한 방법##########
# sum = 0
# candidate = 0
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             sum = li[i] + li[j] + li[k]
#             if sum <= M:
#                 candidate = max (candidate, sum) # 값 비교. -> 작은 값들 중에 큰 값!


# print(candidate)

############ itertools 사용하기!!! ############
from itertools import combinations

N, M = map(int, sys.stdin.readline().split()) # N, M 

li = list(map(int, sys.stdin.readline().split()))

li = list(combinations(li,3))# -> 조합이 모두, 튜플 형식으로 나옴!

candidate = 0
for element in li:
    if sum(element) <= M: #M보다 작거나 같다.
        candidate= max(candidate, sum(element))

print(candidate)


############ 우수코드 ############
# [N,M],c=eval('map(int,input().split()),'*2)
# from itertools import*
# print(max(i for i in map(sum,combinations(c,3))if i<=M)) 