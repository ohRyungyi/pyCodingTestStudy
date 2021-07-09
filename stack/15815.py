import sys
a = sys.stdin.readline().rstrip()
stack = []

ans = 0
for i in a:
    if ord(i) >= 48 and ord(i) <= 57:
        stack.append(int(i))
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b+a)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        else:
            stack.append(b/a)
'''
ans = 0
for i in a:
    if i == '+':
        ans = stack[len(stack)-1] + stack[len(stack)-2]
        stack.pop()
        stack.pop()
        stack.append(ans)
    elif i == '-':
        ans = stack[len(stack)-1] - stack[len(stack)-2]
        stack.pop()
        stack.pop()
        stack.append(ans)
    elif i == '*':
        ans = stack[len(stack)-1] * stack[len(stack)-2]
        stack.pop()
        stack.pop()
        stack.append(ans)
    elif i == '/':
        ans = stack[len(stack)-1] / stack[len(stack)-2]
        stack.pop()
        stack.pop()
        stack.append(ans)
    else:
        stack.append(int(i))
'''

print(int(stack[0]))

'''
입력 예시
163/+

출력 예시
7
'''
