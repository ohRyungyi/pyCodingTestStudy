import sys

while True:
    case = sys.stdin.readline().rstrip()

    if case == '.':
        break

    stack = []
    error = 0

    for c in case:
        if c == '(' or c == ')' or c == '[' or c == ']':
            if c == '(' or c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) != 0 and stack[len(stack)-1] == '(':
                    stack.pop()
                else:
                    error = 1
            elif c == ']':
                if len(stack) != 0 and stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    error = 1

    if len(stack) == 0 and error == 0:
        print("yes")
    else:
        print("no")

'''
입력 예시
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

출력 예시
yes
yes
no
no
no
yes
yes
'''
