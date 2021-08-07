import sys

N, M = sys.stdin.readline().split('\n')[0].split(' ')
N = int(N)
M = int(M)

boards = []

for i in range(N):
    data = list(map(str, sys.stdin.readline().split('\n')[0]))
    boards.append(data)
    

type1 = list()
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))

type2 = list()
type2.append(list(map(str, 'BW'*4)))
type2.append(list(map(str, 'WB'*4)))
type2.append(list(map(str, 'BW'*4)))
type2.append(list(map(str, 'WB'*4)))
type2.append(list(map(str, 'BW'*4)))
type2.append(list(map(str, 'WB'*4)))
type2.append(list(map(str, 'BW'*4)))
type2.append(list(map(str, 'WB'*4)))

counts = 64
num1 = 0
num2 = 0

for i in range(N):
    for j in range(M):
        if N-i < 8 and M-j<8:
            print(counts)
        elif M-j<8:
            break
        elif N-i<8:
            # M-j<8
            break
        else:
            num1 = 0
            num2 = 0
            for n in range(i, i+8):
                for m in range(j, j+8):
                    if type1[n-i][m-j] != boards[n][m]:
                        num1+=1
                    if type2[n-i][m-j] != boards[n][m]:
                        num2+=1
            if counts > num1:
                counts = num1
            if counts > num2:
                counts = num2
print(counts)

'''
입력
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

출력
1

입력
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

출력
12
'''