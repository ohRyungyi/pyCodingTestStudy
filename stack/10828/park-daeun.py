import sys

n = int(sys.stdin.readline())
st = []


def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False


for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order == 'pop':
        if isEmpty(st):
            print('-1')
        else:
            print(st.pop())

    elif order == 'size':
        print(len(st))

    elif order == 'empty':
        if isEmpty(st):
            print('1')
        else:
            print('0')

    elif order == 'top':
        if isEmpty(st):
            print('-1')
        else:
            print(st[len(st)-1])

    else:
        order = order.split()
        st.append(int(order[1]))

'''
입력 예시
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

7
pop
top
push 123
top
pop
top
pop

출력 예시
2
2
0
2
1
-1
0
1
-1
0
3

-1
-1
123
123
-1
-1
'''
