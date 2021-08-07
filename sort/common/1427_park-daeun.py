import sys

n = sys.stdin.readline().rstrip()

n = list(n)
n.sort(reverse=True)
print(*n, sep='')

'''
입력 예시
2143

출력 예시
4321
'''