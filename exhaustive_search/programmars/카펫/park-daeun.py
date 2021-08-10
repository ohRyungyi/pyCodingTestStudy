def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i

            if brown == i*2 + j*2 + 4:
                if i >= j:
                    answer = [i + 2, j + 2]
                else:
                    answer = [j + 2, i + 2]

    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))

'''
입력 예시
brown = 10
yellow = 2

brown = 8
yellow = 1

brown = 24
yellow = 24

출력 예시
[4, 3]

[3, 3]

[8, 6]
'''