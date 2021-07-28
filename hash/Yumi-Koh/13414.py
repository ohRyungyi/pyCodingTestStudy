import sys
k, l = map(int,sys.stdin.readline().split())
n=1 # 수강신청 등록번호
dic = {}
for i in range(l):
    s = sys.stdin.readline().rstrip()
    dic[s] = n
    n+=1
sdict = sorted(dic.items(), key = lambda item: item[1]) # dic의 value값을 기준으로 내림차순 정렬
result=[]
if k<len(sdict): # 수강가능인원보다 신청인원이 많은 경우
    for i in range(k):
        result.append(sdict[i][0])
else: # 수강가능인원이 신청인원보다 많은 경우
    for i in range(len(sdict)):
        result.append(sdict[i][0])
for i in result:
    print(i)