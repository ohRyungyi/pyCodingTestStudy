import sys

# n: 총 게임 횟수
# p: 해킹을 통해 얻은 플레이어 정보의 수
n, p = map(int, sys.stdin.readline().split())

# w: 이긴 경우 획득 점수
# l: 졌을 때 떨어지는 점수
# g: IRON 티어 벗어나기 위한 점수
w, l, g = map(int, sys.stdin.readline().split())

# 해킹한 선수, 이기는지(W) or 지는지(L) 딕셔너리에 받기
hacked_player = {}
for i in range(p):
    name, t = sys.stdin.readline().split()
    hacked_player[name] = t

# 같이 게임하는 플레이어 이름 받아서 점수 계산하기
point = 0
for j in range(n):
    name = sys.stdin.readline().rstrip()

    if hacked_player.get(name) == 'W':  # 해킹을 해서 무조건 이길 수 있는 확률
        point += w
    else:  # 해킹을 했는데 지는 선수이거나, 해킹 정보가 없는 선수
        point -= l
        if point < 0:  # 점수는 절대 0점 밑으로 떨어지지 않음
            point = 0

    if point >= g:  # 점수가 IRON 티어 벗어나기 위한 점수를 넘겼을 때
        print("I AM NOT IRONMAN!!")
        quit()  # 프로그램 종료

print("I AM IRONMAN!!")

'''
입력 예시
10 3
20 15 100
JIHOON W
GANGYEOP L
MINSUNG L
JIHOON
MYEONGKI
GANGYEOP
MINSUNG
JIHOON
JIHOON
JIHOON
JIHOON
JIHOON
MINSUNG

10 3
20 15 100
JIHOON W
GANGYEOP L
MINSUNG L
JIHOON
GANGYEOP
JISUP
MINSUNG
JIHOON
JIHOON
MOJI
KYUNGMIN
SOOHO
SEOKGYE

출력 예시
I AM NOT IRONMAN!!

I AM IRONMAN!!
'''
