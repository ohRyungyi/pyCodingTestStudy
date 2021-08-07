import sys

n = int(sys.stdin.readline())

list = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline())
    list[a] += 1

for i in range(10001):
    for j in range(list[i]):
        print(i)

'''
입력 예시
10
10000
2
3
1
4
2
3
5
1
7

출력 예시
1
1
2
2
3
3
4
5
5
7
'''