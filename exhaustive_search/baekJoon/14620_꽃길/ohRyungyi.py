import sys

N = int(sys.stdin.readline())

gardens = list()
isAble = list()

for i in range( N):
    gardens.append(list(map(int, sys.stdin.readline().split('\n')[0].split(' '))))
    isAble.append([True]*N)

ans = []

def brute(isAble, cnt, ans, cost):
    if (cnt) == 3:
        ans.append(cost)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if isAble[i][j] == True and isAble[i-1][j] == True and isAble[i+1][j] == True and isAble[i][j-1] == True and isAble[i][j+1] == True:
                    isAble[i][j] = False
                    isAble[i-1][j] = False
                    isAble[i+1][j] = False
                    isAble[i][j-1] = False
                    isAble[i][j+1] = False
                    brute(isAble, cnt+1, ans, cost+gardens[i][j]+gardens[i-1][j]+gardens[i+1][j]+gardens[i][j+1]+gardens[i][j-1] )
                    isAble[i][j] = True
                    isAble[i-1][j] = True
                    isAble[i+1][j] = True
                    isAble[i][j-1] = True
                    isAble[i][j+1] = True

brute(isAble, 0, ans, 0)
print(sorted(ans)[0])
'''
입력
6
1 0 2 3 3 4
1 1 1 1 1 1
0 0 1 1 1 1
3 9 9 0 1 99
9 11 3 1 0 3
12 3 0 0 0 1

출력
12
'''