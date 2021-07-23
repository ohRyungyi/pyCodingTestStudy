import sys 
input=sys.stdin.readline
result = []

while True:
  x = input().split('\n')[0] # 이거 말구 또는 x = sys.stdin.readline().srtip()
  if x == '*': # 종료조건 
    break
  count = 0 # 쓸데없어 보이지만 가장 중요한 변수

  naljibreak = True 
  for k in range(1, len(x)): # AABB 
    hash = dict() # 빈 딕셔너리에 넣기
    i = 0
    while i <= len(x)-1-k :
     
      if hash.get(x[i] + x[i+k]) == None: 
        hash[x[i] + x[i+k]]= 1
      elif hash[x[i] + x[i+k]] == 1:      
        naljibreak = False
        break
      i += 1

    if naljibreak == False:
      count = 1
      result.append(x+' is NOT surprising.')
      break  
      
  
  if count == 0:
    result.append(x+' is surprising.')

for list_ in result:
  print(list_)


'''입력
ZGBG #문자길이가 4인경우, 0 ~ (4-2) -> 문자길이가 N인경우, 0 ~ N-2
X
EE
AAB 0쌍 - (AA, AB) 1쌍 - (AB)
AABA 0쌍 -(AA, AB, BA) 1쌍 -(AB, AA) 2쌍 -(AA)
AABB 0쌍 -(AA, AB, BB) 1쌍 -(AB, AB) 2쌍 - (AB) -> UNSUPRISING 
BCBABCC 0쌍 -> UNSUPRISING 
*
'''

'''출력
ZGBG is surprising.
X is surprising.
EE is surprising.
AAB is surprising.
AABA is surprising.
AABB is NOT surprising.
BCBABCC is NOT surprising.
'''