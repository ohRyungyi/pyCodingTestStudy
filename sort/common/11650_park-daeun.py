import sys

n = int(sys.stdin.readline())

xy = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy.append((x,y))

xy.sort(key = lambda x : (x[0], x[1]))

for p in xy:
    print(p[0], p[1])

'''
입력 예시
5
3 4
1 1
1 -1
2 2
3 3

출력 예시
1 -1
1 1
2 2
3 3
3 4
'''