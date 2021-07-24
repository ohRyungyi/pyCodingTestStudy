def solution(pb):
    pb.sort(key=len) # 전화번호 길이 순서대로 정렬
    dic = {}
    Len_se = []
    result = True
    
    for i in pb:
        dic[hash(i)] = i # 각 전화번호 hash함수 이용해 dic으로 저장
        Len_se.append(len(i))
    Len = list(set(Len_se)) # Len: 전화번호 길이를 모아놓은 list ex)["12","123","1235","567","88"] => Len = [2,3,4]
    
    for i in pb:
        for j in Len:
            if (len(i) > j): # 전화번호i의 길이가 Len의 원소보다 길때만 검사
                if dic.get(hash(i[0:j])) != None: # hash(전화번호 i의 "Len원소"번째 까지)값이 dic에 존재하면 -> 접두어 존재
                    result = False
                    return result

    return result