#프로그래머스 '완주하지 못한 선수'와 같은 문제 
import sys 

N = int(sys.stdin.readline())
participants = dict()
for i in range(N):
    part = sys.stdin.readline()
    if participants.get(part) == None:
        participants[part] = 1
        continue
    participants[part] += 1
origin_participants = participants.copy()    

for i in range(N-1):
    comp = sys.stdin.readline()
    participants[comp] += 1 
key_li = list(participants.keys())    
for key in key_li:
    if participants[key] != origin_participants[key]  * 2:
        print(key)
        break