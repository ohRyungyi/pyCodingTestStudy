def solution(participant, completion):
    answer = set(participant) - set(completion)

    if len(answer) == 0:
        participant.sort()
        completion.sort()

        for i in range(len(completion)):
            if participant[i] != completion[i]:
                return participant[i]

    return list(answer)[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))

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
