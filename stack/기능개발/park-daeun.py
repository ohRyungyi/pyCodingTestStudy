import math


def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        day = math.ceil((100-p)/s)
        days.append(day)

    first = days[0]
    num = 0

    answer = []
    for i in range(len(days)):
        if days[i] <= first:
            num += 1
        else:
            answer.append(num)
            num = 1
            first = days[i]

        if i == len(days)-1:
            answer.append(num)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))

'''
입력 예시
progresses = [93, 30, 55]
speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

출력 예시
[2, 1]

[1, 3, 2]
'''
