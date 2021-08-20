import sys

X = int(sys.stdin.readline())
stick = [64]

while sum(stick) != X:
    v = min(stick)
    stick.remove(v)

    half = v // 2

    if sum(stick) + half >= X:
        stick.append(half)
    else:
        stick.append(half)
        stick.append(half)

print(len(stick))

'''
입력 예시
23

32

64

48

출력 예시
4

1

1

2
'''