import sys

N = int(sys.stdin.readline())

s_p_info = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]

print(s_p_info)

answer = []
for student in s_p_info:
    count = 1
    for i in range(N):
        if student[0] < s_p_info[i][0] and student[1] < s_p_info[i][1]:
            count += 1
    answer.append(count)

print(*answer, sep=' ')