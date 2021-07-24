def solution(participant, completion):
    answer = ''
    p_dic = {}
    c_dic = {}
    for i in completion: #completion을 dic으로 변환
        c_dic[i] = 0
    for i in completion: #두 번 for문으로 굳이 처음에 0을 넣고 이후에 +1하는 이유: 중복된 이름을 가진 사람이 있으므로 (dic은 중복key값을 인정해주지 않으므로, 중복된 이름을 가진 사람은 value값을 고쳐주려고)
        c_dic[i] += 1
    
    for i in participant: #위 과정을 participant에도 적용
        p_dic[i] = 0   
    for i in participant:
        p_dic[i] += 1    
    
    for i in participant: #completion에 participant(참가자가 없으면) 그 참가자 return
        if c_dic.get(i) == None:
            answer = i
        else:
            if c_dic[i] != p_dic[i]: #중복이름 검사: <completion에 통과한 i이름을 가진 사람 수 = i이름을 가진 participant의 사람수> 체크
                answer = i

    return answer