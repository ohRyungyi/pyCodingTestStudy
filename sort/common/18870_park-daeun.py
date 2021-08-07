import sys

n = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
set_X = set(X)
dX = dict(zip(sorted(list(set_X)), range(len(set_X))))
#print(dX)

for x in X:
    print(dX.get(x), end = ' ')

'''
입력 예시
5
2 4 -10 4 -9

6
1000 999 1000 999 1000 999

출력 예시
2 3 0 3 1

1 0 1 0 1 0
'''