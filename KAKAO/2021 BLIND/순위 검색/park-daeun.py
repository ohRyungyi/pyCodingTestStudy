from itertools import combinations # 조건 조합

def binary_search(arr, start, end, target): # target이 점수 arr에 들어갈 index 찾음
    if target > arr[end]: # ex: arr = [0, 50, 100], target = 300이면 target의 index는 end+1
        return end+1

    while start <= end:
        mid = (start + end) // 2

        if (arr[mid] >= target > arr[mid-1]): # ex. arr = [50, 80, 150, 150, 260], target = 150이면 충족하는 score의 수는 3임.
            break
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    
    return mid

def solution(info, query):
    answer = []

    info_dict = dict() # 조건의 조합:점수를 딕셔너리에 저장

    # info를 하나씩 보며 딕셔너리에 저장
    for i in range(len(info)):
        info[i] = info[i].split(' ') # "java backend junior pizza 150" -> [java, backend, junior, pizza, 150]

        f = info[i][:-1] # [java, backend, junior, pizza] (조건)
        score = int(info[i][-1]) # 150 (점수)

        arr = list(f) # arr = [java, backend, junior, pizza]
        arr.extend(list(combinations(f, 2))) # arr = [java, backend, junior, pizza, (java, backend), (java, junior), ...]
        arr.extend(list(combinations(f, 3))) # arr = [java, backend, ..., (java, backend), ..., (java, backend, junior), (java, backend, pizza), ...]
        arr.append(tuple(f)) # arr = [java, backend, ..., (java, backend), ..., (java, backend, junior), ..., (java, backend, junior, pizza)]

        if 'all' in info_dict: # 조건이 "- and - and - and -"일 때 사용할 key
            info_dict['all'].append(score)
        else:
            info_dict['all'] = [score]

        for a in arr: # 모든 조건의 조합에 점수를 value로 추가
            if a in info_dict:
                info_dict[a].append(score)
            else:
                info_dict[a] = [score]
    # print(info_dict) # {'all': [150, 0, 100, 260, 80, 50], 'java': [150, 80], 'backend': [150, 260, 80, 50], ...}
    
    # 이진 탐색을 이용하기 위해 딕셔너리의 value를 정렬한 값으로 업데이트
    for b in info_dict.items():
        so = info_dict.get(b[0])
        info_dict[b[0]] = sorted(so)

    # query를 하나씩 보며 해당하는 지원자의 수를 answer에 저장
    for j in range(len(query)):
        query[j] = query[j].replace('and ', '') # cpp and - and senior and pizza 300 -> cpp - senior pizza 300
        query[j] = query[j].split(' ') # cpp - senior pizza 300 -> ['cpp', '-', 'senior', 'pizza', '300']
        
        x = query[j][:-1] # ['cpp', '-', 'senior', 'pizza'] (조건)
        s = int(query[j][-1]) # 300 (점수)
        
        # '-' 제거
        while x and x.count('-') > 0:
            x.remove('-')

        cnt = 0 # 해당하는 지원자의 수
        if not x: # x가 []일 때 (-, -, -, - 이었다가 제거된 리스트)
            a = info_dict.get('all') # 딕셔너리 value
            cnt = len(a) - binary_search(a, 0, len(a)-1, s) # a의 총 길이에서 이진탐색을 통해 찾은 위치 빼주기(크거나 같은 점수의 개수)

        elif tuple(x) in info_dict: # ex ['cpp', 'senior', 'pizza'] -> ('cpp', 'senior', 'pizza')가 딕셔너리에 있을 때
            a = info_dict.get(tuple(x))
            cnt = len(a) - binary_search(a, 0, len(a)-1, s)

        elif len(x) == 1 and (x[0] in info_dict): # ex ['cpp'] -> 'cpp'가 딕셔너리에 있을 때
            a = info_dict.get(x[0])
            cnt = len(a) - binary_search(a, 0, len(a)-1, s)

        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 0",
        "python frontend senior chicken 100",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 0",
        "cpp and - and senior and pizza 300",
        "- and backend and senior and - 51",
        "- and - and - and chicken 100",
        "- and - and - and - 260",
        "java and frontend and junior and pizza 100",
        "python and - and - and - 30"]

print(solution(info, query))