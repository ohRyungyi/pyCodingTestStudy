import sys

n = int(sys.stdin.readline())
inputs = [int(sys.stdin.readline()) for i in range(n)]

plus = 0
minus = 0

stack = []
pm = []

i = 1
j = 0

sum = 0
error = 0
while j < n:
    stack.append(i)
    plus += 1
    pm.append('+')

    if inputs[j] < stack[len(stack)-1]:
        error = 1
        break

    while j < n and len(stack) > 0 and stack[len(stack)-1] == inputs[j]:
        stack.pop()
        minus += 1
        pm.append('-')

        j += 1

    i += 1

if error == 1:
    print('NO')
else:
    for s in pm:
        print(s)

'''
입력 예시
8
4
3
6
8
7
5
2
1

5
1
2
5
3
4

출력 예시
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

NO
'''
