import sys

N, M = sys.stdin.readline().split('\n')[0].split(' ')
N = int(N)
M = int(M)

cards_list = [int(n) for n in sys.stdin.readline().split('\n')[0].split(' ')]

max = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            data = cards_list[i]+cards_list[j]+cards_list[k]
            if data <= M:
                if data > max:
                    max = data

print(max) 
'''
입력
5 21
5 6 7 8 9

출력
21

입력
10 500
93 181 245 214 315 36 185 138 216 295

출력
497
'''