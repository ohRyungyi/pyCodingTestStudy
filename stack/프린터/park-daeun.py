def solution(priorities, location):
    papers = [i for i in range(len(priorities))]

    prints = []

    while True:
        j = priorities[0]
        k = papers[0]

        if max(priorities) > j:
            priorities.remove(j)
            priorities.append(j)

            papers.remove(k)
            papers.append(k)

        else:
            prints.append(k)
            priorities.remove(j)
            papers.remove(k)

            if k == location:
                break

    answer = prints.index(location)+1
    return answer


priorities = [2, 1, 3, 2]
location = 2

res = solution(priorities, location)
print(res)

'''
입력 예시
priorities = [2, 1, 3, 2]
location = 2

priorities = [1, 1, 9, 1, 1, 1]
location = 0

출력 예시
1

5
'''
