import sys

n = int(sys.stdin.readline())

for i in range(n):
    sn = list(str(i))
    n_list = list(map(int, sn))

    if n == i + sum(n_list):
        print(i)
        quit()

print(0)

'''
입력 예시
216

출력 예시
198
'''