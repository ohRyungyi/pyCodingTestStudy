#완주하지 못한 선수
def solution(participant, completion):
    answer = set(participant) - set(completion) #차집합 이용하는 것을 생각했음. 하지만 동명이인이 있을 시 집합은 중복을 제거함.

    if len(answer) == 0: #동명이인이 있다면 차집합을 한 요소의 개수는 0이됨.
        participant.sort() #정렬
        completion.sort() #정렬

        for i in range(len(completion)):
            if participant[i] != completion[i]:
                return participant[i]

    return list(answer)[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))

'''
다른 사람 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

배운 점
리스트의 모든 요소의 개수를 세서 dictionary로 출력하기를 원한다면 Counter을 사용하면 된다.

print(collections.Counter(participant)) >> Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
print(collections.Counter(completion)) >> Counter({'stanko': 1, 'ana': 1, 'mislav': 1})

answer = collections.Counter(participant)-collections.Counter(completion)
print(answer) >> Counter({'mislav': 1})

print(list(answer)[0]) >> mislav
print(list(answer.keys())[0]) >> mislav
'''

'''
입력 예시
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

출력 예시
"leo"

"vinko"

"mislav"
'''
