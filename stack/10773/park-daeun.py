import sys

n = int(sys.stdin.readline())
nums = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))

'''
입력 예시
4
3
0
4
0

10
1
3
5
4
0
0
7
0
0
6

출력 예시
0

7
'''
