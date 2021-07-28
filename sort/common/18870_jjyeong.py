import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split())) # [2, 4, -10, 4, -9]
sorted_li = sorted(set(li)) #sorted({2,4,-10,-9}) -> [-10,-9,2,4]

sorted_hash={sorted_li[i]:i for i in range(len(sorted_li))}
print(*[sorted_hash[i] for i in li])