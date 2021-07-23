# 해쉬
# key -value 쌍의 데이터를 저장하는 자료구조

# 완주하지 못한 선수
# 여러명이 참여해서 단 한명을 제외하고는 모드 완주에 성공하였다.
def solution(participant, completion):
    answer = ''
    # # 아이디어 1 : 
    # # 딕셔너리 구조를 활용해서 사람의 이름을 key로 그리고 0으로 지정했다가 완료한 사람의 값을 1로 변경해서 나중에 값이 0인 애를 출력
    # # 오류 = 동명이인이 있는 경우 오류를 발생시킨다.
    # arr = {}
    # for i in participant:
    #     arr[i] = 0
    # for j in completion:
    #     arr[j] = 1
    # for i in arr.keys():
    #     if arr[i] == 0:
    #         answer = i
    #         break

    # 아이디어 2:
    # # 딕셔너리 구조를 활용해서 사람의 이름을 key로 지정, 값을 1로 지정한다. 
    # 이때 동명이인인 경우를 대비해서 참여한 사람의 숫자만큼 valu의 값을 설정한다.
    # 이후에 완료자가 생성된 경우 해당 사람의 값에서 1을 제외해준다.
    # 따라서 최종적으로 0의 값이 아닌 사람이 완료자가 아니다.
    # 완료
    arr = {}
    for i in participant:
        if i in arr.keys():
            arr[i]  = arr[i]+ 1
        else:
            arr[i]=1
    for i in completion:
        arr[i]= arr[i]-1
    for i in arr.keys():
        if arr[i] >0:
            answer = i
            break
    return answer