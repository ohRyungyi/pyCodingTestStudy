import sys
from collections import Counter
N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
#평균
print(round(sum(li)/N)) 

#중앙값 
li.sort()
print((li[N // 2]))

#최빈값
co = Counter(li).most_common(2)
print(co) 
if len(co) == 1:
  print(co[0][0])
elif len(co) == 2:
  if co[0][1] == co[1][1]:
    print(co[1][0])
  else:
    print(co[0][0])


#범위
print(max(li) - min(li))



'''입력
5
1
3
8
-2
2
'''

'''출력
2
2
1
10
'''

'''입력
1
4000
'''

'''출력
4000
4000
4000
0
'''

'''입력
5
-1
-2
-3
-1
-2
'''

'''출력
-2
-2
-1
2
'''