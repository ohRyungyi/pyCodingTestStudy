import sys

n = int(sys.stdin.readline())
int_list = [0] * 10001

for i in range(n):
    int_list[int(sys.stdin.readline())]+=1

for i in range(10001):
    for j in range(int_list[i]):
        print(i)