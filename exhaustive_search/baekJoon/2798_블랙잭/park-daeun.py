import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

three_cards = list(combinations(cards, 3))
print(three_cards)

ans = 0
for c in three_cards:
    if sum(c) == m:
        ans = m
        break
    elif sum(c) > m:
        continue
    else:
        if ans < sum(c):
            ans = sum(c)

print(ans)

'''
입력 예시
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295

출력 예시
21

497
'''