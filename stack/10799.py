import sys
a = sys.stdin.readline().rstrip()

stack = []
ans = 0

for i in a:
    #print(stack, ans)
    if i == '(':
        stack.append(i)
    elif i == ')':
        if stack[len(stack)-1] == '(':
            stack.pop()
            stack.append('1')
        else:
            stack.pop(len(stack)-2)
            ans += int(stack[len(stack)-1]) + 1

    if len(stack) >= 2 and stack[len(stack)-1].isnumeric() == True and stack[len(stack)-2].isnumeric() == True:
        n = int(stack[len(stack)-1]) + int(stack[len(stack)-2])
        stack.pop()
        stack.pop()
        stack.append(str(n))

print(ans)

'''
입력 예시
()(((()())(())()))(())

(((()(()()))(())()))(()())

출력 예시
17

24
'''
