n, m = input().split(' ') # 그룹 수, 문제 수를 각각 n, m 변수에 저장
n = int(n) # 문자열을 정수로 변환
m = int(m) # 문자열을 정수로 변환
hash_map_mem = {} # key를 멤버 이름으로 하고 value를 해당 멤버가 속한 그룹의 이름으로 설정한 해시 테이블
hash_map_team = {} # key를 팀 이름으로 하고 value를 해당 그룹들의 모든 멤버들의 리스트로 저장하는 해시 테이블
for i in range(n): # n 개의 그룹에 대해서 해시 테이블 값을 채우기 위해서 반복문 수행
    team = input()  # 팀 이름을 team 변수에 저장
    num = int(input()) # 해당 팀의 멤버수를 num 변수에 저장
    mems = list() # 모든 멤버들을 저장할 리스트 변수 mems 정의
    for j in range(num): # num개의 멤버 수에 대해서 반복문 수행
        mem = input() # 멤버 이름을 mem 변수에 저장
        hash_map_mem[mem] = team # 멤버 이름을 key로 팀 이름을 value로 해시 테이블에 저장
        mems.append(mem) # 멤버들 이름 리스트에 멤버 이름을 추가
    
    mems.sort() # 멤버 이름을 사전순으로 정렬
    
    hash_map_team[team] = mems # key를 팀 이름으로 value를 멤버들 이름 리스트로 해시 테이블에 데이터 추가

for i in range(m): # m개의 문제에 대해 반복문 수행
    quest = input() # 팀 이름 또는 멤버 이름을 quest 변수에 저장
    qType = int(input()) # 0의 값이면 팀 이름이 quest 변수에 저장, 1의 값이면 멤버 이름이 quest 변수에 저장

    if qType == 1:
        # 멤버가 속한 팀의 이름 출력
        print(hash_map_mem[quest]) # key가 멤버 이름인 해시 테이블에 대해서 value값 출력
    else : 
        # 팀에 속한 멤버들의 이름으르 출력
        for i in hash_map_team[quest]: # key가 팀 이름인 해시 테이블에 대해서 value값인 해당 팀의 멤버들의 리스트를 출력하기 위해 반복문 수행
            print(i)
