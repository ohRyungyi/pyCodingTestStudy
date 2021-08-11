import sys

N = int(sys.stdin.readline())

# key = data, value = repeat
ind = [0]*21

def add(ind, x):
    ind[x] +=1

def remove(ind, x):
    if ind[x] != 0:
        ind[x] -= 1

def check(ind, x):
    if ind[x] >=1:
        print(1)
    else:
        print(0)

def toggle(ind, x):
    if ind[x] == 0:
        ind[x] += 1
    else:
        ind[x] -= 1

def all(ind):
    for i in range(0, 21):
        ind[i] = 1

def empty(ind) :
    for i in range(0, 21):
        ind[i] = 0



for i in range(N):
    commands = sys.stdin.readline().split('\n')[0].split(' ')

    if len(commands) == 1:
        # all , empty
        if commands[0] == 'all':
            all(ind)
        else:
            empty(ind)
    else:
        command = commands[0]
        data = int(commands[1])

        if command == 'add':
            add(ind, data)
        elif command == 'remove':
            remove(ind, data)
        elif command == 'check':
            check(ind, data)
        else:
            toggle(ind, data)


'''
입력
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

출력
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