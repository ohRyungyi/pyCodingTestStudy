import sys

n = int(sys.stdin.readline())
list = (int(sys.stdin.readline()) for i in range(n))

print(*sorted(list), sep = '\n')

'''
입력 예시
5
5
4
3
2
1

출력 예시
1
2
3
4
5
'''