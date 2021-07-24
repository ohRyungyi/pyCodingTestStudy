import sys

test_case_N = int(sys.stdin.readline())
result = []

for _ in range(test_case_N):
  N = int(sys.stdin.readline())
  first_key = list(map(str,sys.stdin.readline().split()))  # A B C D 
  second_key = list(map(str,sys.stdin.readline().split())) # B C D A 
  
  hash = dict()
  for i in range(N):
    hash[second_key.index(first_key[i])] = i
  sort_hash = sorted(hash.items())
  
  secrete_key = list(map(str,sys.stdin.readline().split()))
  normal_key = secrete_key.copy()
  
  for i in range(N):
    normal_key[sort_hash[i][1]] = secrete_key[i]

  normal_key = ' '.join(normal_key)
  result.append(normal_key)
print('\n'.join(result) )
  