import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for a in arr:
    print(a)

'''
입력 예시
5
5
2
3
4
1

출력 예시
1
2
3
4
5
'''
