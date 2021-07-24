import sys
import itertools  # 조합

# n: 해전의 개수
n = int(sys.stdin.readline())

# 해전 순서의 정답
wars_correct = dict(zip(sys.stdin.readline().split(), [i for i in range(n)]))

# 학생의 답안
wars_answer = sys.stdin.readline().split()

# 학생의 답안 중 N(N-1)/2개의 쌍 고름
pick = list(itertools.combinations(wars_answer, 2))
''' >>> 출력: [('sacheon', 'hansan'), ('sacheon', 'myeongnyang'), ('sacheon', 'noryang'), ('sacheon', 'okpo'), ('hansan', 'myeongnyang'),
 ('hansan', 'noryang'), ('hansan', 'okpo'), ('myeongnyang', 'noryang'), ('myeongnyang', 'okpo'), ('noryang', 'okpo')]
'''
point = 0  # 학생의 점수
# N(N-1)/2개의 쌍 중에서 해전이 일어난 연도의 순서를 맞게 적었다면 +1점
for p in pick:
    if wars_correct.get(p[0]) < wars_correct.get(p[1]):
        point += 1

# 학생 점수/총 점수
print("%d/%d" % (point, n*(n-1)/2))

'''
입력 예시
5
okpo sacheon hansan myeongnyang noryang
sacheon hansan myeongnyang noryang okpo

3
alpha beta gamma
alpha gamma beta

5
naboo geonosis yavin hoth endor
geonosis yavin hoth endor naboo

출력 예시
6/10

2/3

6/10
'''
