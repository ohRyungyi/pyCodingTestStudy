from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        combi = dict() # 조합이 몇개나왔는지 갱신하는 딕셔너리

        for o in orders:
            o = sorted(list(o)) # x,y,w / w,x,y 동일하게 처리하기 위해 정렬
            now = list(combinations(o, c)) # c개로 만들 수 있는 조합 구하기

            for n in now:
                if n in combi: # 조합이 이미 딕셔너리에 있다면
                    combi[n] += 1 # 개수 갱신
                else: # 없다면 추가해주기
                    combi[n] = 1
        
        item = list(combi.items()) # 딕셔너리의 key:value를 리스트로 만들기
        item.sort(key = lambda x : -x[1]) # value값(몇개인지)으로 내림차순 정렬

        if len(item) == 0 or item[0][1] == 1: # 조합이 없거나, 1명의 손님 조합만 있다면
            continue

        max = item[0][1] # 내림차순으로 정렬했으므로 item[0][1]이 조합 개수의 최댓값
        for i in item:
            if i[1] != max: # max가 아니라면 이후로는 다 더 작으므로 멈춤
                break
            answer.append(''.join(i[0])) # 문자열로 만들어 answer리스트에 추가

    answer.sort() # 사전순으로 리턴하기 위해 정렬
    return answer