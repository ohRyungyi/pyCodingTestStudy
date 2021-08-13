import sys

n = int(sys.stdin.readline())
k = sys.stdin.readline().rstrip()
print(k)

cnt = 0
for i in k:
    if i == '1':
        cnt += 1

print(cnt)

# n = int(sys.stdin.readline())
# k = int(sys.stdin.readline(), 2)

# cnt = 0
# while k != 0:
#     k = k-(k&((~k)+1))
#     cnt += 1

# print(cnt)

'''
입력 예시
5
10110

출력 예시
3
'''