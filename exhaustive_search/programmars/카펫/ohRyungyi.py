def solution(brown, yellow):
    answer = []

    for i in range(brown+yellow-1, 2, -1):
        row = i
        col = (brown+yellow)//i
        if (brown+yellow) % i  == 0 and row >= col:

            if (row-2)*(col-2) == yellow:
                # answer.append([row, col])
                answer = [row, col]

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))