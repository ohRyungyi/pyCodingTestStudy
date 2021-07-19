import sys

# n: 도감에 등록된 포켓몬 개수
# m: 맞춰야 하는 문제 개수
n, m = map(int, sys.stdin.readline().split())

pocketmons_keyname = {}
pocketmons_keynum = {}

# 도감에 포켓몬 등록하기
for i in range(n):
    pocketmon = sys.stdin.readline().rstrip()  # 입력된 포켓몬
    pocketmons_keyname[pocketmon] = i+1
    pocketmons_keynum[i+1] = pocketmon

# 문제 맞추기
for j in range(m):
    question = sys.stdin.readline().rstrip()  # 포켓몬 맞추는 문제

    # 도감에서 포켓몬 불러오기
    if question.isnumeric() == True:
        print(pocketmons_keynum.get(int(question)))
    else:
        print(pocketmons_keyname.get(question))

'''
입력 예시
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

출력 예시
Pikachu
26
Venusaur
16
14
'''
