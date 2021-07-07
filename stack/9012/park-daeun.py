import sys

n = int(sys.stdin.readline())

for i in range(n):
    case = sys.stdin.readline().rstrip()

    num = 0
    error = 0
    stack = []
    for c in case:
        if c == '(':
            stack.append('0')
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                error = 1

    if len(stack) == 0 and error == 0:
        print("YES")
    else:
        print("NO")

'''
입력 예시
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

3
((
))
())(()

출력 예시
NO
NO
YES
NO
YES
NO

NO
NO
NO
'''
