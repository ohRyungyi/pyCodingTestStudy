import sys 

N = int(sys.stdin.readline()) # N : 기준열

M = int(sys.stdin.readline()) # M : S열이 가지는 길이 
S = sys.stdin.readline() #길이 하나 더 받아짐
#공백을제거하거나 그냥 가면됨 
count = 0
result = 0
i = 0
while (i < M-2):
  #만약에 이게 맞다면 
  if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I': #이게맞다면 
    count += 1 
    if count == N: 
      result +=1
      count -= 1
    i += 1
  elif count != 0:
    count = 0
  i += 1  
  
  
print(result)