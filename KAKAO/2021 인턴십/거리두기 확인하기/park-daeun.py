# def solution(places):
#     answer = []
#     return answer

def solution(places):
    answer = []

    move_case1 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    move_case2 = [(-2, 0), (2, 0), (0, 2), (0, -2)]
    move_case3 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for place in places:
        ans = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    print(i, j)
                    for m1 in move_case1:
                        if i + m1[0] >= 0 and i + m1[0] <= 4 and j + m1[1] >= 0 and j + m1[1] <= 4:
                            if place[i + m1[0]][j + m1[1]] == 'P':
                                ans = 0
                                break
                    
                    for m2 in move_case2:
                        if i + m2[0] >= 0 and i + m2[0] <= 4 and j + m2[1] >= 0 and j + m2[1] <= 4:
                            if m2[0] == -2:
                                if place[i - 1][j] != 'X' and place[i - 2][j] == 'P':
                                    ans = 0
                                    break
                            elif m2[0] == 2:
                                if place[i + 1][j] != 'X' and place[i + 2][j] == 'P':
                                    ans = 0
                                    break
                            elif m2[1] == -2:
                                if place[i][j - 1] != 'X' and place[i][j - 2] == 'P':
                                    ans = 0
                                    break
                            else:
                                if place[i][j + 1] != 'X' and place[i][j + 2] == 'P':
                                    ans = 0
                                    break
                    
                    for m3 in move_case3:
                        if i + m3[0] >= 0 and i + m3[0] <= 4 and j + m3[1] >= 0 and j + m3[1] <= 4:
                            if m3[0] == -1 and m3[1] == -1:
                                if (place[i - 1][j] != 'X' or place[i][j - 1] != 'X') and place[i-1][j-1] == 'P':
                                    ans = 0
                                    break
                            elif m3[0] == -1 and m3[1] == 1:
                                if (place[i - 1][j] != 'X' or place[i][j + 1] != 'X') and place[i-1][j+1] == 'P':
                                    ans = 0
                                    break
                            elif m3[0] == 1 and m3[1] == -1:
                                if (place[i + 1][j] != 'X' or place[i][j - 1] != 'X') and place[i+1][j-1] == 'P':
                                    ans = 0
                                    break
                            else:
                                if (place[i + 1][j] != 'X' or place[i][j + 1] != 'X') and place[i+1][j+1] == 'P':
                                    ans = 0
                                    break
        
        if ans == 0:
            answer.append(0)
        else:
            answer.append(1)

    return answer

# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.
# 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.

# place = ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
# print(solution(place))

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],  
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))