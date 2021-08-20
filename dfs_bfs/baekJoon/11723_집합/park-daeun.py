import sys

def add(S, x):
    S = S | x
    return S

def remove(S, x):
    S = S & (~x)
    return S

def check(S, x):
    if x == (S & x):
        return 1
    else:
        return 0

def toggle(S, x):
    if check(S, x) == 1:
        S = remove(S, x)
    else:
        S = add(S, x)
    return S

n = int(sys.stdin.readline())
S = 0
#print(1<<4-1)

for i in range(n):
    order = list(sys.stdin.readline().split())

    if order[0] == 'add':
        S = add(S, 1 << int(order[1])-1)
    elif order[0] == 'remove':
        S = remove(S, 1 << int(order[1])-1)
    elif order[0] == 'check':
        print(check(S, 1 << int(order[1])-1))
    elif order[0] == 'toggle':
        S = toggle(S, 1 << int(order[1])-1)
    elif order[0] == 'all':
        S = int('11111111111111111111', 2)
    else:
        S = 0

    #print(S)
    


'''
입력 예시
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

출력 예시
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''