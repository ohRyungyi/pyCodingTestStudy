import sys

N = int(sys.stdin.readline())

s_p_info = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]

print(s_p_info)

answer = []
for student in s_p_info: # student => (몸무게,키)
    #count = 0
    count = 1
    for the_other_student in s_p_info:
        if student[0] < the_other_student[0] and student[1] < the_other_student[1]:
            count += 1
    answer.append(count)

print(*answer, sep=' ')

'''
5
55 185
58 183
88 186
60 175
46 155
'''

'''2 2 1 2 5'''