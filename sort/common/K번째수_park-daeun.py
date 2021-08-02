def solution(array, commands):
    answer = []

    for c in commands:
        a = array[c[0]-1:c[1]]
        a.sort()
        answer.append(a[c[2]-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))

'''
입력 예시
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

출력 예시
[5, 6, 3]
'''