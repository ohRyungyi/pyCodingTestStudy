import sys

n, m = map(int, sys.stdin.readline().split())
chess = []

for i in range(n):
    line = list(sys.stdin.readline().rstrip())
    chess.append(line)

min_cnt = 100

for k in range(n-8+1):
    for l in range(m-8+1):
        # start : W
        cnt = 0
        for i in range(k, k+8):
            for j in range(l, l+8):
                if i%2 == 0:
                    if j%2 == 0:
                        if chess[i][j] == 'B':
                            cnt += 1
                    else:
                        if chess[i][j] == 'W':
                            cnt += 1
                else:
                    if j%2 == 0:
                        if chess[i][j] == 'W':
                            cnt += 1
                    else:
                        if chess[i][j] == 'B':
                            cnt += 1
        min_cnt = min(min_cnt, cnt)

        # start : B
        cnt = 0
        for i in range(k, k+8):
            for j in range(l, l+8):
                if i%2 == 0:
                    if j%2 == 0:
                        if chess[i][j] == 'W':
                            cnt += 1
                    else:
                        if chess[i][j] == 'B':
                            cnt += 1
                else:
                    if j%2 == 0:
                        if chess[i][j] == 'B':
                            cnt += 1
                    else:
                        if chess[i][j] == 'W':
                            cnt += 1
        min_cnt = min(min_cnt, cnt)

print(min_cnt)

'''
입력 예시
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

출력 예시
1

12
'''