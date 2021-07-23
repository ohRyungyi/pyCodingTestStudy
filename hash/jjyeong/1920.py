from sys import stdin, stdout

x = int(stdin.readline())
x = [1]*x
x_data = list(map(int,stdin.readline().split()))
dic = {name:value for name, value in zip(x_data, x)}
#print(dic)
#print(dic[5] == True)
y = int(stdin.readline())
y_data = list(map(int,stdin.readline().split())) 
for y_val in y_data:
  result = dic.get(y_val, 'Null')
  if result == 'Null':
    print(0)
  else:
    print(1) 