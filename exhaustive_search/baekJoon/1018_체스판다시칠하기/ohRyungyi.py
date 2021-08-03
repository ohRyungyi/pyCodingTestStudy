import sys

N, M = sys.stdin.readline().split('\n')[0].split(' ')
N = int(N)
M = int(M)

boards = []

for i in range(N):
    # boards.append([])
    # print()
    data = list(map(str, sys.stdin.readline().split('\n')[0]))
    # print(data)
    boards.append(data)
    # boards[i].append(sys.stdin.readline().split('\n')[0])

type1 = list()
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))
type1.append(list(map(str, 'WB'*4)))
type1.append(list(map(str, 'BW'*4)))
# type1 = 'WB'*4+"\n"+'BW'*4+'\n'+'WB'*4+"\n"+'BW'*4+'\n'+'WB'*4+"\n"+'BW'*4+'\n'+'WB'*4+"\n"+'BW'*4
# print('\n'+type1)
# type2 = 'BW'*4+'\n'+'WB'*4+'\n'+'BW'*4+'\n'+'WB'*4+'\n'+'BW'*4+'\n'+'WB'*4+'\n'+'BW'*4+'\n'+'WB'*4
# print('\n'+type2)
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

# def repaint(boards, x, y, N, M, counts) :
#     numw = 0
#     numb = 0
    
#     if (N)-x <8 and (M)-y<8:
#         # print(x, y, counts)
#         return counts
#     elif (M)-y<8:
#         # print(x, y, counts)
#         return repaint(boards, x+1, 0, N, M, counts)
#     elif (N)-x <8:
#         # print(x, y, counts)
#         return repaint(boards, x, y+1, N, M, counts)
#     else:
#         for i in range(x, x+8):
#             for j in range(y, y+8):
#                 if type1[i-x][j-y] != boards[i][j]:
#                     numw+=1
#                 if type2[i-x][j-y] != boards[i][j]:
#                     numb+=1
#         if counts > numw:
#             counts = numw
#         if counts > numb:
#             counts = numb
#         # print(x, y, counts, numw, numb)
#         return repaint(boards, x, y+1, N, M, counts)

# print(repaint(boards, 0, 0, N, M, N*M))

# for i in range(0, N-7):
#     for j in range(0, M-7):
#         print(boards[i][j:j+8])

# print(boards)


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